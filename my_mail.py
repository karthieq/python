import smtplib

with smtplib.SMTP('localhost') as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()

    smtp.login()
