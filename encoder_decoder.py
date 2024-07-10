import string
import random

def encode(mes):
    words = mes.split()
    nwords = []
    for word in words:
        if(len(word)>=3):
            r1= "".join(random.choices(string.ascii_lowercase, k=3))
            r2= "".join(random.choices(string.ascii_lowercase, k=3))
            stnew = r1 + word[1:] +word[0] +r2
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print("Encoded Value:")
    print(" ".join(nwords))
    program()

        
    
    
def decode(mes):
    words = mes.split()
    nwords = []
    for word in words:
        if(len(word)==6):
            print("Invalid Code")
            program()
        elif(len(word)>=3):
            stnew = word[3:-3]
            stnew = stnew[-1]+stnew[:-1]
            nwords.append(stnew)
        else:
            nwords.append(word[::-1])
    print("Decoded Value:")
    print(" ".join(nwords))
    program()



def program():
    print(" [1]. Encode")
    print(" [2]. Decode")
    choice = int(input("Enter Choice: "))

    match(choice):
        case 1:
            mes = input("Enter the message: ")
            encode(mes)
        case 2:
            mes = input("Enter the message: ")
            decode(mes)
        case _:
            print("Invalid!")
            program()

program()

