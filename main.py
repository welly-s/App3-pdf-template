from fpdf import FPDF
import pandas as pd

pdf = FPDF(orientation='P', unit='mm', format='A4')    #P is potrait, L is landscape
pdf.set_auto_page_break(auto=False, margin=0)  #prevent automatic page break

df = pd.read_csv('topics.csv')

for index, row in df.iterrows():
    # Add header
    pdf.add_page()  #to create page
    pdf.set_font(family='Times',style="B", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0, h=12, txt=row['Topic'], align='L', ln=1, border=0)   # w= cell width, ln= move to next line
    pdf.line(x1=10, y1=20, x2=200, y2=20)

    pdf.ln(255) # create breakline in predefined unit

    # Add footer
    pdf.set_font(family='Times', style="I", size=8)
    pdf.set_text_color(180, 180, 180)
    pdf.cell(w=0, h=10, txt=row['Topic'], align='R', ln=0, border=0)



    for x in range(int(row['Pages'])-1):
        pdf.add_page()

        pdf.ln(265)  # create breakline in predefined unit
        # Add footer
        pdf.set_font(family='Times', style="I", size=8)
        pdf.set_text_color(180, 180, 180)
        pdf.cell(w=0, h=10, txt=row['Topic'], align='R', ln=0, border=0)

pdf.output('output.pdf')