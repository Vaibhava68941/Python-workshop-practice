#Reverse the string order of the words in a sentence and store them in a list

sentence = "Bye bye Deadpool "

words = []
word = ''
for i in sentence:
    if i != ' ':
        word = i + word //adds new character to front of the string 
    else:
        words.append(word)
        word = ''
        
print(words)