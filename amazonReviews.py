def getTopReviews(soup):
    
    topReviewsList=list(soup.find_all("div","a-expander-content reviewText review-text-content a-expander-partial-collapse-content"))
    topReviewsList=[element.text.strip().replace(
        "Your browser does not support HTML5 video.",""
    ).strip() for element in topReviewsList]
    
    return topReviewsList

def printTopReviews(soup):
    try:
        reviews=getTopReviews(soup)
    except:
        print("\n\n------------------unable to fetch reviews------------------\n\n")
        return
    total=len(reviews)

    if total == 1:
        aux="is"
    elif total == 0:
        print("\t(No reviews so far!)\n\n")
        return
    else:
        aux="are"

    print("Here {} some Top {} reviews from customers!\n".format(aux,total))
    for i, review in enumerate(reviews,1):
        print(i,review,sep=". ",end="\n\n")

if __name__=="__main__":
    printTopReviews(soup)