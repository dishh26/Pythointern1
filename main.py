quiz_data_india = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. Kolkata", "C. New Delhi", "D. Chennai"],
        "answer": "C"
    },
    {
        "question": "Which river is considered the holiest river in India?",
        "options": ["A. Yamuna", "B. Ganga", "C. Brahmaputra", "D. Narmada"],
        "answer": "B"
    },
    {
        "question": "Who is known as the Father of the Nation in India?",
        "options": ["A. Jawaharlal Nehru", "B. Mahatma Gandhi", "C. Subhash Chandra Bose", "D. Sardar Patel"],
        "answer": "B"
    },
    {
        "question": "Which is the largest state in India by area?",
        "options": ["A. Maharashtra", "B. Uttar Pradesh", "C. Madhya Pradesh", "D. Rajasthan"],
        "answer": "D"
    },
    {
        "question": "Which festival is known as the Festival of Lights in India?",
        "options": ["A. Holi", "B. Diwali", "C. Navratri", "D. Eid"],
        "answer": "B"
    },
    {
        "question": "Which Indian city is also known as the Silicon Valley of India?",
        "options": ["A. Hyderabad", "B. Pune", "C. Bengaluru", "D. Chennai"],
        "answer": "C"
    }
]

def ask_question(question_data):
    print(question_data["question"])
    for option in question_data["options"]:
        print(option)
    user_answer = input("Enter the letter of your answer: ").strip().upper()
    return user_answer == question_data["answer"]

def run_quiz(quiz_data):
    score = 0
    for question_data in quiz_data:
        if ask_question(question_data):
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is {question_data['answer']}.")
        print()  # Print a newline for better readability

    print(f"Your final score is {score}/{len(quiz_data)}.")

if __name__ == "__main__":
    run_quiz(quiz_data_india)
