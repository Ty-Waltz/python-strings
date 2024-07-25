review = "I had a bad experience with this product. It didn't meet my expectations."

def summary(review):
    if len(review) <= 30:
        return review
    else:
        summary_review = review[30]
        if review[30] != " ":
            index = 30
            while index > 0 and review[index] != " ":
                index -= 1
            if index > 0:
                summary_review = review[:index]
                return summary_review + "..."

print(summary(review))
