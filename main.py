import smtplib
from email.message import EmailMessage
from secrets import password

# E-mail config
EMAIL_ADDRESS = ''
EMAIL_PASSWORD = password

# =====|===+|==== PORTUGUÊS ====|+===|+=====

"""
MUDANÇA DO GOOGLE - 30-06-2022

1º Configure seu email para verificação em duas etapas:
-Acesse a parte "Gerenciar sua Conta do Google"
-Selecione o menu "Segurança"
-Realize os procedimentos de "Verificação em duas etapas"
2º No menu "Segurança" clique em "Senhas de App"
3º Clique em "Selecionar app"
4º Clique em "Outro" digite o nome que você quer dar para seu APP
*5º Copie a senha que irá aparecer. NÃO TEM COMO RECUPERÁ-LA.
6º Cole a senha gerada no campo "password" em secrets.py
7º Execute este programa
"""

# Criando e-mail

msg = EmailMessage()
# Título do e-mail
msg['Subject'] = 'Título do E-mail!'
# Quem vai enviar
msg['From'] = ''
# Quem vai receber
msg['To'] = ''
# Conteúdo
msg.set_content('Conteúdo do E-mail!')

# Enviar e-mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)

# =====|===+|==== ENGLISH ====|+===|+=====

"""
GOOGLE UPDATE - 30-06-2022

1º Configure your email with 2-Step Verification:
-Access "Manage your Google Account"
-Select "Security" menu
-Perform the "2-Step Verification" procedures
2º In "Security" menu, go to "App passwords"
3º Click in "Selecionar app"
4º Click in "Other" and type the name you want for your APP
*5º Copy the generated password. YOU CAN NOT RECOVER IT AFTERWARDS.
6º Paste the generated password in "password" field at secrets.py
7º Run this app
"""

# Creating e-mail
"""
msg = EmailMessage()
# E-mail's title
msg['Subject'] = 'Title'
# Who's sending
msg['From'] = ''
# Who's receiving
msg['To'] = ''
# Content
msg.set_content('Content.')

# Send e-mail
with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
    smtp.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    smtp.send_message(msg)
"""