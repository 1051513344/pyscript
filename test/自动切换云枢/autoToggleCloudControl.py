import pyautogui
from pynput import keyboard
import time

ALT_FLAG = False
control = keyboard.Controller()
def autoToggle():
    # 打开云枢
    pyautogui.moveTo((1724, 1062))  # 控制鼠标移动
    pyautogui.click(clicks=1)  # 实现鼠标单击
    # 切换
    pyautogui.moveTo((1000, 535))  # 控制鼠标移动
    pyautogui.click(clicks=1)  # 实现鼠标单击
    # 关闭云枢
    pyautogui.moveTo((1382, 267))  # 控制鼠标移动
    pyautogui.click(clicks=1)  # 实现鼠标单击

def on_press(key):
    global ALT_FLAG
    global control
    if key == keyboard.Key.alt_l:
        ALT_FLAG = True
    else:
        try:
            if ALT_FLAG:
                # print(f'alt + {key}')
                if isinstance(key, keyboard.KeyCode):
                    if key.vk == 81:
                        control.press(keyboard.Key.cmd)
                        time.sleep(1)
                        control.press('d')
                        control.release(keyboard.Key.cmd)
                        control.release('d')
                        autoToggle()
                        control.press(keyboard.Key.alt_l)
                        control.press(keyboard.Key.tab)
                        control.release(keyboard.Key.alt_l)
                        control.release(keyboard.Key.tab)
                        control.release(keyboard.Key.alt_l)
                        control.release(key)
            else:
                # print(key)
                pass
        except Exception as e:
            print(e)
            ALT_FLAG = False

def on_release(key):
    global ALT_FLAG
    global control
    if ALT_FLAG:
        # print(f'alt + {key}')
        if isinstance(key, keyboard.KeyCode):
            if key.vk == 81:
                ALT_FLAG = False

def listen_key_nblock():
    listener = keyboard.Listener(
        on_press=on_press, on_release=on_release
    )
    listener.start()  # 启动线程

if __name__ == "__main__":

    # autoToggle()
    listen_key_nblock()
    while True:
        pass

    # 循环执行pyautogui.position()获取不同位置坐标
    # while True:
    #     print("当前鼠标的坐标为：", pyautogui.position())
    #     time.sleep(1)
