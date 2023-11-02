from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample quiz questions and answers
quiz_data = [
    {
        'question': 'What is the capital of France?',
        'options': ['Paris', 'London', 'Berlin'],
        'correct_answer': 'Paris',
    },
    {
        'question': 'Which planet is known as the Red Planet?',
        'options': ['Mars', 'Venus', 'Jupiter'],
        'correct_answer': 'Mars',
    },
    {
        'question': 'What is the largest mammal in the world?',
        'options': ['Elephant', 'Blue Whale', 'Giraffe'],
        'correct_answer': 'Blue Whale',
    },
]

current_question = 0
score = 0

@app.route('/')
def index():
    return render_template('layout.html')

@app.route('/quiz', methods=['GET', 'POST'])
def quiz():
    global current_question
    global score

    if request.method == 'POST':
        selected_option = request.form['option']
        correct_answer = quiz_data[current_question]['correct_answer']

        if selected_option == correct_answer:
            score += 1

        current_question += 1

        if current_question < len(quiz_data):
            return render_template('quiz.html', question=quiz_data[current_question])
        else:
            return redirect(url_for('result'))

    if current_question < len(quiz_data):
        return render_template('quiz.html', question=quiz_data[current_question])
    else:
        return redirect(url_for('result'))

@app.route('/result')
def result():
    global score
    score_percentage = (score / len(quiz_data)) * 100
    return f'Your score: {score}/{len(quiz_data)} ({score_percentage:.2f}%)'

if __name__ == '__main__':
    app.run(debug=True)

