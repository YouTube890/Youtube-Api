## Función dataPlayList

Para llamar la función `dataPlayList()` importamos el archivo *dataApiYouTube.py* que se encuentra en este repositorio


```python
from dataApiYouTube import dataPlayList
```

Luego es necesario tener una llave de la Api de YouTube v3 para poder correr la función. En la sección inicial de [consultas](#Consultas/README.md) mostramos como crearla. Tambien es necesario proveer un link de una lista de reproducción activa de YouTube.

Vamos a ver un ejemplo de el uso de la función. Primero definimos las dos variables que requiere la función.


```python
apiKey='AIzaSyDqq-BEw8S5_mJq60d5QGZcBv13Gyu6qiw'

playlistId='PLquqRxGjdk0746Gtzb102zxI3gmDVJts5'
```

Luego ejeecutamos la función y obtenemos un archivo `.JSON` con la URL, Titulo, Definición, Dimensión, Numero de comentarios, Numero de favoritos, Likes y vistas; de los videos incluidos en la lista de reproducción proporcionada. 

```python
dataPlayList(api_Key=apiKey,playlist_Id=playlistId)
```




    [{'Views': 468469,
      'Likes': 7487,
      'Favorite': 0,
      'Coments': 227,
      'Duration': 'PT4M54S',
      'Dimension': '2d',
      'Definition': 'sd',
      'Caption': 'false',
      'UploadDate': '2017-08-28T12:00:03Z',
      'Title': '1. MAGNITUDES FÍSICAS (Teoría)',
      'URL': 'https://youtu.be/bMpHEu-pzhw'},
     {'Views': 110371,
      'Likes': 1555,
      'Favorite': 0,
      'Coments': 53,
      'Duration': 'PT2M44S',
      'Dimension': '2d',
      'Definition': 'sd',
      'Caption': 'false',
      'UploadDate': '2017-08-30T12:00:03Z',
      'Title': '2. MAGNITUDES FÍSICAS (Ejercicio 1)',
      'URL': 'https://youtu.be/VSL5aFjRR0c'},
      
      .
      .
      .
      
     {'Views': 25478,
      'Likes': 519,
      'Favorite': 0,
      'Coments': 53,
      'Duration': 'PT7M25S',
      'Dimension': '2d',
      'Definition': 'sd',
      'Caption': 'false',
      'UploadDate': '2018-09-24T17:03:25Z',
      'Title': '101. MOMENTO DE UNA FUERZA (Ejercicio 2)',
      'URL': 'https://youtu.be/ZLazF5ZIgi8'}]




```python

```
