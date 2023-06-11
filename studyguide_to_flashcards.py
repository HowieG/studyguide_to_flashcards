import os
import re

def process_questions(filename):
    with open(filename, 'r') as file:
        input_str = file.read()
        
    # Split into sets where a set begins with a question. Questions begin with a line number.
    multiple_choice_sets = re.split(r'(?=\n\d+\.)', input_str)

    output = []
    for multiple_choice_set in multiple_choice_sets:
        # Split into lines. We only care about the question and the answer which are on their own lines
        sections = [s for s in re.split(r'\n', multiple_choice_set) if s.strip()]

        # Beginning of file has non-multiple-choice text that doesn't have a line number so we skip that
        if not sections:
            continue

        # Set begins with question
        question = sections[0]

        # Answer begins with "Ans:". E.g. Ans: C
        answer_key = re.findall(r'Ans:\s+ (\w)', multiple_choice_set)
        if not answer_key:
            continue

        answer_key = answer_key[0]

        # Use the Ans key e.g. "C" to look up the actual answer text from the multiple choice options e.g. "C) deceleration"
        answer = re.findall(r'{0}\)    (.*)'.format(answer_key), multiple_choice_set)
        if not answer:
            continue

        answer = answer[0]

        # Output question and answer on their own lines
        output.append(question + '\n\n' + answer + '\n\n\n')

    return '\n'.join(output)


# Change working directory to script location
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# Input files are in inputs/ directory
input_files = os.listdir('inputs')

for file in input_files:
    if file.endswith('.txt'):
        print(f"Processing file: {file}")
        output_str = process_questions(os.path.join('inputs', file))
        
        # Open a new file in the 'outputs' directory with the same name, and write the output
        with open(os.path.join('outputs', file), 'w') as output_file:
            output_file.write(output_str)
            

#Input: txt files in an inputs/ directory on the same level as this script
#Output: txt files in an outputs/ directory on the same level as this script

# Sample:

# Chapter: Ch 29 - Trauma Systems and Mechanism of Injury

# Multiple Choice

# 1.    The acute physiologic and structural change that occurs in a patient's body when an external source of energy dissipates faster than the body's ability to sustain and dissipate it is called:
# A)    injury.
# B)    trauma.
# C)    deceleration.
# D)    kinematics.

# Ans:    B
# Page:    1483
# Type:    General Knowledge


# 2.    The energy stored in an object, such as a bridge pillar, is called __________ energy, and the energy from motion is called __________ energy.
# A)    kinetic, potential
# B)    barometric, kinetic
# C)    potential, kinetic
# D)    chemical, potential

# Ans:    C
# Page:    1484
# Type:    General Knowledge