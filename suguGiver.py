# Create 3 arrays

questions = ["Python uses indentation to define blocks", "The keyword 'def' is used to define a function in Python", "In Python, lists are immutable (They cannot be changed after creation)", "The print() function is used to display output to the console", "Python variable names can start with a number"]

answers = ["t", "t", "f", "t", "f"]

userAnswers = []

print("Welcome. Read each statement carefully. You must choose either true(t) or false(f)")

#print out questions and save answers in an array

i = 0

while len(userAnswers) < 5:
        answer = ""
        answer = input(questions[i]).lower()   
        while answer != "f" and answer != "t":
                answer = input("You have to type either 't' or 'f'" + questions[i]).lower()   
        i += 1
        userAnswers.append(answer)

#Compare both arrays, select those that differ

incorrectQuestions = []
incorrectAnswers = []

for i in range(len(answers)):
        if answer != userAnswers[i]:
                incorrectAnswers.append(userAnswers[i])
                incorrectQuestions.append(questions[i])
                i += 1

# Print out a response for the user and the incorrect questions/answer if there are any

if len(incorrectAnswers) == 0:
        response = "Congrats! You'got every question right! You've won a Sugu!"
elif len(incorrectAnswers) == 1:
        response = "Sorry! You this question wrong: " + incorrectQuestions[0], incorrectAnswers[0]
elif len(incorrectAnswers) == len(questions):
        response = "You've got every question wrong! Try again!"
else:
        for i in range(len(incorrectQuestions)):
                response = ("Sorry! You've got these questions wrong: " + incorrectQuestions[i] + incorrectAnswers[i])
                

print(response)




