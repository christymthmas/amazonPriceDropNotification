def getProductTitle(soup):
    title = soup.find("span", id = "productTitle").text.strip()
    return title

def getBrandName(soup):
    brandName = soup.find("a", id = "bylineInfo").text.strip().replace("Visit the ","").replace("Brand: ","").replace(" Store","")
    return brandName

def getMRP(soup):
    mrpstr = soup.find("span", class_ = "priceBlockStrikePriceString a-text-strike").text.strip().replace("₹","").replace(",","")
    mrp=round(float(mrpstr))
    return mrp

def getamzPrice(soup):
    try:
        amzPriceStr = soup.find_all("td", class_ ="a-span12")[1].text.strip().replace("₹","").replace(",","")
    except:
        try:
            amzPriceStr = soup.find("span", id="priceblock_dealprice").text.strip().replace("₹","").replace(",","")
        except:
            amzPriceStr = soup.find("span", id="priceblock_ourprice").text.strip().replace("₹","").replace(",","")

    
    amzPrice=round(float(amzPriceStr))
    return amzPrice

def getYouSave(soup):
    youSaveStr = soup.find("td", class_ ="a-span12 a-color-price a-size-base priceBlockSavingsString").text.strip().replace("₹","").replace(",","")
    youSavePercentageStr=youSaveStr[-5:]
    youSavePercentage=int(youSavePercentageStr.strip(")%").strip().replace("(", ""))
    youSave=round(float(youSaveStr[:-5].strip()))
    return youSave, youSavePercentage

def getAvailability(soup):
    avail = soup.find("div", id="availability").text.strip()
    if avail == "In stock.":
        return True
    else:
        return False

def printDetails(soup):
    try:
        productTitle = getProductTitle(soup) # title of the product
        brandName = getBrandName(soup) # name of the Brand
        mrp = getMRP(soup) # mrp
        amazonPrice = getamzPrice(soup) # current price on Amazon
        youSave, youSavePercentage = getYouSave(soup) # the saved money and percentage of saved
    except:
        try:
            productTitle = getProductTitle(soup)
            brandName = getBrandName(soup)
            amazonPrice = getamzPrice(soup)
            print("""
----------------------------------------------------------------------------------------

    Product\t\t:\t{}
    Brand Name\t\t:\t{}
    Amazon Price\t:\t₹ {:,}

----------------------------------------------------------------------------------------""".format(productTitle,brandName,amazonPrice))
            return True
        except:
            try:
                productTitle = getProductTitle(soup)
                brandName = getBrandName(soup)
                print("""
----------------------------------------------------------------------------------------

    Product\t\t:\t{}
    Brand Name\t\t:\t{}
    
        (Unable to fetch the price details)
----------------------------------------------------------------------------------------""".format(productTitle,brandName))
                return False
            except:
                print("\n\n------------------unable to fetch the product details------------------\n\n")
                return False

            
    
    if getAvailability(soup):
        availability="This product is currently in Stock!"
    else:
        availability="This product is currently NOT in Stock!"


    print("""
----------------------------------------------------------------------------------------

    Product\t\t:\t{}
    Brand Name\t\t:\t{}
    Amazon Price\t:\t₹ {:,}
    MRP\t\t\t:\t₹ {:,}
    \tYou'll save ₹ {:,} ({}%)

    {}
    
----------------------------------------------------------------------------------------
""".format(productTitle,brandName,amazonPrice,mrp,youSave,youSavePercentage,availability))
    return 




