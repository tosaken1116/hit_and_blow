import random
import re
def input_answer(history):
    input_format_flag = False
    first_input = True
    while not input_format_flag:
        user_input = input("answer:" if first_input else "\033[1Aanswer:")
        print(f"\033[1Aanswer:{' '*len(user_input)}")
        if len(user_input) ==3 and re.fullmatch('[0-9]+',user_input) and len(user_input) == len(set(user_input)) and not is_answer_duplicate(history,user_input):
            input_format_flag=True
        first_input = False
    return user_input

def answer_init():
    answer = ""
    choice_flag = False
    while not choice_flag:
        add_answer = str(random.randint(0,9))
        if add_answer not in answer:
            answer += add_answer
        if len(answer) == 3:
            choice_flag=True
    return answer

def is_answer_duplicate(history,input_answer):
    for ans in history:
        if ans["user_input"] == input_answer:
            return True
    return False
def check_answer(answer,user_input):
    hit = 0
    blow = 0
    for index, char in enumerate(user_input):
        if char == answer[index]:
            hit +=1
        elif char in answer:
            blow += 1
    return (hit,blow)

def main():
    answer =answer_init()
    correct_flag = False
    history = []
    for i in range(0,10):
        user_input = input_answer(history)
        hit,blow = check_answer(answer,user_input)
        if hit==3:
            correct_flag = True
        history.append({"hit":hit, "blow":blow,"user_input":user_input})
        output_result(history)
        if correct_flag:
            print("\n"*(len(history)+1))
            print("\033[32mcorrect\033[0m\n")
            break
    if not correct_flag:
        print("\n"*(len(history)+1))
        print('game over')
    print(f'answer = \033[41m{answer}\033[0m')
    return input('continue?[y:n]' )== "n"

def output_result(history):
    print("\033[31mhit \033[34mblow \033[0muser_input")
    for result in history:
        print(f' \033[31m{result["hit"]}    \033[34m{result["blow"]}     \033[0m{result["user_input"]}')
    print(f'\033[{len(history)+3}A')
if __name__=="__main__":
    continue_flag = False
    while not continue_flag:
        continue_flag = main()
    print('exit')