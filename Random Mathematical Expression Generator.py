# Random Mathematical Expression Generator
import random
import operator


def math_quiz():
    print("=== Math Quiz Game ===")
    print("Solve the following problems:\n")

    # Available operations with symbols
    operations = [
        ('+', operator.add),
        ('-', operator.sub),
        ('*', operator.mul),
        ('//', operator.floordiv)  # Integer division for simplicity
    ]

    # Generate and present 5 questions
    score = 0
    for _ in range(5):
        # Randomly select operation and numbers
        op_symbol, op_func = random.choice(operations)
        a = random.randint(1, 10)
        b = random.randint(1, 10)

        # Ensure division problems have integer solutions
        if op_symbol == '//':
            a = a * b  # Guarantees clean division

        # Calculate correct answer
        correct_answer = op_func(a, b)

        # Present question
        print(f"What is {a} {op_symbol} {b}?")

        # Get user answer
        while True:
            try:
                user_answer = int(input("Your answer: "))
                break
            except ValueError:
                print("Please enter a valid integer!")

        # Check answer
        if user_answer == correct_answer:
            print("Correct!\n")
            score += 1
        else:
            print(f"Incorrect. The right answer is {correct_answer}\n")

    # Display final score
    print(f"Your score: {score}/5")


# Run the quiz
if __name__ == "__main__":
    math_quiz()