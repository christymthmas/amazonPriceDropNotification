import requests
from bs4 import BeautifulSoup
from random import randint
from time import sleep


import amazonDetails as details
from  mailAlert import mailing


def condition(DESIRED_PRICE,url,headers,fromaddr,password,toaddr,yourname):

    while True:
        while True:
            try:
                resp = requests.get(url, headers=headers)
                soup=BeautifulSoup(resp.content,"lxml")
                break
            except:
                sleep(randint(10,20))
                pass
                    
        productTitle = details.getProductTitle(soup)
        brand = details.getBrandName(soup)
        try:
            amazonPrice = details.getamzPrice(soup)
            youSave, youSavePercentage = details.getYouSave(soup)
        except:
            youSave, youSavePercentage = (-1,-1)
            try:
                amazonPrice = details.getamzPrice(soup)
               
            except:
                amazonPrice = -1
                
        if amazonPrice == -1:
            print("\n\nUnable to find the price information!")
            sleep(2)
            print("\n----------------------aborting the excecution----------------------\n\n")
            break
        else:
            if DESIRED_PRICE >= amazonPrice:
                return mailing(brand,DESIRED_PRICE,url,fromaddr, password, toaddr, yourname,productTitle, amazonPrice, youSave,youSavePercentage)
                sleep(5)
                break
        print("\n\nYou'll be notified when price falls via email!\n(NB: To get notified, don't terminate this session)\n")
        
        sleep(randint(600,900))
        


        
        
        
