import random
def hangman():
    word=random.choice(["yellow","blue","black","code","love","laptop","mouse","drink"])
    validletters='abcdefghijklmnopqrstuvwxyz'
    turns=10
    guessmade = ''
    while len(word)>0:
        main= ""

        for letter in word:
            if letter in guessmade:
                main=main+letter
            else:
                main=main+"_"+""

        if main==word:
            print(main)
            print("you win!")

            break

        print("guess the word : ", main)
        guess=input()



        if guess in validletters:
            guessmade= guessmade+guess
        else:
            guess=input("Enter a valid character ")
        if guess not in word:
            turns=turns-1
            global miss
            miss +=1


            if turns == 9:
                print("9 turns left")
                print("  --------  ")
            if turns == 8:
                print("8 turns left")
                print("  --------  ")
                print("            ")
                print("     O      ")
            if turns == 7:
                print("7 turns left")
                print("  --------  ")
                print("            ")
                print("     O      ")
                print("     |      ")
            if turns == 6:
                print("6 turns left")
                print("  --------  ")
                print("            ")
                print("     O      ")
                print("     |      ")
                print("    /       ")
            if turns == 5:
                print("5 turns left")
                print("  --------  ")
                print("            ")
                print("     O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 4:
                print("4 turns left")
                print("  --------  ")
                print("            ")
                print("   \ O      ")
                print("     |      ")
                print("    / \     ")
            if turns == 3:
                print("3 turns left")
                print("  --------  ")
                print("            ")
                print("   \ O /    ")
                print("     |      ")
                print("    / \     ")
            if turns == 2:
                print("2 turns left")
                print("  --------  ")
                print("         |   ")
                print("   \ O / |  ")
                print("     |      ")
                print("    / \     ")
            if turns == 1:
                print("1 turns left")
                print("Last breaths counting, Take care!")
                print("  --------  ")
                print("         |  ")
                print("  \ O_/__|  ")
                print("    |       ")
                print("   / \      ")
            if turns == 0:
                print("You loose")
                print("You let a kind man die")
                print("  --------  ")
                print("         |  ")
                print("     O___|  ")
                print("    /|\     ")
                print("    / \     ")
                break




miss=0
name=input("Enter your name = ")
print("welcome",name)
print("|---------------------------------------------|")
print("Try to guess the word in less than 10 attempts")
hangman()
print("miss= ",miss)
