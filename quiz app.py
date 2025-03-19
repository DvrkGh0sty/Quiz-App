quiz_data = [
    {
        "question": "What is the capital of France?",
        "options": ["A. Paris", "B. London", "C. Berlin", "D. Madrid"],
        "answer": "A"
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["A. Earth", "B. Mars", "C. Jupiter", "D. Saturn"],
        "answer": "B"
    },
    {
        "question": "Who wrote 'To Kill a Mockingbird'?",
        "options": ["A. Harper Lee", "B. Mark Twain", "C. J.K. Rowling", "D. Ernest Hemingway"],
        "answer": "A"
    },
    {
        "question": "What is the largest ocean on Earth?",
        "options": ["A. Atlantic Ocean", "B. Indian Ocean", "C. Arctic Ocean", "D. Pacific Ocean"],
        "answer": "D"
    },
    {
        "question": "What is the chemical symbol for water?",
        "options": ["A. H2O", "B. CO2", "C. NaCl", "D. O2"],
        "answer": "A"
    }
]

def display_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)

def get_user_answer():
    while True:
        user_answer = input("Your answer (A/B/C/D): ").strip().upper()
        if user_answer in ["A", "B", "C", "D"]:
            return user_answer
        else:
            print("Invalid input. Please enter A, B, C, or D.")

def run_quiz(quiz_data):
    score = 0
    for question in quiz_data:
        display_question(question)
        user_answer = get_user_answer()
        if user_answer == question["answer"]:
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question['answer']}.\n")
    return score

def display_result(score, total_questions):
    print(f"Quiz ended! Your score is {score}/{total_questions}.")
    percentage = (score / total_questions) * 100
    print(f"You scored {percentage:.2f}%.")

def replay_quiz():
    while True:
        replay = input("Do you want to play again? (yes/no): ").strip().lower()
        if replay in ["yes", "no"]:
            return replay == "yes"
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

def main():
    print("Welcome to the Quiz App!\n")
    total_questions = len(quiz_data)

    while True:
        score = run_quiz(quiz_data)
        display_result(score, total_questions)

        if not replay_quiz():
            print("Thank you for playing! Goodbye!")
            break

if __name__ == "__main__":
    main()