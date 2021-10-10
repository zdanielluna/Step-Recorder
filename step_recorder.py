import pyautogui
import os
import keyboard

input_string = input('\nIncidente:')
print('\nCapturar (CTRL + 1)')
print('Sair     (CTRL + 2)')


count = 0
while True:
    if (keyboard.is_pressed('ctrl+1')):
        if not os.path.exists(f'{input_string}'):
            os.mkdir(f'{input_string}')
        ss = pyautogui.screenshot()
        ss.save(f'{input_string}/{input_string}_{count}.png')
        count += 1
        print(f'{input_string}_{count}.png Step {count} gravado!')
    elif (keyboard.is_pressed('ctrl+2')):
        os._exit(0)
