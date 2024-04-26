import random
import operator

def error_handle(problem_answer):
    switch = False
    validated_guess = 0.0
    while not switch:
        try:
            validated_guess = float(input('Please enter a valid answer: '))
            if isinstance(validated_guess, float):
                switch = True
        except ValueError:
            pass
    return validated_guess

def random_problem():
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv,
    }

    num_1 = random.randint(1, 10)
    num_2 = random.randint(1, 10)
    operation = random.choice(list(operators.keys()))
    answer = float(round(operators.get(operation)(num_1, num_2), 3))
    print(f'What is {num_1} {operation} {num_2}')
    return answer

def ask_question():
    answer = random_problem()
    try:
        guess = float(input('Enter your answer: '))
    except ValueError:
        guess = error_handle(answer)
    return guess == answer

def game():
    score = 0
    while True:
        if ask_question():
            score += 1
            print('Correct!')
        else:
            print('Incorrect')
            break
    print(f'======== Game Over ========\nYour score is {score}\nKeep going!')

game()
