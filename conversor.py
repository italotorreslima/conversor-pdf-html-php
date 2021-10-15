import fitz
import os
from PIL import Image

pdffile = "myfile.pdf"
doc = fitz.open(pdffile)
pagesNumber = len(doc)
for i in range(pagesNumber):
    pagina = doc.loadPage(i)
    pix = pagina.getPixmap(matrix=fitz.Matrix(150/72,150/72))
    imagem = ("{}imagem.png".format(i))
    pix.writePNG(imagem)
for i in range(pagesNumber):
    im1 = Image.open(r"{}imagem.png".format(i))
    im1.save(r"{}imagem.jpg".format(i))
    os.remove("{}imagem.png".format(i)) 