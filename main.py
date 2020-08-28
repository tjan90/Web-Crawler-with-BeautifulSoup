import requests
from bs4 import BeautifulSoup
import html5lib
import smtplib
import time

def main():
    URL = 'https://www.amazon.it/Samsung-MZ-V7E1T0BW-SSD-970-NVMe/dp/B07CGJNLBB/'
    headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:79.0) Gecko/20100101 Firefox/79.0'}

    page = requests.get(URL, headers=headers)
    soup = BeautifulSoup(page.content, 'html5lib')

    #print(soup.prettify())

    title = soup.find(id="productTitle").get_text()
    title = title.strip()
    price =  soup.find(id="priceblock_ourprice").get_text()

    #t = soup.find('span', {'class': 'a-size-large product-title-word-break'})
    print(f"Title: {title.strip()}\n Price : {price} ")

    coverted_price = float(price[:-5])
    print(coverted_price)
    if(coverted_price < 170):
        sendMail(title, URL)


def sendMail(item, url):
    print("Sending Email...")
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('Enter-Your-Email-Here@mail.com', 'Password-for-Email-here')
    subject = f'Amazon Price drop of Item {item}'
    email_body = f'Please see the below item, there is a change in the price of {item}, \n Here is the link \n\n {url}'

    msg = f'Subject : {subject} \n\n {email_body}'
    server.sendmail(
        'tanveerjan90@gmail.com',
        'tjan90@yahoo.com', msg
    )
    print("Email sent!")
    server.quit()

if(__name__ == '__main__'):
    while(True):
        main()
        time.sleep(86400)

