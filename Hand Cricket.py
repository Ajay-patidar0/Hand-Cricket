import random

print("WELCOME TO THE HAND CRICKET WORLD")
print("HUMAN VS PC")
print()
print("Rules:")
print("1.You have to enter a number upto 6 but not 5 you will get runs accordingly while batting and computer will choose a random value.")
print("2.If your choice and computer's choice is same, you will be out and vice versa.")
print("3.There will be toss. If you win you can choose between batting and bowling. But if computer wins it will not be your choice to bat or ball first.")
print("4.The one who scores more will be the WINNER")
print()
# Start

choice = int(input("Press 1 to start"))
name = input("Enter your name: ")
if choice == 1:
    #Toss
    print()
    print("Are you excited for today's match.\nIt's gona be interesting.\nNow it's time for the toss")
    Toss = int(input("The coin is in the air! \nPress 1 for Head and 0 for Tails:"))
    t = random.randrange(0, 2, 1)
    if Toss == t:
        print("It's his choice on the coin. \n                  Captain {} won the toss. What you want to choose?".format(name))
        BAT_BOWL = int(input("Press 1 for bat and 0 for bowl"))
        # BAT_BOWL
        if BAT_BOWL == 1:
            print("The batsman is ready for the show. \nIt will be an interesting one.")
            print()
            print("It's the first ball.")
            score = 0
            while (True):
                Run = int(input("What you want to score? Enter your choice (1,2,3,4,6):"))
                Ball = random.randrange(1, 7, 1)
                if Run != Ball:
                    if (Run == 4):
                        print("A smooth shot to the boundary and it's a 4!")
                        score += 4
                    elif (Run == 6):
                        print("The ball is in the air......\nOh! and It's an amazing 6!!")
                        score += 6
                    elif (Run in [1, 2, 3]):
                        print("Good running between the wickets. {} added".format(Run))
                        score = score + Run
                    else:
                        print("Choose your runs correctly")
                        print("Sorry Match Stopped here due to an invalid entry")
                        print("Your Total Score: ", score)
                        break

                else:
                    print("What a clean wicket!!. {} Departs".format(name))
                    print("Your Total Score: ", score)
                    print()
                    print()
                    print("2ND INNINGS...Computer comes to bat and the opponent {} ready with the ball".format(name))
                    chase = 0
                    c_bat = random.randrange(1, 7, 1)
                    c_bowl = int(input("Enter your value to ball."))
                    if c_bat != c_bowl:
                        if (c_bat == 4):
                            print("It's a Boundary----4 runs!")
                            score += 4
                        elif (c_bat == 6):
                            print("What a Huge 6!")
                            score += 6
                        elif (c_bat in [1, 2, 3]):
                            print("More runs added to the score. {} added".format(Run))
                            score = score + Run
                        else:
                            print("Choose your runs correctly")
                            print("Sorry Match Stopped here due to an invalid entry")
                            print("Your Total Score: ", chase)
                            break
                    else:
                        print("This is what the bowling team needed.....A wicket!")
                        print("Computer's Total Score: ", chase)
                        print("The match ends here.")
                    print()
                    if score > chase:
                        print("Congratulation!!!\nYou won the match. It was just an amazing match.")
                        break
                    elif score == chase:
                        print("Oh My God!\n Unbelievable!!\nIt's a tie.")
                        break
                    else:
                        print("Oh! {} Lost.But played well".format(name))
                        print("Computer made it. Taken away the trophy from one of the toughest player.")
                        break
        if BAT_BOWL == 0:
            print()
            print("It's the first ball.")
            score = 0
            while (True):
                Run = int(input("What you want to score? Enter your choice (1,2,3,4,6):"))
                Ball = random.randrange(1, 7, 1)
                if Run != Ball:
                    if (Run == 4):
                        print("Amazing shot to the boundary....4 runs!")
                        score += 4
                    elif (Run == 6):
                        print("He is in aggressive mode\nIt's a Unbelievable 6!")
                        score += 6
                    elif (Run in [1, 2, 3]):
                        print(
                            "It seems easy to make runs\n How smoothly they are running between the wickets!. {} added".format(
                                Run))
                        score = score + Run
                    else:
                        print("Choose your runs correctly")
                        print("Sorry Match Stopped here due to an invalid entry")
                        break

                    if Run == Ball:
                        print("Its a clean OUT. {} Departs".format(name))
                        print("Your Total Score: ", score)
                        print()
                        print()
                        print(
                            "2ND INNINGS...Computer comes to bat and the opponent {} ready with the ball".format(name))
                        chase = 0
                        c_bat = random.randrange(1, 7, 1)
                        c_bowl = int(input("Enter your value to ball."))
                        if c_bat != c_bowl:
                            if (c_bat == 4):
                                print("A smooth shot to the boundary and it's a 4!")
                                score += 4
                            elif (c_bat == 6):
                                print("The ball is in the air......\nOh! and It's an amazing 6!")
                                score += 6
                            elif (c_bat in [1, 2, 3]):
                                print("More runs added to the score. {} added".format(Run))
                                score = score + Run
                            else:
                                print("Choose your value correctly")
                                print("Sorry Match Stopped here due to an invalid entry")
                                print("Your Total Score: ", chase)
                                break
                        else:
                            print("Its a wicket")
                            print("Computer's Total Score: ", chase)
                            print("The match ends here.")
                        print()
                        if score > chase:
                            print("Congratulation!!!\n You won the match. It was just an amazing match.")
                            print("{} lifts the trophy".format(name))
                            break
                        elif score == chase:
                            print("Oh My God!\n Unbelievable!!\nIt's a tie.")
                            break
                        else:
                            print("Oh! {} Lost.But played well".format(name))
                            print("Computer made it. Taken away the trophy from one of the toughest player.")
                            break




    else:
        print("Computer won the Toss. He Choosed to Bowl First.")
        print("The batsman seems to be in confident today")
        print()
        print("It's the first ball.")
        score = 0
        while (True):
            Run = int(input("What you want to score? Enter your choice (1,2,3,4,6):"))
            Ball = random.randrange(1, 7, 1)
            if Run != Ball:
                if (Run == 4):
                    print("Amazing shot to the boundary....4 runs!")
                    score += 4
                elif (Run == 6):
                    print("He is in aggressive mode\nIt's a Unbelievable 6!")
                    score += 6
                elif (Run in [1, 2, 3]):
                    print("It seems easy to make runs\n How smoothly they are running between the wickets!. {} added".format(Run))
                    score = score + Run
                else:
                    print("Choose your runs correctly")
                    print("Sorry Match Stopped here due to an invalid entry")
                    break

                if Run == Ball:
                    print("Its a clean OUT. {} Departs".format(name))
                    print("Your Total Score: ", score)
                    print()
                    print()
                    print("2ND INNINGS...Computer comes to bat and the opponent {} ready with the ball".format(name))
                    chase = 0
                    c_bat = random.randrange(1, 7, 1)
                    c_bowl = int(input("Enter your value to ball."))
                    if c_bat != c_bowl:
                        if (c_bat == 4):
                            print("A smooth shot to the boundary and it's a 4!")
                            score += 4
                        elif (c_bat == 6):
                            print("The ball is in the air......\nOh! and It's an amazing 6!")
                            score += 6
                        elif c_bat in [1, 2, 3]:
                            print("More runs added to the score. {} added".format(Run))
                            score = score + Run
                        else:
                            print("Choose your value correctly")
                            print("Sorry Match Stopped here due to an invalid entry")
                            print("Your Total Score: ", chase)
                            break
                    else:
                        print("Its a wicket")
                        print("Computer's Total Score: ", chase)
                        print("The match ends here.")
                    print()
                    if score > chase:
                        print("Congratulation!!!\nYou won the match. It was just an amazing match.")
                        print("{} lifts the trophy".format(name))
                        break
                    elif score == chase:
                        print("Oh My God!\n Unbelievable!!\nIt's a tie.")
                        break
                    else:
                        print("Oh! {} Lost.But played well".format(name))
                        print("Computer made it. Taken away the trophy from one of the toughest player.")
                        break

else:
    print("Please enter a valid input.".format(name))