import random

choices = ["r", "p", "s"]

pc = random.choice(choices)

choose = input("Choose Rock, Paper or Scissors!(r, p, s): ")

if choose == pc:
    print("Tie!")

if choose == "r" and pc == "p":
    print(f"You lost to {pc} with {choose}!")

if choose == "r" and pc == "s":
    print(f"You won to {pc} with {choose}!")

if choose == "p" and pc == "r":
    print(f"You won to {pc} with {choose}!")

if choose == "p" and pc == "s":
    print(f"You lost to {pc} with {choose}!")

if choose == "s" and pc == "p":
    print(f"You won to {pc} with {choose}!")

if choose == "s" and pc == "r":
    print(f"You lost to {pc} with {choose}!")