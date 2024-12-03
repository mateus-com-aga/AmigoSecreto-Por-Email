import random
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

participantes = {
  'Matheus': 'matheus.farias@teste.com.br',
  'Nome_2': 'nome_2@teste.com.br',
  'Nome_1': 'nome_1@teste.com.br',
}

# Função para realizar o sorteio
def sortear_amigo_secreto(participantes):
    nomes = list(participantes.keys())
    sorteados = nomes[:]
    random.shuffle(sorteados)

    resultado = {}
    for i, nome in enumerate(nomes):
        if nome == sorteados[i]:  # Garante que ninguém tire a si mesmo
            return sortear_amigo_secreto(participantes)
        resultado[nome] = sorteados[i]

    return resultado

# Função para enviar e-mail
def enviar_email(email, amigo_secreto):
    smtp_server = 'mail.teste.com.br'
    port = 587
    sender_email = 'Seu e-mail aqui.'
    password = 'Sua senha aqui.'

    subject = 'Amigo Secreto - Resultado'
    body = f'Olá, você tirou {amigo_secreto} no amigo secreto! 🎁'

    # Configuração do e-mail
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Enviando o e-mail
    try:
        server = smtplib.SMTP(smtp_server, port)
        server.starttls()
        server.login(sender_email, password)
        server.sendmail(sender_email, email, msg.as_string())
        print(f'E-mail enviado para {email}')
    except Exception as e:
        print(f'Erro ao enviar e-mail para {email}: {e}')
    finally:
        server.quit()

# Realizar o sorteio
sorteio = sortear_amigo_secreto(participantes)

# Enviar e-mails para os participantes
for nome, amigo_secreto in sorteio.items():
    email = participantes[nome]
    enviar_email(email, amigo_secreto)

# Imprimir a lista dos sorteados no final
print("\nResultado do sorteio de Amigo Secreto:")
for nome, amigo_secreto in sorteio.items():
    print(f"{nome} tirou {amigo_secreto}")