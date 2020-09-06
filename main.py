import time
from os import system
from random import randint
import keyboard, pyfiglet

# Table Width And Height
TABLE_WIDTH = 20
TABLE_HEIGHT = 20

# Main Variables
table = [[' ' for i in range(TABLE_WIDTH)] for _ in range(TABLE_HEIGHT)]
direction = "d"
snake = [[0,0]]
apples = []

# Duration in Seconds
duration = 0.5

# Scores
scores = 0

# Clear The Table
def clear_table():
    global table
    table = [[' ' for i in range(TABLE_WIDTH)] for _ in range(TABLE_HEIGHT)]

# Clear The Screen
def clrscr():
    system("cls")

# Draw Snake On Table Variable
def set_m():
    clear_table()
    for i in snake:
        table[i[0]][i[1]] = '*'
    for i in apples:
        table[i[0]][i[1]] = '+'

def is_ok(snake):
    ans = []
    for i in snake:
        if i not in ans:
            ans.append(i)
        else:
            return False
    return True

# Draw Table On Screen
def draw():
    print("Score : " + str(len(snake) - 1))
    print('_' * (TABLE_WIDTH + 2))
    for i in table:
        print("|",end='')
        for j in i:
            print(j,end='')
        print("|")
    print('_' * (TABLE_WIDTH + 2))

# Add Apples On Table
def add_apple():
    x = -1
    y = -1
    while True:
        b = 1
        x = randint(0,TABLE_WIDTH - 1)
        y = randint(0,TABLE_HEIGHT - 1)
        for i in snake:
            if i[0] == x and i[1] == y:
                b = 0
                break
        if b == 1:
            break
        else:
            continue
    apples.append([x,y])

def change_direction(d):
    global direction
    if direction == 'r' and d == 'l':
        return
    if direction == 'u' and d == 'd':
        return
    if direction == 'l' and d == 'r':
        return
    if direction == 'd' and d == 'u':
        return
    direction = d

clrscr()

while True:
    if direction == "r":
        tar = [snake[0][0],snake[0][1] + 1]
        if tar in apples:
            apples.remove(tar)
            snake.append([snake[-1][0],snake[-1][1] - 1])
        ans = snake.copy()
        for c,i in enumerate(snake):
            if c == 0:
                continue
            ans[c] = snake[c - 1].copy()
        ans[0][1] += 1
        snake = ans.copy()
    elif direction == "l":
        tar = [snake[0][0],snake[0][1] - 1]
        if tar in apples:
            apples.remove(tar)
            snake.append([snake[-1][0],snake[-1][1] + 1])
        ans = snake.copy()
        for c,i in enumerate(snake):
            if c == 0:
                continue
            ans[c] = snake[c - 1].copy()
        ans[0][1] -= 1
        snake = ans.copy()
    elif direction == "d":
        tar = [snake[0][0] + 1,snake[0][1]]
        if tar in apples:
            apples.remove(tar)
            snake.append([snake[-1][0] + 1,snake[-1][1]])
        ans = snake.copy()
        for c,i in enumerate(snake):
            if c == 0:
                continue
            ans[c] = snake[c - 1].copy()
        ans[0][0] += 1
        snake = ans.copy()
    elif direction == "u":
        tar = [snake[0][0] - 1,snake[0][1]]
        if tar in apples:
            apples.remove(tar)
            snake.append([snake[-1][0] - 1,snake[-1][1]])
        ans = snake.copy()
        for c,i in enumerate(snake):
            if c == 0:
                continue
            ans[c] = snake[c - 1].copy()
        ans[0][0] -= 1
        snake = ans.copy()
    try:
        set_m()
    except:
        break
    draw()
    if scores % 5 == 0:
        add_apple()
        if duration > 0:
            duration -= 0.01
    if snake[0][0] == TABLE_WIDTH or snake[0][0] == -1:
        break
    if snake[0][1] == TABLE_HEIGHT or snake[0][1] == -1:
        break
    if not is_ok(snake):
        break
    if duration > 0:
        time.sleep(duration)
    scores += 1
    keyboard.on_press_key("w",lambda _: change_direction('u'))
    keyboard.on_press_key("d",lambda _: change_direction('r'))
    keyboard.on_press_key("s",lambda _: change_direction('d'))
    keyboard.on_press_key("a",lambda _: change_direction('l'))
    clrscr()

clrscr()

for i in range(5):
    print(pyfiglet.Figlet('banner').renderText('You Lose :('))
    time.sleep(0.1)
    clrscr()
    time.sleep(0.1)

print(pyfiglet.Figlet('small').renderText('Score : ' + str(len(snake) - 1)))
time.sleep(2)
clrscr()