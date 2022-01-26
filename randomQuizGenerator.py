#! python
#
# randomQuizGenerator.py
#
# Automate the Boring Stuff Chapter 9: Project
#
# The task is to create a program that does the following:
#
# 1. Creates 35 different quizzes
# 2. Creates 50 multiple-choice questions for each quiz,
#    in random order
# 3. Provides the correct answer and three random wrong answers for 
#    each question, in random order
# 4. Writes the quizzes to 35 text files
# 5. Writes the answer keys to 35 text files
#
# The code will need to do the following:
# 1. Store the U.S. States and their capitals in a dict
# 2. Call open(), write() and close() for the quiz and answer key text files
# 3. Use random.shuffle() to randomize the order of the questions and
#    multiple-choice options

# Imports
import random, os, sys
from pathlib import Path

# These variables should be changed to something sensible for your OS
parent_directory = Path('/home/taladan/programs/mypy/atbs') 
test_directory = Path('quizzes')

# Do not change anything below this line
# Constants
CAPITALS = {'Alabama': 'Montgomery',
'Alaska': 'Juneau',
'Arizona': 'Phoenix',
'Arkansas': 'Little Rock',
'California': 'Sacramento',
'Colorado': 'Denver',
'Connecticut': 'Hartford',
'Delaware': 'Dover',
'Florida': 'Tallahassee',
'Georgia': 'Atlanta',
'Hawaii': 'Honolulu',
'Idaho': 'Boise',
'Illinois': 'Springfield',
'Indiana': 'Indianapolis',
'Iowa': 'Des Moines',
'Kansas': 'Topeka',
'Kentucky': 'Frankfort',
'Louisiana': 'Baton Rouge',
'Maine': 'Augusta',
'Maryland': 'Annapolis',
'Massachusetts': 'Boston',
'Michigan': 'Lansing',
'Minnesota': 'Saint Paul',
'Mississippi': 'Jackson',
'Missouri': 'Jefferson City',
'Montana': 'Helena',
'Nebraska': 'Lincoln',
'Nevada': 'Carson City',
'New Hampshire': 'Concord',
'New Jersey': 'Trenton',
'New Mexico': 'Santa Fe',
'New York': 'Albany',
'North Carolina': 'Raleigh',
'North Dakota': 'Bismarck',
'Ohio': 'Columbus',
'Oklahoma': 'Oklahoma City',
'Oregon': 'Salem',
'Pennsylvania': 'Harrisburg',
'Rhode Island': 'Providence',
'South Carolina': 'Columbia',
'South Dakota': 'Pierre',
'Tennessee': 'Nashville',
'Texas': 'Austin',
'Utah': 'Salt Lake City',
'Vermont': 'Montpelier',
'Virginia': 'Charleston',
'Washington': 'Olympia',
'West Virginia': 'Charleston',
'Wisconsin': 'Madison',
'Wyoming': 'Cheyenne'}
states = list(CAPITALS.keys())

number_of_quizzes = 35
full_path = parent_directory/test_directory
class_name = "Social Studies"
student_date_line = "Name:" + "_" * 20 + "  Date:" + "__/__/__" + " Period:" + "_" * 3 + "\n\n"
header_pad = 40

# If the quizzes directory doesn't exist, make it and navigate to it
if not full_path.exists():
    try:
        os.chdir(parent_directory)
        os.mkdir(test_directory)
        os.chdir(full_path)
    except FileNotFoundError as e:
        print(e)
        sys.exit()
# If the full path exists, navigate to the test directory
else:                              
    os.chdir(full_path)

# Main loop
for quizNum in range(number_of_quizzes):
    # Create headers for each file
    quiz_header = class_name.ljust(header_pad - len(class_name)) + f'Quiz #{quizNum+1}\n\n\n'.rjust(header_pad - quizNum+1)
    quiz_answer_key_header = class_name.ljust(header_pad - len(class_name)) + f'Answer Key for Quiz #{quizNum+1}\n\n\n'.rjust(header_pad - quizNum+1)

    # Create quiz and answer key file
    testnum = quizNum + 1
    current_quiz = open(full_path/f'Capitals-Quiz_Test_{testnum:02d}.txt', 'w')
    current_answer_key = open(full_path/f'Capitals_Quiz_Test_{testnum:02d}_Answer Key.txt', 'w')

    # Write out header for the quiz
    current_quiz.write(quiz_header)
    current_answer_key.write(quiz_answer_key_header)
    current_quiz.write(student_date_line)
    current_quiz.write(' ' * 20 + f'State Capitals Quiz (Form({quizNum+1}))\n\n')

    # Shuffle the order of the states
    random.shuffle(states)

    # Loop through all 50 states, making a question for each
    for questionNum in range(50):
        # Get right and wrong answers
        correctAnswer = CAPITALS[states[questionNum]]
        wrongAnswers = list(CAPITALS.values())
        # Remove right answer from wrongAnswers list so it's not sampled
        del wrongAnswers[wrongAnswers.index(correctAnswer)]

        # Get a sample of 3 'wrong' answers
        wrongAnswers = random.sample(wrongAnswers, 3)

        # Set and shuffle our 4 answer options including the correct answer
        answerOptions = wrongAnswers + [correctAnswer]
        random.shuffle(answerOptions)

        # Write the question and answer options to the quiz file.
        current_quiz.write(f'{questionNum + 1}. What is the capital of {states[questionNum]}?\n')
        for i in range(4):
            '''
            Interesting approach here from ATBS: 'ABCD'[i] where 'ABCD' is treated as a str array and [i] accesses
            the appropriate option within the loop.  Neat!
            '''
            current_quiz.write(f"\t{'ABCD'[i]}. { answerOptions[i]}\n")
        current_quiz.write('\n')
        # Write the answer key to file
        current_answer_key.write(f"{questionNum +1}. {'ABCD'[answerOptions.index(correctAnswer)]}\n")

    # Close the files in prep for the next loop
    current_quiz.close()
    current_answer_key.close()
