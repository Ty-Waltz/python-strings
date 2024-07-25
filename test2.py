sentence = "Hello my name is Ty"
       
my_word = "name"   
def is_my_word_here(sentence, my_word):
    spl_str = sentence.split()
    for word in spl_str:
        if word == my_word:
            return "Yes"
        return"no"
print(is_my_word_here(sentence,my_word))

