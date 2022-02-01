import requests, sys, time, os, argparse

# Lista de características fáciles de recopilar
snippet_features = ["title",
                    "publishedAt",
                    "channelId",
                    "channelTitle",
                    "categoryId"]

# Cualquier carácter para excluir, generalmente estas son cosas que se vuelven problemáticas en archivos CSV
unsafe_characters = ['\n', '"']

# Se usa para identificar columnas, orden codificado actualmente
header = ["video_id"] + snippet_features + ["trending_date", "tags", "view_count", "likes", "dislikes",
                                            "comment_count", "thumbnail_link", "comments_disabled",
                                            "ratings_disabled", "description"]


def setup(api_path, code_path):
    with open(api_path, 'r') as file:
        api_key = file.readline()

    with open(code_path) as file:
        country_codes = [x.rstrip() for x in file]

    return api_key, country_codes


def prepare_feature(feature):
   # Elimina cualquier carácter de la lista de caracteres no seguros y rodea todo el elemento entre comillas
    for ch in unsafe_characters:
        feature = str(feature).replace(ch, "")
    return f'"{feature}"'


def api_request(page_token, country_code):
    # Construye la URL y solicita el JSON de ella
    request_url = f"https://www.googleapis.com/youtube/v3/videos?part=id,statistics,snippet{page_token}chart=mostPopular&regionCode={country_code}&maxResults=50&key={api_key}"
    request = requests.get(request_url)
    if request.status_code == 429:
        print("Temp-Banned due to excess requests, please wait and continue later")
        sys.exit()
    return request.json()


def get_tags(tags_list):
    # Toma una lista de etiquetas, prepara cada etiqueta y las une en una cadena por el carácter de canalización
    return prepare_feature("|".join(tags_list))


def get_videos(items):
    lines = []
    for video in items:
        comments_disabled = False
        ratings_disabled = False

        # Podemos suponer que algo anda mal con el video si no tiene estadísticas, a menudo esto significa que se ha eliminado
         # para que podamos omitirlo
        if "statistics" not in video:
            continue

        # Puede encontrar una explicación completa de todas estas características en la página de GitHub para este proyecto
        video_id = prepare_feature(video['id'])

        # El fragmento y las estadísticas son subdictaciones del video que contienen la información más útil
        snippet = video['snippet']
        statistics = video['statistics']

        # Esta lista contiene todas las funciones en el fragmento que tienen 1 de profundidad y no requieren un procesamiento especial
        features = [prepare_feature(snippet.get(feature, "")) for feature in snippet_features]

        # Las siguientes son características de casos especiales que requieren un procesamiento único o no están dentro del dictado del fragmento
        description = snippet.get("description", "")
        thumbnail_link = snippet.get("thumbnails", dict()).get("default", dict()).get("url", "")
        trending_date = time.strftime("%y.%d.%m")
        tags = get_tags(snippet.get("tags", ["[none]"]))
        view_count = statistics.get("viewCount", 0)

        # Esto puede no estar claro, esencialmente la forma en que funciona la API es que si un video tiene comentarios o calificaciones deshabilitados
         # entonces no tiene ninguna función para ello, por lo tanto, si no existen en el dictado de estadísticas, sabemos que están deshabilitados
        if 'likeCount' in statistics and 'dislikeCount' in statistics:
            likes = statistics['likeCount']
            dislikes = statistics['dislikeCount']
        else:
            ratings_disabled = True
            likes = 0
            dislikes = 0

        if 'commentCount' in statistics:
            comment_count = statistics['commentCount']
        else:
            comments_disabled = True
            comment_count = 0

        # Compila todos los diversos bits de información en una línea con formato consistente
        line = [video_id] + features + [prepare_feature(x) for x in [trending_date, tags, view_count, likes, dislikes,
                                                                       comment_count, thumbnail_link, comments_disabled,
                                                                       ratings_disabled, description]]
        lines.append(",".join(line))
    return lines


def get_pages(country_code, next_page_token="&"):
    country_data = []

   # Debido a que la API usa tokens de página (que son literalmente la misma función de los números en todas partes) es mucho
     # más inconveniente para iterar sobre las páginas, pero eso es lo que se hace aquí.
    while next_page_token is not None:
        # A page of data i.e. a list of videos and all needed data
        video_data_page = api_request(next_page_token, country_code)

        # Obtenga el token de la página siguiente y cree una cadena que se pueda inyectar en la solicitud con él, a menos que sea Ninguno,
         # entonces deja que todo sea Ninguno para que el ciclo termine después de este ciclo
        next_page_token = video_data_page.get("nextPageToken", None)
        next_page_token = f"&pageToken={next_page_token}&" if next_page_token is not None else next_page_token

        # Obtenga todos los elementos como una lista y deje que get_videos devuelva las funciones necesarias
        items = video_data_page.get('items', [])
        country_data += get_videos(items)

    return country_data


def write_to_file(country_code, country_data):

    print(f"Writing {country_code} data to file...")

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    with open(f"{output_dir}/{time.strftime('%y.%d.%m')}_{country_code}_videos.csv", "w+", encoding='utf-8') as file:
        for row in country_data:
            file.write(f"{row}\n")


def get_data():
    for country_code in country_codes:
        country_data = [",".join(header)] + get_pages(country_code)
        write_to_file(country_code, country_data)


if __name__ == "__main__":

    parser = argparse.ArgumentParser()
    parser.add_argument('--key_path', help='Path to the file containing the api key, by default will use api_key.txt in the same directory', default='api_key.txt')
    parser.add_argument('--country_code_path', help='Path to the file containing the list of country codes to scrape, by default will use country_codes.txt in the same directory', default='country_codes.txt')
    parser.add_argument('--output_dir', help='Path to save the outputted files in', default='output/')

    args = parser.parse_args()

    output_dir = args.output_dir
    api_key, country_codes = setup(args.key_path, args.country_code_path)

    get_data()