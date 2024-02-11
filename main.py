import PySimpleGUI as sg
import WindowSol as ws
import FileSol as fs

#Settig theme
sg.theme('DarkAmber')

'''
This file is the file for LAB_01 from Algorithms theory subject
'''

via_file = sg.Button("Via File",font=ws.font_std)
via_program = sg.Button("Via Program",font=ws.font_std)

solve_window = sg.Window("Way To Solve",layout=[[via_file,via_program]])
while True:
    events = solve_window.read()[0]
    match events:
        case "Via Program":
            ws.windowSol()
        case "Via File":
            fs.fileSol()
        case sg.WIN_CLOSED:
            break
    print(events)
solve_window.close()