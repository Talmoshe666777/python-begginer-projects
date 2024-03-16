print("Welcome to my computer quiz!")
playing = input("Do you want to play? ")
questions = ["What does CPU stand for? ", "What does GPU stand for? ", "What does RAM stand for? ", "What does PSU stand for? "]
answers = ["central processing unit", "graphics processing unit", "random access memory", "power supply"]
correct_answers = 0
incorrect_answers = 0

if playing != "yes":
    quit()

print("OK! Lest's play")

for idx, q in enumerate(questions):
    answer = input(q)

    if answer.lower() == answers[idx]:
        print("Correct!")
        correct_answers += 1
    else:
        print("Incorrect!")
        incorrect_answers += 1

print("You have "+str(correct_answers)+" correct answers and "+str(incorrect_answers)+" incorrect answers")

if correct_answers > incorrect_answers:
    print("Well Done!")
elif correct_answers == incorrect_answers:
    print("Not good, but not that bad")
else:
    print("Better luck next time :(")
# answer = input("What does CPU stand for? ")
#
# if answer.lower() == "central processing unit":
#     print("Correct!")
# else:
#     print("Incorrect!")

