def getRatings(soup):

    # total rating
    rating=soup.find("div", class_="a-row a-spacing-medium averageStarRatingNumerical")
    totalRating=int(rating.text.strip(" global ratings").strip().replace(",",""))

    #return total number of ratings as an integer
    return totalRating

def getStarPercentage(soup):
    starTable=soup.find("table",class_="a-normal a-align-center a-spacing-base").text.strip().replace("0% (0%)","")
    
    
    from re import findall
    starsPer=findall('\d+',starTable)
    
    del starsPer[0::2] #deleting elements in the odd positions

    starsPer = list(map(int,starsPer)) #appliying int function to all elements in list

    # for i,star in enumerate(starTable):
    #     replaceText= "{} star".format(5-i)
    #     try:
    #         starsPer.append(int(star.text.replace(replaceText,"").strip().replace("%","")))
    #     except:
    #         starsPer.append(0)
        

    #returns 5-1 star percentages as a list
    # return starTable
    return starsPer

def getOutOfFiveRating(soup):
    averageRating=soup.find("span", class_="a-size-medium a-color-base").text
    averageRatingValue=float(averageRating.replace(" out of 5",""))
    return averageRatingValue

def printRating(soup):
    try:
        totalRating=getRatings(soup) # int
        starsPer = getStarPercentage(soup) #list
        outOfFive = getOutOfFiveRating(soup) #float
    except:
        print("\n\n------------------unable to fetch the rating------------------\n\n")
        return
    fiveStar = starsPer[0]
    fourStar = starsPer[1]
    threeStar = starsPer[2]
    twoStar = starsPer[3]
    oneStar = starsPer[4]


    print("""
    \t{} out of 5 stars

    Total No of ratings : {}\n
    Five Stars\t:\t{:2} %
    Four Stars\t:\t{:2} %
    Three Stars\t:\t{:2} %
    Two Stars\t:\t{:2} %
    One Stars\t:\t{:2} %

----------------------------------------------------------------------------------------

    """.format(outOfFive,totalRating,fiveStar,fourStar,threeStar,twoStar,oneStar))

if __name__=="__main__":
    import requests
    from bs4 import BeautifulSoup

    headers = {"User-Agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.115 Safari/537.36"}

    url = input("Paste the Amazon URL of the product :")
    #url = "https://www.amazon.in/COTTON-SHOPY-Womens-Embroidered-Kanjivaram/dp/B08H11HVMH/ref=pd_sbs_2/261-0957789-8344412?pd_rd_w=iNuYF&pf_rd_p=950901b9-b71e-4c33-9fc5-41ec6db58ad1&pf_rd_r=P42KRHGY79GQTVKSRV0Y&pd_rd_r=0ffff1db-ea9e-4c9a-9472-7f18bbd1a07a&pd_rd_wg=2QCAF&pd_rd_i=B08H11FBV1&th=1"
    resp = requests.get(url, headers=headers)

    soup=BeautifulSoup(resp.content,"lxml")

    totalRating=getRatings(soup) # int
    starsPer = getStarPercentage(soup) #list
    outOfFive = getOutOfFiveRating(soup) #float

    # fiveStar = starsPer[0]
    # fourStar = starsPer[1]
    # threeStar = starsPer[2]
    # twoStar = starsPer[3]
    # oneStar = starsPer[4]

    print(starsPer)
    







