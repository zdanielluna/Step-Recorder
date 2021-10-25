import pyautogui
import os
import pathlib
import keyboard

desktop = pathlib.Path.home() / 'Desktop'


def valida_entrada(incidente):
    if (os.path.exists(f'{desktop}/{incidente}')):
        print(
            'Já existe um diretório criado com o número deste incidente, por favor insira um diferente:')
        executa()


def exibe_comandos():
    print('\nCapturar  (ctrl+1)')
    print('Sair      (ctrl+2)')
    print('Reiniciar (ctrl+3)')
    print('Abortar   (ctrl+c)')


def executa():

    incidente = input('\nIncidente:')
    # Verifica se já existe um diretório com esse nome
    valida_entrada(incidente)
    exibe_comandos()

    count = 0
    while True:

        if (keyboard.is_pressed('ctrl+1')):
            # Cria um diretório para o incidente, caso não exista ainda.
            if not os.path.exists(f'{desktop}/{incidente}'):
                os.mkdir(f'{desktop}/{incidente}')
            # Captura e salva a tela
            ss = pyautogui.screenshot()
            ss.save(f'{desktop}/{incidente}/{incidente}_{count}.png')
            count += 1
            print(f'{incidente}_{count}.png Step {count} gravado!')

        elif (keyboard.is_pressed('ctrl+2')):
            os._exit(0)
        elif (keyboard.is_pressed('ctrl+3')):
            executa()


executa()
