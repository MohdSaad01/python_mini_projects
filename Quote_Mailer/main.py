import random
import smtplib

import datetime as dt
day=dt.datetime.now().weekday()

my_email = "Sender@gmail.com"  # Enter you Sender Gmail Here!
password = "App_Password"  # Enter your App Password form your Gmail account!


if day==0:
    with open(file="quotes.txt") as file:
        quotes=file.readlines()
        randomquote=random.choice(quotes)
        print(randomquote)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(from_addr=my_email,
                            to_addrs="Receiver@gmail.com", #Enter the Receivers Gmail Here!
                            msg=f"Subject:Motivational Quote \n\n {randomquote}")
