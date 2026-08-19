# To run and test the code you need to update 4 places:
# 1. Change MY_EMAIL/MY_PASSWORD to your own details.
# 2. Go to your email provider and make it allow less secure apps.
# 3. Update the SMTP ADDRESS to match your email provider.
# 4. Update birthdays.csv to contain today's month and day.
# See the solution video in the 100 Days of Python Course for explainations.


import datetime
import smtplib
from email.message import EmailMessage


# import os and use it to get the Github repository secrets
USERNAME = os.environ.get("USERNAME")
PASSWORD = os.environ.get("PASSWORD")

def send_email(day):
    msg = EmailMessage()
    msg["Subject"] = "It's Raise Day B*tches!"
    msg["From"] = USERNAME
    msg["To"] = USERNAME
    msg.set_content(f"It's the {day}th today! Gather your balls and ask for a raise!")

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(USERNAME, PASSWORD)
        connection.send_message(msg)



x = datetime.datetime.now()
day_of_month = x.strftime("%d")

if int(day_of_month) == 19:
    send_email(day_of_month)
