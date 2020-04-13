
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import smtplib
from email.message import EmailMessage
from analysis import *


def visualize(df,tour,year):
    title = 'Top 10 players '+ tour+ " "+ str( year)
    fig, ax = plt.subplots(figsize=(23,8))
    barchart = sns.barplot(data=df, x='Winner', y='Round')
    plt.title(title + "\n", fontsize=22)
    print(barchart)
    return barchart

def save_chart(graph,tour,year):
    title = 'Top 10 players '+ tour+ " "+ str( year)
    fig=graph.get_figure()
    fig.savefig(title + '.png')

def email():
    EMAIL_ADDRESS=os.environ.get("EMAIL_USER")
    EMAIL_PASSWORD=os.environ.get("EMAIL_PASS")
    destination=input("Introduce your email:")
    msg=EmailMessage()
    msg["Subject"]="Check out my Proyect 2: Data Pipeline!"
    msg["From"]=EMAIL_ADDRESS
    msg["To"]= destination
    msg.set_content("These are the top 10 player of the tournament")
    files=['Top 10 players RolandGarros 2019.png']
    for file in files:
        with open(file,"rb") as f:
            file_data=f.read()
            file_type=imghrd.what(f.name)
            file_name=f.name
    msg.add_attachment(file_data,maintype="image",subtype=file_type,filename=file_name)
    with smtplib.SMTP_SSL(destination,465) as smtp:
        smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
        smtp.send_message(msg)

