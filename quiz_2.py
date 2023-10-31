quiz_1 = {
##
## QUESTION 1
##
    "questions": [
        {
            "code": """
x = 10
x = 'hello'
""",
            "question": "What is the value of x?",
            "possible_answers": [
                "x cannot be reused error",
                "x equals 'hello'",
                "x equals 10"
            ],
            "correct_answer_index": 1
        },
##
## QUESTION 2
##
        {
            "code": """
x, y = 1, 2, 3, 4
""",
            "question": "What is the result of the above operation?",
            "possible_answers": [
                "x equals (1, 2) and y equals (3, 4)",
                "x equals 1 and y equals 2",
                "unpacking error"
            ],
            "correct_answer_index": 2
        },
##
## QUESTION 3
##
        {
            "question": "In accordance with PEP-8, if we were defining a constant for the value of the speed of light, which would be an appropriate name?",
            "possible_answers": [
                "speedOfLight",
                "speed_of_light",
                "SPEED_OF_LIGHT"
            ],
            "correct_answer_index": 2
        },
##
## QUESTION 4
##
        {
            "code": """
name: int = 'Kamil'
""",
            "question": "What is the type of variable name?",
            "possible_answers": [
                "str",
                "int",
                "name"
            ],
            "correct_answer_index": 0
        },
##
## QUESTION 5
##
        {
            "question": "Can lists contain more than 1 type?",
            "possible_answers": [
                "True",
                "False"
            ],
            "correct_answer_index": 0
        },
##
## QUESTION 6
##
        {
            "code": """
years = [1983, 1985, 2018, 2020]
""",
            "question": "What is the value of years[-1]?",
            "possible_answers": [
                "1983",
                "None",
                "2020"
            ],
            "correct_answer_index": 2
        },
##
## QUESTION 7
##
        {
            "code": """
[1, 1] + [2, 2]
""",
            "question": "What is the result of the above operation?",
            "possible_answers": [
                "[1, 1, 2, 2]",
                "[3, 3]",
                "[]",
                "[1, 2, 1, 2]"
            ],
            "correct_answer_index": 0
        },
##
## QUESTION 8
##
        {
            "code": """
x = 10
y = 3
z = ((x // y) ** y) % x
""",
            "question": "What is the result of the above operation?",
            "possible_answers": [
                "27",
                "7",
                "7.037",
                "5"
            ],
            "correct_answer_index": 1
        },
##
## QUESTION 9
##
        {
            "code": """
name = 'Kamil'
greeting = f'Hello {name}'
""",
            "question": "What is the value of the variable greeting?",
            "possible_answers": [
                "Kamil",
                "Hello Kamil",
                "Hello {name}"
            ],
            "correct_answer_index": 1
        },
##
## QUESTION 10
##
        {
            "code": """
matrix_2D = [[1, 2, 3], 
             [4, 5, 6], 
             [7, 8, 9]]
""",
            "question": "What is the value for matrix_2D[2][2]?",
            "possible_answers": [
                "3",
                "4",
                "9"
            ],
            "correct_answer_index": 2
        },
    ]
}

quiz_2 = {
    "questions": [
        {
            "code": """
x = True
y = False
z = not x or y
""",
            "question": "What is the value of z?",
            "possible_answers": ["z is True", "z is False", "z is not defined"],
            "correct_answer_index": 1,
        },
        {
            "code": """
a = True
b = False
c = a and b
""",
            "question": "What is the value of c?",
            "possible_answers": ["c is True", "c is False", "c is not defined"],
            "correct_answer_index": 1,
        },
        {
            "code": """
num = 15
if num % 2 == 0:
    result = "Even"
else:
    result = "Odd"
""",
            "question": "What is the value of 'result' when num is 15?",
            "possible_answers": [
                "result is 'Even'",
                "result is 'Odd'",
                "result is not defined",
            ],
            "correct_answer_index": 1,
        },
        {
            "code": """
value = -3
output = "Positive" if value > 0 else "Negative"
""",
            "question": "What is the value of 'output' when 'value' is -3?",
            "possible_answers": [
                "output is 'Positive'",
                "output is 'Negative'",
                "output is not defined",
            ],
            "correct_answer_index": 1,
        },
        {
            "code": """
x = 5
y = 10
if x > y:
    result = "x is greater than y"
else:
    if x < y:
    result = "x is less than y"
        else:
    result = "x and y are equal"
""",
            "question": "What is the value of 'result' when x is 5 and y is 10?",
            "possible_answers": [
                "result is 'x is greater than y'",
                "result is 'x is less than y'",
                "result is 'x and y are equal'",
                "result is not defined",
            ],
            "correct_answer_index": 1,
        },
        {
            "code": """
def do_nothing():
    pass
""",
            "question": "What does the function 'do_nothing' do?",
            "possible_answers": [
                "The function raises an exception",
                "The function does nothing and returns None",
                "The function is not defined",
            ],
            "correct_answer_index": 1,
        },
        {
            "code": """
count = 0
while count < 5:
    count += 1
""",
            "question": "How many times does the 'while' loop run?",
            "possible_answers": [
                "0 times",
                "5 times",
                "Infinite times",
                "count is not defined",
            ],
            "correct_answer_index": 1,
        },
        {
            "code": """
for i in range(3):
    print(i)
""",
            "question": "What will be printed when this 'for' loop is executed?",
            "possible_answers": [
                "0, 1, 2",
                "1, 2, 3",
                "2, 3, 4",
                "The loop raises an exception",
            ],
            "correct_answer_index": 0,
        },
        {
            "code": """
add = lambda x, y: x + y
""",
            "question": "What does the 'add' lambda function do?",
            "possible_answers": [
                "The lambda function subtracts y from x",
                "The lambda function multiplies x and y",
                "The lambda function adds x and y",
                "The lambda function is not defined",
            ],
            "correct_answer_index": 2,
        },
    ]
}
