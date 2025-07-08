import os, smtplib
from email.mime.text import MIMEText

leads=["hedge1@fund.ai","quant2@bank.com"]
for lead in leads:
    msg=MIMEText(f"Scopri il nostro Robo-Advisor Quantistico: {os.getenv('APP_DOMAIN')}/subscribe")
    msg["Subject"]="Quantum Portfolio 🚀"
    msg["From"]=os.getenv("SMTP_USER")
    msg["To"]=lead
    with smtplib.SMTP(os.getenv("SMTP_HOST")) as conn:
        conn.login(os.getenv("SMTP_USER"), os.getenv("SMTP_PASS"))
        conn.send_message(msg)
