import src.script as SC
import os

ROOT = os.getcwd()
arquivos = os.listdir(ROOT + '\\docs')
for arquivo in arquivos:
    file_path = ROOT + str('\\docs\\'+str(arquivo))
    leitor = SC.Script(file_path)
    leitor.pdf_to_db()
#pdf_obj = readPDF.gerar_csv(file_path)
