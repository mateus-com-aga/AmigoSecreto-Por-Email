# Sorteio de Amigo Secreto com Envio de E-mails 🎁

Este repositório contém um script em **Python** que realiza o sorteio de amigo secreto entre participantes e envia os resultados automaticamente por e-mail. 

O script:
- Garante que nenhum participante tire a si mesmo.
- Envia e-mails personalizados informando os resultados.
- Utiliza SMTP para envio de mensagens.

## 🛠 Funcionalidades
- **Sorteio aleatório:** Garante que ninguém seja sorteado para si mesmo.
- **Envio automático de e-mails:** Notifica cada participante sobre o resultado.
- **Personalização fácil:** Adicione participantes com nome e e-mail.

## 📋 Requisitos
Certifique-se de ter os seguintes requisitos:
- **Python 3.x** instalado.
- Bibliotecas nativas do Python:
  - `random`
  - `smtplib`
  - `email`

## 🚀 Como Usar

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/seu-usuario/amigo-secreto.git
   cd amigo-secreto

2. **Atualize os participantes:** Edite a lista no dicionário participantes no arquivo principal, adicionando os nomes e e-mails. Exemplo:
    ```bash
    participantes = {
    'Matheus': 'matheus.farias@teste.com.br',
    'Nome_2': 'nome_2@teste.com.br',
    'Nome_1': 'nome_1@teste.com.br',
    # Adicione mais participantes aqui
    }

3. **Configure as credenciais de e-mail:** No código, ajuste:
- `sender_email`: O e-mail que será usado para enviar as mensagens.
- `password`: A senha do e-mail.
- `smtp_server`: O servidor SMTP utilizado (exemplo: mail.seuservidor.com).

4. **Execute o script:**
   ```bash
   python amigo_secreto.py

5. **Verifique os resultados:**
- O sorteio será exibido no terminal.
- Cada participante receberá um e-mail com o resultado.

## ⚠️ Atenção
- Este script foi desenvolvido para aprendizado e demonstração. Certifique-se de cumprir as políticas de privacidade ao enviar e-mails para terceiros.

## 🌟 Contribuição
Sinta-se à vontade para abrir issues ou enviar pull requests para melhorias. Algumas ideias:
- Suporte a mais servidores de e-mail.
- Interface para adicionar participantes.
- Criptografia para maior segurança no envio.
