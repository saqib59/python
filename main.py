'''
100 days of code - Python
'''


questions = [
    {
        "question": "What is the capital of France?",
        "answers": ["Berlin", "London", "Paris", "Madrid"],
        "correct": "Paris"
    },
    {
        "question": "What is 2 + 2?",
        "answers": ["3", "4", "5", "6"],
        "correct": "4"
    },
    {
        "question": "What is the color of the sky?",
        "answers": ["Green", "Blue", "Red", "Yellow"],
        "correct": "Blue"
    },
]

points = 0  # Initialize points

for q in questions:
    print(f"Question: {q['question']}")
    for i, answer in enumerate(q['answers']):
        print(f"{i+1}. {answer}")
    
    # Take input from the user
    user_answer = input("Enter the number of your answer: ")
    
    try:
        # Check if the input is a valid integer and within the range of answers
        user_answer_index = int(user_answer) - 1
        if user_answer_index >= 0 and user_answer_index < len(q['answers']):
            if q['answers'][user_answer_index] == q['correct']:
                print("Correct!")
                points += 1  # Add points for correct answer
            else:
                print("Wrong answer.")
        else:
            print("Invalid answer number.")
    except ValueError:
        print("Please enter a valid number.")
    
    print()  # Print a new line for better readability

print(f"Your total points: {points}")
