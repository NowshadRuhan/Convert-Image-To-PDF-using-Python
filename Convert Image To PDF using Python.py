from fpdf import FPDF
from IPython.display import IFrame

pdf = FPDF()
x=2
w=120
h=120
pdf.add_page()
pdf.image("inport_img.jpg", x, w, h)
pdf.output("newfile.pdf", "F")
IFrame("newfile.pdf", width=600, height=300)