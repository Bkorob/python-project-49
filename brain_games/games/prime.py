import random


QUESTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game():
    num = random.randint(2, 50)
    screen_q = num
    for i in range(int(num / 2), 1, - 1):
        if num % i == 0:
            screen_ans = 'no'
            return screen_ans, screen_q
    return screen_ans, screen_q
