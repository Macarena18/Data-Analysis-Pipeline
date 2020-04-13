import pandas as pd

def acquire():
    data=pd.read_csv('src/atp_clean.csv')
    return data

def filters(df,year,tour):
    filtered=df[(df["Year"]==year)&(df["Tournament"]==tour)]
    if year not in df["Year"]:
        print("No es posible realizar el análisis de este año. Por favor, incluye 2017,2018 o 2019.")
    else:
        print(filtered)
    if tour not in df["Tournament"]:
        print("No es posible realizar el análisis de este torneo. Por favor, incluye AustralianOpen, RolandGarros, Wimbledon,USOpen.")
    else:
        print(filtered)
    return filtered

def analysis(df):
    grouped=df.groupby("Winner").agg({"Round":"count"}).reset_index()
    results=grouped.sort_values("Round",ascending=False).head(10)
    print(results)
    return results

