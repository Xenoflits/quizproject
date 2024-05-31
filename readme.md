# QuizBrain

QuizBrain is a simple quiz game implemented in Python. It asks users true or false questions and checks their answers, keeping track of the score. This project is designed as a beginner exercise to help understand basic concepts of Python such as classes, loops, and conditional statements.

## Features

- Asks a series of true/false questions.
- Keeps track of the current question number and the user's score.
- Checks the user's answer and updates the score accordingly.
- Provides feedback on the user's progress and score.
- Ends the quiz if the user provides a wrong answer.

## How to Use

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/QuizBrain.git
    ```
2. Navigate to the project directory:
    ```bash
    cd QuizBrain
    ```
3. Run the quiz game:
    ```bash
    python quiz_brain.py
    ```

## Code Overview

The main class in this project is `QuizBrain`. Here's a brief overview of its methods:

- `__init__(self, question_list)`: Initializes the quiz with a list of questions, sets the question number to 0, and the score to 0.
- `still_has_questions(self)`: Checks if there are any questions left in the quiz.
- `next_question(self)`: Prompts the user with the next question, checks their answer, and updates the score.
- `check_answer(self, answer, real_answer)`: Compares the user's answer to the correct answer.
- `winner(self)`: Prints a winning message if the user scores 12 points.

## Example

```python
questions = [
    {"text": "The sky is blue.", "answer": "True"},
    {"text": "The moon is made of cheese.", "answer": "False"},
    # Add more questions as needed
]

quiz = QuizBrain(questions)
quiz.next_question()
