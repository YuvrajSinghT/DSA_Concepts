import random
a=random.randint(1,10)
your_guess=None

while(your_guess!=a):
        your_guess=int(input("computer guessed a number \n\t try to guess that\n"))

        if(your_guess>a):
            print("try a lower number")
        elif(your_guess<a):
            print("try a lower number")
        else:
            print("You WOn")
            break


#game(a,your_guess)