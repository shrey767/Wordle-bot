words=set()
with open('five_letter_words.txt','r') as f:
    for line in f:
        word=line.strip()
        words.add(word)
print(len(words))
fwords=set()
for word in words:
    if(len(word)==5):
        fwords.add(word)
guess=input("Guess: ")
guess=guess.lower()
for _ in range(6):
    inp=input("Match: ")
    if(inp=="ggggg"):
        print(f"Congrats you did it in {_ + 1} guesses\nThank you for using wordle-bot!")
        break
    while len(inp)!=5:
        print("Incorrect Match, try again")
        inp=input("Match: ")
    inp=inp.lower()
    newwords=set()
    cnfed=set()
    for word in fwords:
        if ord(word[0])<97:
            continue
        flags=[0]*5
        for i in range(5):
            if(inp[i]=="y"):
                for j in range(5):
                    if(word[j]==guess[i] and i!=j):
                        flags[i]=1
                    elif(word[j]==guess[i] and i==j):
                        flags[i]=0
                        break
                cnfed.add(guess[i])
            elif(inp[i]=="g"):
                cnfed.add(guess[i])
                if(word[i]==guess[i]):
                    flags[i]=1
            else:
                if guess[i] in cnfed:
                    flags[i]=1
                    continue
                flags[i]=1
                for j in range(5):
                    if(word[j]==guess[i]):
                        flags[i]=0
                        break
        if flags==[1,1,1,1,1]:
            newwords.add(word)
    freq=[0]*30
    freqtuple=[]
    for word in newwords:
        for letter in word:
            if letter not in cnfed:
                freq[ord(letter)-97]+=1
    for word in newwords:
        score = sum(freq[ord(ch) - 97] for ch in set(word))
        freqtuple.append((word,score))
    freqtuple=sorted(freqtuple,key=lambda x: x[1])
    print(len(freqtuple), " words left")
    if(len(freqtuple)>8):
        print("BEST CHOICES: ")
        for k in range(3*len(freqtuple)//4 -  2, 3*len(freqtuple)//4 +3):
            print(freqtuple[k][0],end=" ")
        print()
    else:
        if(len(freqtuple)==0):
            print(fwords)
        print("BEST CHOICES")
        print(*freqtuple)
    guess=input("Guess: ")
    while guess not in words:
        if guess not in words:
            print("Not in wordlist, try again: ")
            guess=input("Guess: ")
    guess=guess.lower()
    fwords=newwords
