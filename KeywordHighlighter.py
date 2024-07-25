reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
def cap_keyword(reviews):
    keyword = "good"
    cap_reviews = []
    for review in reviews:
        if keyword in review:
            review = review.replace(keyword,keyword.upper())
            cap_reviews.append(review)
    return cap_reviews 
def cap_keyword1(reviews):
    keyword = "excellent"
    cap_reviews = []
    for review in reviews:
        if keyword in review:
            review = review.replace(keyword,keyword.upper())
            cap_reviews.append(review)
    return cap_reviews 
     
def cap_keyword2(reviews):
    keyword = "bad"
    cap_reviews = []
    for review in reviews:
        if keyword in review:
            review = review.replace(keyword,keyword.upper())
            cap_reviews.append(review)
    return cap_reviews 
def cap_keyword3(reviews):
    keyword = "quality"
    cap_reviews = []
    for review in reviews:
        if keyword in review:
            review = review.replace(keyword,keyword.upper())
            cap_reviews.append(review)
    return cap_reviews 
def cap_keyword4(reviews):
    keyword = "average"
    cap_reviews = []
    for review in reviews:
        if keyword in review:
            review = review.replace(keyword,keyword.upper())
            cap_reviews.append(review)
    return cap_reviews 
               
     
cap_review = cap_keyword(reviews)
print(cap_review)
cap_review1 = cap_keyword1(reviews)
print(cap_review1)
cap_review2 = cap_keyword2(reviews)
print(cap_review2)
cap_review3 = cap_keyword3(reviews)
print(cap_review3)
cap_review4 = cap_keyword4(reviews)
print(cap_review4)






    
 



    

            
    