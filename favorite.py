import random

def main():

    favourite = ["dogs", "cats","bats"]  # change this
    p = random.random()
    if p < .8:
        print("I love " + favourite[0]) 
    elif p < .9:
        print("I love " + favourite[1]) 
    else:
        print("I love " + favourite[2])
    


main()