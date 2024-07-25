reviews = [
        "This product is really good. I'm impressed with its quality.",
        "The performance of this product is excellent. Highly recommended!",
        "I had a bad experience with this product. It didn't meet my expectations.",
        "Poor quality product. Wouldn't recommend it to anyone.",
        "The product was average. Nothing extraordinary about it."
    ]
#def keyword_check(text):
cap_word = []
for word in reviews:
        if word == 'good':
            cap_word.append("GOOD")
        elif word == "excellent":
            cap_word.append("EXCELLENT")
        elif word == "bad":
            cap_word.append("BAD")
        elif word == "Poor":
            cap_word.append("POOR")
        elif word == "average":
            cap_word.append("AVERAGE")
        print(cap_word)





    
 



    

            
    