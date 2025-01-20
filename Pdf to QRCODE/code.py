from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import os
import qrcode

# Lista os arquivos.pdf na pasta 'pdfs'
lista_pdfs = os.listdir('Pdf to QRCODE\pdfs')
index_lista = 0

def upload_para_drive(caminho_do_arquivo):

    global nome_pdf
    # Define o nome a partir da última barra, retirando também o .pdf
    nome_pdf = (caminho_do_arquivo.split("/")[-1]).replace(".pdf", "")
    
    #Setup
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile("Pdf to QRCODE\client_secrets.json")
    gauth.LocalWebserverAuth()
    drive = GoogleDrive(gauth)

    #Cria o arquivo                 
    arquivo_drive = drive.CreateFile({
        'title': nome_pdf
    })
    
    #Dá conteúdo ao arquivo
    arquivo_drive.SetContentFile(caminho_do_arquivo)

    #Faz o upload do arquivo
    arquivo_drive.Upload()
  
    # Adiciona permissão para todos
    arquivo_drive.InsertPermission({
    'type': 'anyone',
    'value': 'anyone',
    'role': 'reader'
    })
    
    global link_pdf
    link_pdf = arquivo_drive['alternateLink']

for i in range(1, len(lista_pdfs) + 1):
    upload_para_drive(f"Pdf to QRCODE/pdfs/{lista_pdfs[index_lista]}")

    # Faz um qrcode com o link do pdf
    qr = qrcode.make(link_pdf)
    qr.save(f"{nome_pdf}.png")

    # Passa para o próximo nome na lista de pdfs
    index_lista += 1