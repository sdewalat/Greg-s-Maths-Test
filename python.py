import time
import random

def main():
    print("Welcome to Greg's Maths Test!")
    print("Select a difficulty:")
    print("1) Easy")
    print("2) Medium")
    print("3) Hard")

    # --- Difficulty selection ---
    while True:
        choice = input("> ").strip()   # Read user input
        if choice not in ["1", "2", "3"]:
            print("Invalid choice!  Enter 1, 2 or 3.")
        else:
            break   # Exit loop when valid choice is entered

    # --- Assign difficulty ranges based on choice ---
    if choice == "1":
        print("Easy mode selected!")
        min_val, max_val = 1, 10
    elif choice == "2":
        print("Medium mode selected!")
        min_val, max_val = 1, 20
    else:
        print("Hard mode selected!")
        min_val, max_val = 1, 50

    # --- Initialize variables ---
    score = 0
    total_questions = 5
    results = []   # Will store (question_no, correct/incorrect, response_time)

    # --- Ask questions loop ---
    for question_number in range(1, total_questions + 1):
        num1 = random.randint(min_val, max_val)
        num2 = random.randint(min_val, max_val)
        operator = random.choice(["+", "-"])  # Choose addition or subtraction

        # Ensure positive result for subtraction
        if operator == "-" and num2 > num1:
            num1, num2 = num2, num1

        if question_number == total_questions:
            print("Challenge question!")   # Last one is challenge

        print(f"Score: {score}")
        print(f"Question {question_number} of {total_questions}:")
        print(f"What is {num1} {operator} {num2}? ", end="")

        # Measure start time
        start_time = time.time()
        try:
            answer = int(input())   # User's input
        except ValueError:
            answer = None           # If user enters non-numeric
        end_time = time.time()

        # Calculate response time
        response_time = int(end_time - start_time)

        # Compute correct answer safely
        if operator == "+":
            correct_answer = num1 + num2
        else:
            correct_answer = num1 - num2

        # --- Check correctness ---
        if answer == correct_answer:
            # Award points based on speed
            if response_time <= 2:
                points = 8
            elif response_time <= 4:
                points = 6
            else:
                points = 4
            print(f"Correct! You answered in {response_time} second(s) - {points} point(s) awarded.")
            score += points
            results.append((question_number, "Yes", response_time))
        else:
            print(f"Incorrect! You answered in {response_time} second(s) - no points awarded.")
            results.append((question_number, "No", response_time))

    # --- Calculate summary stats ---
    correct_count = sum(1 for _, correct, _ in results if correct == "Yes")
    percent_correct = round((correct_count / total_questions) * 100)
    avg_time = round(sum(t for _, _, t in results) / total_questions)

    # --- Final Results ---
    print("\nResults:")
    print(f"Final score: {score}")
    print(f"Correct answers: {percent_correct}%")
    print(f"Average response time: {avg_time}s")

    # --- Breakdown of performance ---
    print("\nBreakdown:")
    print("Question   Correct   Time")
    for q, correct, t in results:
        print(f"{q:<10} {correct:<8} {t}s")

    print("\nNote: The correct answer percentage and average response time should be rounded to the nearest integer.")

# --- Run program ---
if __name__ == "__main__":
    main()
