words=[]
with open('Collins Scrabble Words (2019).txt','r') as f:
    f.readline()
    f.readline()
    for _ in range(279496):
        word=f.readline()
        if len(word)==6:
            word=word.lower()
            words.append(word)
with open('five_letter_words.txt','w') as f:
    for word in words:
        f.write(f"{word}")