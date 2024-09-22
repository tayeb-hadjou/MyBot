import requests
import json
import nodriver as uc
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as webdriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.firefox.options import Options
import time

url = ""

async def main():
    options = Options() 
    options.add_argument("-headless") 
    driver  = webdriver.Firefox(options=options)
    driver.get(url)
    try:
        search_for_wath_you_want(driver.page_source)
        #driver.quit()
    except Exception as e:
        print(e)
        #driver.quit()

def search_for_wath_you_want(driver):

    soup = BeautifulSoup(driver.page_source, 'html.parser')
    res = ""
    find = soup.find('', class_='')
    if find is not None:
        send_email()
        do_want_you_want(find)

def send_email():
    #use stmplib to send email
    #print("Sending email")
    from_mail = ""
    password = ""
    to_mail = ""
    subject = ""
    body = ""

    message = "Subject: {}\n\n{}".format(subject,body)
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(from_mail,password)
    server.sendmail(from_mail,to_mail,message)
    server.quit()
    #print("Email sent")

def do_want_you_want(find):
    #do what you want to do
    pass

    
if __name__=='__main__':
    uc.loop().run_until_complete(main())
