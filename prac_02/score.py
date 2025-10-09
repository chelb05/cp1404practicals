"""
CP1404/CP5632 - Practical
Program to determine score status
"""
import random

def get_score(score):
    score = float(input("Enter score: "))
    print(result(score))

def result(score):
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")
    return result

def main():
    score = random.randint(0, 100)
    result_of_score = result(score)
    print("Random Number: ", score)
    print(result_of_score)

main()