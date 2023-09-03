#/usr/bin/python3

import PySimpleGUI as sg

layout = [[]]

wimdows = sg.Windows('converter', layout)

while True:
    event, values = windows.read()
    if event == sg.WIN_CLOSED:
        break

windows.close()
