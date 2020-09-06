import os,time
os.system('cls')
filenames = ["quizquest.txt","questquiz.txt"]
frames = []

for name in filenames:
    with open(name,"r",encoding="utf8") as f:
        frames.append(f.readlines())
for i in range (3):
    for frame in frames:
        print("".join(frame))
        time.sleep(1)
        os.system('cls')
print("                                                                    by: MunzeyDev")

print("""1. The apple quiz
2. The english quiz
3. (COMING SOON)""")

print("")
choice = input("Choose a level: ")
print("")
if choice == "1":
    print("""Question A. Who is the founder of the company Apple?
1. Toby Maguire
2. Tom Hanks
3. Steve Jobs
4. John Appleseed""")
    print("Type the number of your choice!")
    var1 = input("Your Answer: ")
    if var1 == "3":
        print("CORRECT!")
    else:
        print("try again")
        var1 = input("Question A. What is your Answer?: ")
        if var1 == "3":
            print("CORRECT!")
    print("")
    print("""Question B. What is the first thing Apple released?:
1. Powerbook G4
2. IBook
3. First-gen Ipod
4. Apple I""")
    print("Type the number of your choice!")
    var2 = input("Your answer: ")
    if var2 == "4":
        print("CORRECT!")
    else:
        print("try again")
        var2 = input("Question B. What is your Answer?: ")
        if var2 == "4":
            print("CORRECT!")
    print("")
    var3 = input("Question C. What is your name?: ")

    print("")
    print("Hey " + var3 + " you did pretty good. Thank you for playing my game, you can run it again to play a different level, also stay tuned for upcoming levels!")

if choice == "2":
    print("""Question A. What is a synonym for situation?
1. location
2. position
3. absence
4. intermission""")
    print("Type the number of your choice!")
    var4 = input("Your Answer: ")
    if var4 == "2":
        print("CORRECT!")
    else:
        print("try again")
        var4 = input("Question A. What is your Answer?: ")
        if var4 == "2":
            print("CORRECT!")
    print("")
    print("""Question B. Fill in the blank, The old man needed ____ to cross the street.
1. assist
2. time
3. the cars to stop
4. speed""")
    print("Type the number of your choice!")
    var5 = input("Your answer: ")
    if var5 == "1":
        print("CORRECT!")
    else:
        print("try again")
        var5 = input("Question B. What is your Answer?: ")
        if var5 == "1":
            print("CORRECT!")
    print("")
    var3 = input("Question C. What is your name?: ")

    print("")
    print("Good Job " + var3 + "! Thank you for playing my game, you can run it again to play a different level, also stay tuned for upcoming levels!")
