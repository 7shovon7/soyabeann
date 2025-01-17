# -*- coding: utf-8 -*-
"""chaldal.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1aeo4MqWcBx852796VjUTgiXapl3FMH8q
"""

import requests
from bs4 import BeautifulSoup

import smtplib
from email.message import EmailMessage

from time import sleep

rupchada_5ltr = "https://chaldal.com/rupchanda-soyabean-oil-5-ltr-5"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.111 Safari/537.36"}


def get_price(product_link, headers):
    r = requests.get(url=product_link, headers=headers)
    soup = BeautifulSoup(r.content, "html.parser")
    product_name = soup.find("h1", attrs={"itemprop": "name"}).get_text()
    product_price = soup.find("span", attrs={"itemprop": "price"}).get_text()
    return [product_name, product_price]


my_email = 'amberabder@gmail.com'
my_password = 'hkxwafzzepqxtyee'


def send_email_to(smtp, person_name, e_mail, prod_name, prod_price):
    msg = EmailMessage()
    msg['From'] = 'Amber Abder'
    msg['To'] = e_mail
    msg['Subject'] = "Price of soyabean oil has been gone down"
    msg_body = f'''
  Hi {person_name},
  The price of {prod_name} has been down to {prod_price} taka. You can check the price at http://www.chaldal.com.
  '''
    msg.set_content(msg_body)
    smtp.send_message(msg)


run_program = True
with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
    smtp.login(my_email, my_password)
    while run_program:
        prod_details = get_price(product_link=rupchada_5ltr, headers=headers)
        if int(prod_details[1]) > 550:
            send_email_to(smtp, "Shovon", "mahmudur.rahman99@gmail.com",
                          prod_details[0], prod_details[1])
        sleep(180)
