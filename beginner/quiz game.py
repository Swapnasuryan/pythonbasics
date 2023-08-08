def new_game():

    guesses = []
    correct_guesses = 0
    Question_num = 1

    for key in Questions:
        print("_________________")
        print(key)
        for i in options[Question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(Questions.get(key), guess)
        Question_num += 1
    display_score(correct_guesses, guess)

#___________________________________________________________
def check_answer(answer, guess):

    if answer == guess:
        print("correct!")
        return 1
    else:
        print("wrong!")
        return 0
#_______________________________________________________________
def display_score(correct_guesses, guesses):
    print("___________________________")
    print("Results")
    print("______________________________")
    print("Answers: ", end=" ")
    for i in Questions:
        print(Questions.get(i), end=" ")
    print()

    print("gussess: ", end=" ")
    for i in guesses:
        print(i,end=" ")
    print()

    score = int(correct_guesses/len(Questions)*100)
    print("your score is "+str(score)+"%")
#__________________________________________________________________
def play_again():
    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False

#_______________________________________________________________

Questions = {
    "who created Python?:": "A",
    "what year was Python created?:": "B",
    "Python is tributed to which comedy group?:": "C",
    "Is the Earth round?:": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zukerberg"],
           ["A. 1989", "B.1991", "C. 2000", "D. 2016"],
           ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
           ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]

new_game()

while play_again():
    new_game()

print("Byeee!")