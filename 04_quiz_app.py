score = 0

print("--- SIMPLE QUIZ APP ---")

user_answer = input("Q1. What is the capital of India? ")
if user_answer.lower() == "delhi":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The answer is Delhi.")

user_answer = input("Q2. What is 5 + 3? ")
if user_answer == "8":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The answer is 8.")

user_answer = input("Q3. Which language are you learning right now? ")
if user_answer.lower() == "python":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The answer is Python.")

user_answer = input("Q4. How many continents are there? ")
if user_answer == "7":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The answer is 7.")

user_answer = input("Q5. What is the largest planet in our solar system? ")
if user_answer.lower() == "jupiter":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The answer is Jupiter.")

user_answer = input("Q6. What is 10 x 10? ")
if user_answer == "100":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The answer is 100.")

user_answer = input("Q7. What is the national animal of India? ")
if user_answer.lower() == "tiger":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The answer is Tiger.")

user_answer = input("Q8. Which is the smallest prime number? ")
if user_answer == "2":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The answer is 2.")

user_answer = input("Q9. What is the color of the sky on a clear day? ")
if user_answer.lower() == "blue":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The answer is Blue.")

user_answer = input("Q10. How many days are there in a week? ")
if user_answer == "7":
    print("Correct!")
    score = score + 1
else:
    print("Wrong! The answer is 7.")

print("\n--- QUIZ OVER ---")
print("Your score is:", score, "out of 10")

if score == 10:
    print("Perfect score! Amazing!")
elif score >= 7:
    print("Great job!")
elif score >= 4:
    print("Not bad, keep practicing!")
else:
    print("Better luck next time!")