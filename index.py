import src.script as SC
import os

ROOT = os.getcwd()
file_path = ROOT + str('\\docs\\2021-7.pdf')

leitor = SC.Script(file_path)
leitor.pdf_to_db()
#pdf_obj = readPDF.gerar_csv(file_path)
