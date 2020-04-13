# Project 2 - Data Analysis Pipeline

Para este proyecto utilizo:
- Dataset ATP descargado de Kaggle -> https://www.kaggle.com/hwaitt/tennis-20112019
- API - TheSportsDB -> https://www.thesportsdb.com/api.php
- Web Scrapping - Articulo La Nación -> https://www.lanacion.com.ar/deportes/tenis/el-ranking-historico-ganancias-del-tenis-quien-nid2267639

**Cleaning Dataset:**

En primer lugar, realizo la limpieza de datos del dataset descargado `Cleaning.ipynb`:
- Elimino columnas no necesarias
- Limpio contenido de las columnas
- Creo nuevas columnas necesarias para el posterior ánalisis
- Genero nuevo CSV (`atp_clean.csv`) con datos limpios.

**API & Web Scrapping:**

En segundo lugar, tras identificar los ganadores de GrandSlam de los últimos años, procedo a obtener los datos personales (Nacionalidad,Fecha de nacimiento, Altura) de estos jugadores a través de la `API de TheSportsDB` incluyendo los parametros de cada jugador. 

Además, realizo un  `Web Scrapping` para obtener el total de ganancias de cada uno de estos jugadores.

Tras obtener estos datos a través de la API y Web Scrapping, creo un nuevo dataframe con ambos datos (`winners_atp.csv`).

**Script:**

Por último, procedo a crear un programa de python `main.py` para generar el análisis de  los 10 mejores tenistas para cada torneo y año seleccionado. Para ello, he utilizado `argparse` para crear dos parametros "year" y "tour" que van a filtrar el dataset.

Este programa va a generar:
- Gráfica con los 10 tenistas con mejores resultados en cada torneo (con más victorias) `analysis.py` `barcharts.py`
- Imagen guardada de la gráfica `barcharts.py`
- Dataframe con el nombre de los tenistas ganadores de los últimos GrandSlams y la media de sets y juegos disputados por cada jugador. `analysis2.py`
- De estos jugadores, dataframe con sus datos personales (Nacionalidad,Fecha de nacimiento, Altura y Ganancias). `analysis2.py`
- Envío de email usando la librería de  python `smtplib`. 







