import pandas as pd
from analysis import *

def filters2(df):
    filtered2=df[(df["Round"]==12)]
    print(filtered2)
    return filtered2

def analysis2(df):
    grouped2=df.groupby("Winner").agg({"Round":"count","Total_games":"mean","Total_sets":"mean"})
    results2=grouped2.sort_values("Round",ascending=False)
    print("Estos son los ganadores de Grand Slams de los últimos años (2017,2018,2019) con el número total de titulos(Round), media de juegos por partido y media de sets jugados:")
    print(results2)
    return results2

def acquire2():
    winners_data=pd.read_csv('src/winners_clean.csv')
    winners_data=winners_data.drop(columns=["Unnamed: 0"])
    print("Además, estos son los datos personales de cada ganador: Nacionalidad, Fecha de Nacimiento, Altura, Ganancias:", winners_data)
    return winners_data



