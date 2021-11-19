import random
random_number = (random.randint(1,10))
insert_number = int(input("Guess the number generated: \n"))

if insert_number == random_number:
        print ("Correct Guess !!!") 

else:
    difference_number = random_number - insert_number
    print ("Differnce between generated and random number: " + str(difference_number))

    if random_number > insert_number:
        print ("Number too SMALL!")
    else:
        print ("Number too BIG!")

play_again = input("Play again? [y/n]\n")

while play_again != "n":
    if play_again == "y":
        random_number = (random.randint(1,10))
        insert_number = int(input("Guess the number generated: \n"))

        if insert_number == random_number:
            print ("Correct Guess !!!") 
            play_again = input("Play again? [y/n]\n")

        else:
            difference_number = random_number - insert_number
            print ("Differnce between generated and random number: " + str(difference_number))

            if random_number > insert_number:
                print ("Number too SMALL!")
            else:
                print ("Number too BIG!")
            play_again = input("Play again? [y/n]\n")
else:
    print ("GAME ENDED!!!")