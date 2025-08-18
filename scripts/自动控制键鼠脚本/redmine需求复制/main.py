import pydirectinput
import time

def main():
    openTask()
    start = 0
    end = 14
    bottomTask = [11, 13]
    for task in range(start, end):
        if task+1 in bottomTask:
            continue
        execute(task, start)
    for task in bottomTask:
        execute(task-1, -1)

def execute(task, start):
    pydirectinput.mouseDown(x=650, y=365+task*21)
    pydirectinput.mouseUp(x=650, y=365+task*21)
    time.sleep(0.3)
    pydirectinput.click(button='right')
    if task < 16:
        pydirectinput.mouseDown(x=700, y=365+task*21+130)
        pydirectinput.mouseUp(x=700, y=365+task*21+130)
    else:
        pydirectinput.mouseDown(x=700, y=365+16*21+120)
        pydirectinput.mouseUp(x=700, y=365+16*21+120)
    if task == start:
        tab(2)
    else:
        tab(1)
    copyTaskContent()
    tab(1)

def openTask():
    tab(1)

def copyTaskContent():
    pydirectinput.keyDown('ctrl')
    time.sleep(0.2)
    pydirectinput.keyDown('v')
    time.sleep(0.2)
    pydirectinput.keyUp('v')
    time.sleep(0.2)
    pydirectinput.keyUp('ctrl')
    pydirectinput.keyDown('enter')
    pydirectinput.keyUp('enter')

def tab(num):
    pydirectinput.keyDown('alt')
    time.sleep(0.2)
    for n in range(num):
        pydirectinput.keyDown('tab')
        time.sleep(0.2)
        pydirectinput.keyUp('tab')
    pydirectinput.keyUp('alt')

if __name__ == "__main__":
    main()