# Create 3 arrays

questions = ["Python uses indentation to define blocks", "The keyword 'def' is used to define a function in Python", "In Python, lists are immutable (They cannot be changed after creation)", "The print() function is used to display output to the console", "Python variable names can start with a number"]

answers = ["t", "t", "f", "t", "f"]

user_answers = []

print("Welcome. Read each statement carefully. You must choose either true(t) or false(f)")

#print out questions and save answers in an array

i = 0

while len(user_answers) < len(answers):
        answer = ""
        answer = input(questions[i]).lower()   
        while answer != "f" and answer != "t":
                answer = input("You have to type either 't' or 'f'. " + questions[i]).lower()   
        i += 1
        user_answers.append(answer)

#Compare both arrays, select those that differ

incorrect_questions = []
incorrect_answers = []

for i in range(len(answers)):
        if answers[i] != user_answers[i]:
                incorrect_answers.append(user_answers[i])
                incorrect_questions.append(questions[i])

# Print out a response for the user and the incorrect questions/answer if there are any

if len(incorrect_answers) == 0:
        response = "Congrats! You've got every question right! You've won a Sugu!"
elif len(incorrect_answers) == 1:
        response = "Sorry! You this question wrong: " + incorrect_questions[0] + " Yo answer: " + incorrect_answers[0]
elif len(incorrect_answers) == len(questions):
        response = "You've got every question wrong! Try again!"
else:
        for i in range(len(incorrect_questions)):
                response = ("Sorry! You've got these questions wrong: "
                + incorrect_questions[i] + incorrect_answers[i])
                

print(response)




