from IPython.core.display import display, HTML, clear_output

init_css = lambda: HTML("""
<style>
@keyframes slow-open {
    from {opacity: 0%;}
    to {opacity: 100%;}
}

.quiz-element {
    border-radius: 0.4rem;
    padding: 10px;
}

.quiz-question {
    opacity: 100%;
    background-color: #dbe9ff;
    animation-name: slow-open;
    animation-duration: 2s;
}

.quiz-score {
    background-color: #dbe9ff;
}

div.output_area pre {
    line-height: 15px !important;
    padding: 15px 0 0px 15px !important;   
}

</style>
""")

def run_quiz(quiz: dict):
    score = 0
    quiz_length = len(quiz['questions'])

    for index, question in enumerate(quiz['questions']):
        
        correct_answer_index = question['correct_answer_index']
        display(HTML(generate_question_html(question, index, quiz_length)))

        while True:    
            user_answer = input('Type in the letter of one of the above choices and press enter:\n').upper()
            user_answer = ord(user_answer[0]) - 65 if len(user_answer) > 0 else None
            if user_answer is not None and user_answer in range(len(question['possible_answers'])):
                if user_answer == correct_answer_index:
                    display(HTML('<em>Correct ✔️</em><hr/>'))
                    score += 1
                else:
                    display(HTML(f'<em>Incorrect ❌<br/>The correct answer was: {question["possible_answers"][correct_answer_index]}</em><hr/>'))
                input('Press enter to continue...')
                clear_output()
                break
            else:
                display(HTML('<em>Error! Try again.</em>'))

    score_percent = f'{(score / quiz_length) * 100:2.1f}'
    display(HTML(f'''
    <div class="quiz-score quiz-element">
        <h2>Final score:</h2>
        <hr style="border-top: 2px solid black;"/>
        {score} / {quiz_length}<br/>{score_percent}%
    </div>
    '''))
    
def generate_question_html(question: dict, index: int, quiz_length: int) -> str:
    question_html = f'<h2>Question {index + 1} of {quiz_length}</h2><hr style="border-top: 2px solid black;"/>'
    
    if 'code' in question:
        question_html += f'<h3>Given the code:</h3><pre><code class="code-snippet">{question["code"][1:]}</code></pre>'
    if 'question' in question:
        question_html += f'<h3>{question["question"]}</h3>'
    if 'possible_answers' in question:
        answers_html = [f'<li><em>{possible_answer}</em></li>' for possible_answer in question['possible_answers']]
        question_html += f'<ol style="list-style-type: upper-alpha;">{"".join(answers_html)}</ol>'
        
    return f'<div class="quiz-question quiz-element">{question_html}</div>'