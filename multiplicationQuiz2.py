#! python
#
# multiplicationQuiz2.py
# 
# Automate the Boring Stuff: Chapter 8 Practice
# Try re-creating the multiplication quiz project
# on your own without importing it.  This program
# will prompt the user with 10 multiplication questions,
# ranging from 0x0 to 9x9.  The following features are required:
# * If the user enters the correct answer, the program displays
#   "Correct!" for 1 second and moves on to the next question.
# * The user gets three tries to enter the correct answer before the
#   program moves on to the next question.
# * Eight seconds after first displaying the question, the question is
#   marked as incorrect even if the user enters the correct answer
#   after the 8-second limit.

# Imports
import pyinputplus as pyip
from random import randint

# CONSTANTS
number_of_questions = 10

# Variables
correct_answers = 0

for q in range(number_of_questions):
    try:
        num1 = randint(0,9)
        num2 = randint(0,9)
        prompt = f"Question #{q + 1}. {num1} x {num2}: "
        pyip.inputNum(prompt, allowRegexes=["^%s$"%(num1 * num2)],
        blockRegexes=[(".*","Incorrect!")],
        timeout=8, limit=3)
    except pyip.TimeoutException:
        print("Sorry, you took too long to answer.")
    except pyip.RetryLimitException:
        print("Sorry, you only get three tries.")
    else:
        print("Correct!")
        correct_answers += 1

print(str(correct_answers) + '/10 answered correctly!')