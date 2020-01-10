#! C:\Users\Admin\AppData\Local\Programs\Python\Python38\python.exe

print('Content-Type: text/html')
print('')

import cgi
import random

#Can treat this like a dictionary

#Check that the GET variable exists before trying to use it
#if "name" in form:
#    print(form.getvalue("name"))
#else:
#    print("No name")

form = cgi.FieldStorage()

reds = 0
whites = 0

if 'answer' in form:
    answer = form.getvalue('answer')
else:
    answer = ''
    for i in range(0, 4):
        char = str(random.randint(0, 9))
        answer += char

if 'guess' in form:
    guess = form.getvalue('guess')
    for key, digit in enumerate(guess):
        if digit == answer[key]:
            reds += 1
        else:
            for answerDigit in answer:
                if answerDigit == digit:
                    whites += 1
                    break


else:
    guess = ''

if 'numberOfGuesses' in form:
    numberOfGuesses = int(form.getvalue('numberOfGuesses')) + 1
else:
    numberOfGuesses = 0

if numberOfGuesses == 0:
    message = "I've chosen a 4-digit number. Can you guess it?"
elif reds == 4:
    message = "Congratulations! You got in right in " + str(numberOfGuesses) + " guess(es) <a href=''>Play Again</a>"
else:
    message = "You have " + str(reds) + " correct digit(s) in the right place and " + str(whites) + " in the wrong place. You have had " + str(numberOfGuesses) + " guess(es)"

print("<h1>Mastermind</h1>")
print("<p>" + message + "</p>")
print('<form method="post">')
print('<input type="text/html" name="guess" value="' + guess + '">')
print('<input type="hidden" name="answer" value="' + answer + '">')
print('<input type="hidden" name="numberOfGuesses" value="' + str(numberOfGuesses) + '">')
print('<input type="submit" name="Guess">')
print('</form>')

print(answer)
#print("<h2>Number of Reds: " + str(reds) + "</h2>")
#print("<h2>Number of Whites: " + str(whites) + "</h2>")
#print(form.keys())

print("<h1>" + guess + "</h1>")
#print('<a href="/python_practice/python_server/mastermind.html">Back to Form</a>')
