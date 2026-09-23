def Quizz():
    questions = {
        "questions": [
            "What is the capital of France?",
            "What is 2+2?",
            "What is the largest ocean on Earth?",
            "What is the chemical symbol for gold?",
            "Who wrote 'Romeo and Juliet'?"
        ],
        "answerq1": ["Paris", "London", "Berlin", "Madrid"],
        "answerq2": ["3", "4", "5", "6"],
        "answerq3": ["Atlantic Ocean", "Indian Ocean", "Arctic Ocean", "Pacific Ocean"],
        "answerq4": ["Au", "Ag", "Fe", "Hg"],
        "answerq5": ["William Shakespeare", "Charles Dickens", "Jane Austen", "Mark Twain"],
        "correct_answers": ["Paris", "4", "Pacific Ocean", "Au", "William Shakespeare"]
    }

    while True:
        print("Final Year Student Quizz")
        matric_number = input("Enter your Matric Number: ")

        if matric_number == "":
            print("Invalid Matric Number. Please try again.")
            continue

        print("Welcome to the Quizz!")
        break

    # Initialize the score
    score = 0
    total_questions = len(questions["questions"])

    for i in range(total_questions):
        print(f"\nQuestion {i + 1}: {questions['questions'][i]}")
        options = questions[f'answerq{i + 1}']
        for j in range(len(options)):
            print(f"{j + 1}. {options[j]}")

        user_answer = input("Enter the number of your answer: ")

        # Validate the user's input
        if not user_answer.isdigit() or not (1 <= int(user_answer) <= len(options)):
            print("Invalid choice. Marked as incorrect.")
            continue

        # Convert the chosen number into the actual answer text
        chosen_answer = options[int(user_answer) - 1]
        correct_answer = questions["correct_answers"][i]

        if chosen_answer == correct_answer:
            print("Correct!")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {correct_answer}")

    # Final score display
    print("\n" + "=" * 30)
    print(f"Quizz Complete, {matric_number}!")
    print(f"Your Score: {score}/{total_questions}")

    percentage = (score / total_questions) * 100
    print(f"Percentage: {percentage:.2f}%")

    if percentage == 100:
        print("Excellent! Perfect score! 🎉")
    elif percentage >= 60:
        print("Good job! 👍")
    else:
        print("Keep practicing! 📚")


Quizz()