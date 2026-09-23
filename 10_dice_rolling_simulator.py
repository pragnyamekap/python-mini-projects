import random

print("--- DICE ROLLING SIMULATOR ---")

total_score = 0
round_number = 1

play = "yes"

while play == "yes":
    print("\n--- Round", round_number, "---")
    
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    
    print("Dice 1:", dice1)
    print("Dice 2:", dice2)
    
    round_total = dice1 + dice2
    print("Round total:", round_total)
    
    if dice1 == dice2:
        print("Double! You get 10 bonus points!")
        round_total = round_total + 10
    
    total_score = total_score + round_total
    print("Your total score so far:", total_score)
    
    round_number = round_number + 1
    
    play = input("\nRoll again? (yes/no): ")
    play = play.lower()

print("\n--- GAME OVER ---")
print("You played", round_number - 1, "rounds")
print("Your final score is:", total_score)

if total_score >= 50:
    print("Amazing! You're a dice master!")
elif total_score >= 25:
    print("Good job!")
else:
    print("Better luck next time!")