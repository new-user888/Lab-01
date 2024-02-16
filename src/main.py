import PySimpleGUI as sg
import src.WindowSol as ws
import src.FileSol as fs
import src.RandomInputSol as ris

#Settig theme
sg.theme('DarkAmber')

'''
This file is the file for LAB_01 from Algorithms theory subject
'''

via_file = sg.Button("Via File",font=ws.font_std)
via_program = sg.Button("Via Program",font=ws.font_std)
via_rand = sg.Button("Via Random",font=ws.font_std)

solve_window = sg.Window("Way To Solve",layout=[[via_file,via_program,via_rand]])
while True:
    events = solve_window.read()[0]
    match events:
        case "Via Program":
            ws.windowSol()
        case "Via File":
            fs.fileSol()
        case "Via Random":
            ris.randomInputSol()
        case sg.WIN_CLOSED:
            break
    print(events)
solve_window.close()