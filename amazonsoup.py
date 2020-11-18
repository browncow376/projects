import requests
from bs4 import BeautifulSoup
import time
import smtplib

url = 'https://www.amazon.com/Gaming-GeForce-Overclocked-Graphics-TUF-GTX1660S-O6G-GAMING/dp/B081SPGMBD/ref=sr_1_5?crid=2U0CBKFOVY77E&dchild=1&keywords=gtx+1660+super&qid=1592755355&sprefix=gtx+1660+%2Caps%2C154&sr=8-5'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Safari/537.36"}

def check_price():
    page = requests.get(url, headers=headers)

    soup = BeautifulSoup(page.content, "html.parser")

    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    converted_price = float(price[1:5])

    if(converted_price > 2.200):
        send_mail()

    print(converted_price)
    print(title.strip())

def send_mail():
    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login("spy84g@gmail.com", "zvsbpzitxreutisd")

    subject = "Price is down"
    body = "Check the amazon link: \n https://www.amazon.com/Gaming-GeForce-Overclocked-Graphics-TUF-GTX1660S-O6G-GAMING/dp/B081SPGMBD/ref=sr_1_5?crid=2U0CBKFOVY77E&dchild=1&keywords=gtx+1660+super&qid=1592755355&sprefix=gtx+1660+%2Caps%2C154&sr=8-5"

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        "spy84g@gmail.com",
        "jgcp84@gmail.com",
        msg
    )           
    print('Email has been sent')

    server.quit()

while(True):
    check_price()
    time.sleep(60)


