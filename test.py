reviews = "This product is really good Im impressed with its quality",
"The performance of this product is excellent. Highly recommended!",
"I had a bad experience with this product. It didn't meet my expectations.",
"Poor quality product. Wouldn't recommend it to anyone.",
"The product was average. Nothing extraordinary about it."
    


def is_word_present(sentence, word):
    s = sentence.split(" ")
    for i in s:
        if (i==word):
            return True
        return False
s = "This product is really good. I'm impressed with its quality."
word = "good"
if (is_word_present(s,word)):
    print("Yes")
else:
    print("No")