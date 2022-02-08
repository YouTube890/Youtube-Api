## Función dataPlayList

Para llamar la función `dataPlayList()` importamos del archivo *dataApiYouTube.py* que se encuentra en este repositorio


```python
from dataApiYouTube import dataPlayList
```

Luego es necesario tener una llave de la Api de YouTube v3 para poder correr la función. En la sección inicial de [consultas](#Consultas/README.md) mostramos como crearla. Tambien es necesario proveer un link de una lista de reproducción activa de YouTube.

Vamos a ver un ejemplo de el uso de la función


```python
apiKey='AIzaSyDqq-BEw8S5_mJq60d5QGZcBv13Gyu6qiw'

playlistId='PLquqRxGjdk0746Gtzb102zxI3gmDVJts5'
```


```python
dataPlayList(api_Key=apiKey,playlist_Id=playlistId)
```




    [{'Views': 468502,
      'Likes': 7489,
      'Favorite': 0,
      'Coments': 227,
      'Duration': 'PT4M54S',
      'Dimension': '2d',
      'Definition': 'sd',
      'Caption': 'false',
      'UploadDate': '2017-08-28T12:00:03Z',
      'Title': '1. MAGNITUDES FÍSICAS (Teoría)',
      'URL': 'https://youtu.be/bMpHEu-pzhw'},
     {'Views': 110385,
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



### Función dataChannels
Para llamar la función `dataChannel()` importamos del archivo *dataApiYouTube.py* que se encuentra en este repositorio


```python
from dataApiYouTube import dataChannel
```

Luego es necesario tener una llave de la Api de YouTube v3 para poder corre la función. En la sección inicial de [consultas]() mostramos como crearla. También es necesario proveer un link del canal o el nombre de usuario del canal, el cual es necesario que sea un canal activo en YouTube.

Vamos a ver un ejemplo del uso de está función


```python
apiKey='AIzaSyDqq-BEw8S5_mJq60d5QGZcBv13Gyu6qiw'

channelId='UNsedebogota'
```


```python
dataChannel(api_Key=apiKey,channel_Id=channelId)
```




    [{'Views': 1012,
      'Likes': '28',
      'Favorite': 0,
      'Coments': '11',
      'Duration': 'PT5M6S',
      'Dimension': '2d',
      'Definition': 'hd',
      'Caption': 'false',
      'UploadDate': '2021-12-16T13:45:00Z',
      'Title': 'Historia del Edificio de Bellas Artes de la UNALBogotá',
      'URL': 'https://youtu.be/WVVdC2Sm7sE'},
     {'Views': 75,
      'Likes': '3',
      'Favorite': 0,
      'Coments': '0',
      'Duration': 'PT6M11S',
      'Dimension': '2d',
      'Definition': 'hd',
      'Caption': 'false',
      'UploadDate': '2021-12-15T20:12:50Z',
      'Title': 'Balance final del año y de los #EncuentrosVRI 2021 - #UNALBogotá',
      'URL': 'https://youtu.be/cXB6QqgCfi4'},
     
     .
     .
     .
     
     {'Views': 5261,
      'Likes': '89',
      'Favorite': 0,
      'Coments': '0',
      'Duration': 'PT7M55S',
      'Dimension': '2d',
      'Definition': 'hd',
      'Caption': 'false',
      'UploadDate': '2014-05-21T23:13:47Z',
      'Title': 'Rendición de Cuentas - UN Sede Bogotá',
      'URL': 'https://youtu.be/vIe8iiX0zv8'}]




```python

```

### Función dataSearch
Para llamar la función `dataSearch()` importamos del archivo *dataApiYouTube.py* que se encuentra en este repositorio


```python
from dataApiYouTube import dataSearch
```

Luego es necesario tener una llave de la Api de YouTube v3 para poder correr la función. En la sección inicial de [consultas](#Consultas/README.md) mostramos como crearla. Tambien es necesario proveer un link de una lista de reproducción activa de YouTube.

Vamos a ver un ejemplo de el uso de la función


```python
apiKey='AIzaSyDqq-BEw8S5_mJq60d5QGZcBv13Gyu6qiw'

query='Big Data'
```


```python
search = dataSearch(api_Key=apiKey,query_Id=query)
search
```




    [{'Views': 645266,
      'Likes': '16355',
      'Favorite': 0,
      'Coments': '369',
      'Duration': 'PT15M42S',
      'Dimension': '2d',
      'Definition': 'hd',
      'Caption': 'false',
      'UploadDate': '2019-04-14T04:10:07Z',
      'Title': '¿Qué es el Big Data?',
      'URL': 'https://youtu.be/M26iIqmqWkI',
      'ChannelId': 'UCP15FVAA2UL-QOcGhy7-ezA'},
     {'Views': 788962,
      'Likes': '15877',
      'Favorite': 0,
      'Coments': '1577',
      'Duration': 'PT5M12S',
      'Dimension': '2d',
      'Definition': 'hd',
      'Caption': 'false',
      'UploadDate': '2019-12-10T14:30:02Z',
      'Title': 'Big Data In 5 Minutes | What Is Big Data?| Introduction To Big Data |Big Data Explained |Simplilearn',
      'URL': 'https://youtu.be/bAyrObl7TYE',
      'ChannelId': 'UCsvqVGtbbyHaMoevxPAq9Fg'},
     
     .
     .
     .
     
     {'Views': 9,
      'Likes': '0',
      'Favorite': 0,
      'Coments': None,
      'Duration': 'PT20M33S',
      'Dimension': '2d',
      'Definition': 'hd',
      'Caption': 'false',
      'UploadDate': '2022-02-04T13:48:22Z',
      'Title': 'UAS Big Data - Vera Oktavia Purba - 16118058 - 4 Logistik D',
      'URL': 'https://youtu.be/IO4sYmP_GLk',
      'ChannelId': 'UCE08Biy8omoj0N66pIpgfiA'}]



Es importante tener en cuenta que la búsqueda arroja en ocasiones un gran número de videos, por lo que en usualmente se debe esperar un poco a que se carguen los datos.


```python
len(search)
```




    591




```python

```
