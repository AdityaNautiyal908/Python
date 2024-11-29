questions = (("How many elements are in the periodic table? : "),
           ("Which animal lays the largest eggs? : "),
           ("What is the most abundant gas in Earth's atmosphere?: "),
           ("How many bones are in the human body? : "),
           ("Which planet in the solar system is the hottest? : "))

options = (("A. 116","B. 117","C. 118","D. 119"),
           ("A. Whale","B. Lion","C. Elephant","D. Ostrich"),
           ("A. Oxygen","B. Nitrogen","C. CO2","D. Argon"),
           ("A. 207","B. 300","C. 202","D. 205"),
           ("A. Mars","B. Earth","C. Venus","D. Mercury"))

answers = ("C","D","B","A","C")
guesses = []
score = 0
question_num = 0

for question in questions:
    print("-----------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A,B,C,D): ").upper()
    guesses.append(guess)
    if guess == answers[question_num]:
        score += 1
        print("CORRECT")
    else:
        print("INCORRECT")
        print(f"{answers[question_num]} is the correct answer")
    question_num += 1

print("---------------------------")
print("           RESULTS         ")
print("---------------------------")

print("answers: ",end=" ")
for answer in answers:
    print(answer,end=" ")
print()


print("guesses: ",end=" ")
for guess in guesses:
    print(guess,end=" ")
print()

score = int(score / len(questions) * 100)
print(f"Your score is: {score}%")