
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from analysis import *


def visualize(df,tour,year):
    title = 'Top 10 players '+ tour+ " "+ str( year)
    fig, ax = plt.subplots(figsize=(15,8))
    barchart = sns.barplot(data=df, x='Winner', y='Round')
    plt.title(title + "\n", fontsize=10)
    return barchart

def save_chart(graph):
    title2 = 'Top 10 players'
    fig=graph.get_figure()
    fig.savefig(title2 + '.png')
    
