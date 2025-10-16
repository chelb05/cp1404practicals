"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = load_subjects(FILENAME)
    display_subjects(subjects)


def load_subjects(filename=FILENAME):
    """Read data from file formatted like: subject,lecturer,number of students."""
    subjects = []
    with open(filename) as input_file:
        for line in input_file:
            line = line.strip()
            parts = line.split(',')
            parts[2] = int(parts[2])
            subjects.append(parts)
    return subjects


def display_subjects(subjects): # New function that displays all subject details.
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]} and has {subject[2]} students")


main()
