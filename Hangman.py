import random
master_list= ["motherboard", "monitor", "cpu", "ram", "keyboard"]
trys=5
word=[]
wrong=False
letters=[]
correct=0
victory=True
win=True
play=True
correctLetters=0
#Game keeps playing until specific number entered
while(play):
    random.shuffle(master_list)
    word=list(master_list[2])
    for i in range (len(word)):
        letters.append("*")
    print(letters)
    while(win):
        guess=input("Guess a letter: ")
        for i in range (len(letters)):
            if guess==word[i]:
                letters[i]=guess
                correctLetters+=1
                print("Trys:",trys)
                print("Correct Letters",correctLetters)
                if correctLetters==(len(word)):
                    win=False
                break
            else:
                wrong=True
            if trys==0:
                win=False
                victory=False
        if wrong:
            trys-=1
            print("Trys:",trys)
        wrong=False
        print(letters)
    print(word)
    play=False
    if (victory):
        print("You win")
    else:
        print("You lose")
'''
Start while loop
    wordNum= random.randint(1,5)
    if wordNum=1:
        word=['m','o','t','h','e','r','b','o','a','r','d']
    elif wordNum=2:
        word=['m','o','n','i','t','o','r']
'''
