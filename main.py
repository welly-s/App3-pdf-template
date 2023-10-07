from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')    #P is potrait, L is landscape

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    pdf.add_page()  #to create page
    pdf.set_font(family='Times',style="B", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1, border=0)   # w= cell width, ln= move to next line
    pdf.line(x1=10, y1=20, x2=200, y2=20)



pdf.output('output.pdf')