import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from argparse import ArgumentParser
from analysis import *
from graficos import *
from analysis2 import *


def parse():
    parser=ArgumentParser(description="Este programa es para buscar los 10 mejores tenistas para cada torneo y año seleccionado")
    parser.add_argument("--year",dest="year",type=int,help="el año en el que se disputó el torneo. El análisis está disponible para los años 2017,2018,2019")
    parser.add_argument("--tour",dest="tour",help="el torneo en el que estamos interesados en saber el resultado de los tenistas. El análisis está disponible para cualquiera de los torneos Grand Slam: AustralianOpen, RolandGarros, Wimbledon")
    return parser.parse_args()
    

def main():
    args=parse()
    year=args.year
    tour=args.tour
    print(year)
    print(tour)
    data=acquire()
    filtered = filters(data,year,tour)
    results = analysis(filtered)
    barchart = visualize(results,tour,year)
    save_chart(barchart,tour,year)
    filtered2 = filters2(data)
    results2 = analysis2(filtered2)
    winners_data = acquire2()
    
if __name__ == '__main__':
    main()

