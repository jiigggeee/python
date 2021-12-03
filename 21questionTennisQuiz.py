# My longest Python project so far.

print("This is the 21 Questions Tennis Quiz!")

play = input("Would you like to play a game? ")
if play.lower() != "yes":
    quit()

print("Nice! Let's crack on!")
score = 0

answer = input("Who won the 1975 Wimbledon Ladies Championship? ")
if answer == "Billie Jean King":
    print("That's correct!")
    score += 1
else:
    print("That's incorrect.")

answer = input("What hairstyle did BJK sport during that tournament? ")
if answer == "Afro":
    print("That's also correct! Good job!")
    score += 1
else:
    print("That's incorrect.")

answer = input("Who is considered one of the most prolific tennis fashion designers in history? ")
if answer == "Teddy Tinling":
    print("That's correct! You're on fire!")
    score += 1
else:
    print("That's incorrect. You cannot be serious with that answer!")

answer = input("Who was the first Brazilian woman to win a grand slam tournament? ")
if answer == "Maria Bueno":
    print("That's correct! Bom!")
    score += 1
else:
    print("That's incorrect. No Bueno.")

answer = input("Where was the U.S. Open originally held? ")
if answer == "Forest Hills":
    print("That's correct! You're on fire!")
    score += 1
else:
    print("That's incorrect.")

answer = input("How many surfaces has the U.S. Open used? ")
if answer == "3":
    print("That's correct! 3 more than the number of Grand Slams Nick Kyrgios has to his hame.")
    score += 1
else:
    print("That's incorrect.")

answer = input("Who was the first aboriginal tennis player to win a Grand Slam? ")
if answer == "Evonne Goolagong":
    print("That's correct! You're on fire!")
    score += 1
else:
    print("That's incorrect...and hint, the Australian Open needs to rename a stadium after her.")

answer = input("After falling on hard times what career did Vic Seixas get into as a senior citizen? ")
if answer == "Bartending":
    print("That's correct! Glug glug, champ!")
    score += 1
else:
    print("That's incorrect.")

answer = input("How did Vitas Gerulaitis die? ")
if answer == "Carbon monoxide poisoning":
    print("That's correct. RIP Vitas.")
    score += 1
else:
    print("That's incorrect.")

answer = input("Who did Nick Kyrgios say he was better than? ")
if answer == "Serena Williams":
    print("That's correct! And he is not.")
    score += 1
else:
    print("That's incorrect...just like him.")

answer = input("Who holds the most Australian Open titles? ")
if answer == "Margaret Court":
    print("Sadly, that's correct.")
    score += 1
else:
    print("That's incorrect.")

answer = input("What is the name of Venus Williams' clothing brand? ")
if answer == "eleVen":
    print("That's correct! Available at Tennis Warehouse online.")
    score += 1
else:
    print("That's incorrect.")

answer = input("Who was the first woman to win all Slams in the same year? ")
if answer == "Maureen Connolly":
    print("That's correct. RIP Little Mo.")
    score += 1
else:
    print("That's incorrect.")

answer = input("What age was she when she won the coveted Grand Slam? ")
if answer == "19":
    print("That's correct! Good for you!")
    score += 1
else:
    print("That's incorrect. Keep going though.")

answer = input("How many Perfect Slams does Margaret Court have to her name? ")
if answer == "3":
    print("That's correct.")
    score += 1
else:
    print("That's incorrect.")

answer = input("Who is the only player to win a Golden Slam? ")
if answer == "Steffi Graf":
    print("That's correct! She won all four in the year plus Olympic Gold!")
    score += 1
else:
    print("That's incorrect.")

answer = input("What is the name of the walk Andre Agassi did during matches? ")
if answer == "Duck Walk":
    print("That's correct! You're on fire!")
    score += 1
else:
    print("That's incorrect.")

answer = input("Billie Jean King beat who during The Battle of the Sexes? ")
if answer == "Bobby Riggs":
    print("That's correct. She beat his ass.")
    score += 1
else:
    print("That's incorrect.")

answer = input("Who was the first trans athlete to compete professionally? ")
if answer == "Renee Richards":
    print("That's correct.")
    score += 1
else:
    print("That's incorrect.")

answer = input("Who outed Billie Jean King? ")
if answer == "Marilyn Barnett":
    print("Correct. Truly sad though. You never out people.")
    score += 1
else:
    print("That's incorrect.")

answer = input("Who won the first Wimbledon Championship? ")
if answer == "Spencer Gore":
    print("That's correct!")
    score += 1
else:
    print("That's incorrect. Sorry.")

print("You got " + str(score) + " questions correct!")
print("You got " + str(score/21 * 100) + " percent.")
