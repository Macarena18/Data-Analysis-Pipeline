from fpdf import FPDF 
import webbrowser as web
from barcharts import *
from analysis2 import *


def create_pdf(tour,year,text,text1):
    pdf=FPDF("P","mm","A4")
    pdf.add_page()
    pdf.set_font("Arial","B",7)
    pdf.text(10,10,f"Top 10 Players {tour} {year}")
    pdf.set_xy(10,110)
    pdf.image("Top 10 players.png",x = 0.25, y = 0.25, w = 0, h = 0)
    pdf.output("report_pdf.pdf","F")
    
    
    

