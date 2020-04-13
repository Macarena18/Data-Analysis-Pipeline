import pandas as pd

def acquire():
    data=pd.read_csv('src/atp_clean.csv')
    return data

def filters(df,year,tour):
    filtered=df[(df["Year"]==year)&(df["Tournament"]==tour)]
    print(filtered)
    return filtered

def analysis(df):
    grouped=df.groupby("Winner").agg({"Round":"count"}).reset_index()
    results=grouped.sort_values("Round",ascending=False).head(10)
    print(results)
    return results

