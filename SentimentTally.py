positive_words = ["good", "excellent", "great", "awesome", "fantastic", "superb", "amazing"]
negative_words = ["bad", "poor", "terrible", "horrible", "awful", "disappointing", "subpar"]

num_words = [len(words.split()) for words in positive_words]
sum_words = sum(num_words)

num_neg_words = [len(words.split()) for words in negative_words]
sum_neg_words = sum(num_neg_words)
print(f"there are {sum_words} positive words and {sum_neg_words} negative words")

        