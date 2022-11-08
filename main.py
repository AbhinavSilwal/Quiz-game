
start = input("Are You Redy to play(y/n): ")
if start == 'y':
    print("You are welcomed to the quiz")
else:
    print("Bye!")
    exit

print("There are 5 questions and you may try to answer all of it!")
score = int(0)
q_1 = input("What is the capital of USA? ")
if q_1.lower() == "washington dc":
    print("You got your first answer correct!")
    score += 1
else:
     print("Your answer was incorrect :(")

q_2 = input("What is the height of mount everest? ")
if q_2.lower() == "8848m":
    print("You got your answer right!")
    score += 1
else: 
    print("Your answer was incorrect :(")
q_3 = input("Who is called the father of computer? ")
if q_3.lower() == "charls babbage": 
    print("Your answer was correct!")
    score += 1
else : 
    print("Your answer was incorrect")

q_4 = input("Who is the writer of the song'Never gonna give you up'? ")
if q_4.lower() == "rick astley":
    print("Your answer was correct!")
    score += 1
else: 
    print("You are just dumb.")

q_5 = input("Which is the biggest youtube channel? ")
if q_5.lower() == "t series": 
    print("Your answer was correct!")
    score += 1
    print("Your answer was not correct :(")

print("You got " + str(score) + " Qustions correct! ")
end = int(input("Enter any key to close: "))
print(end)
