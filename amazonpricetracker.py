import requests 
from bs4 import BeautifulSoup 
import smtplib
import time

URL = 'https://www.amazon.com/LG-UltraFine-International-Certified-Refurbished/dp/B07D24BQBQ/ref=sr_1_3?keywords=lg+macbook+pro+display&qid=1563419236&s=gateway&sr=8-3'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.100 Safari/537.36'}

def check_price():
    page = requests.get(URL, headers = headers) #get the data from the webpage
    soup1 = BeautifulSoup(page.content, 'html.parser') #get the html code made with javascript
    soup2 = BeautifulSoup(soup1.prettify(), "html.parser")  #convert to proper format 

    title = soup2.find(id="productTitle").get_text()   #grab the product title 
    price=soup2.find(id="priceblock_ourprice").get_text()
    converted_price = price[0:5]

    if(converted_price < 1000):
        send_email()

    print(price)
    print(title.strip())
    #print(soup.prettify)

def send_email():
    server = smtplib.SMTP('smtp.google.com',)
    server.ehlo()       #command to connect to email servers
    server.starttls()    #encrypt our connection 
    server.ehlo()

    server.login('bluespoose@gmail.com', 'vxnfnjkizrotbgom')

    subject = 'Price fell down!'  #subject of email
    body = 'Check the following amazon link' + URL
    msg = "Subject: {subject}\n\n{body}"
    server.sendmail('bluespoose@gmail.com' , 'armankhondsker@gmail.com', msg) #send email from bluespoose to my official gmail
    server.quit()
    print("Email has been sent")


check_price()

# while(True):
#     time.sleep(60 * 60)

