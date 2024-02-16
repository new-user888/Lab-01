import PySimpleGUI as sg
import src.Log as Log
import os
import webbrowser
import random 
from datetime import datetime

#setting standard font
font_std = ("Calibri", 14)

def randomInputSol():
    #This var will be used as the userprompt for entering a number
    user_prompt_num = sg.Text('Enter number to count',font=font_std,text_color='Orange',background_color='#2C2825')

    #This var will be used as a result output
    result = sg.Text(background_color='#2C2825',text_color='Orange',font=font_std)

    #This var will be used as the count button
    count_button = sg.Button('Count',font=font_std)

    #This var will be used as the input string num
    input_num = sg.InputText(tooltip="Enter your number", key = "cmp_num",font=font_std)

    #This var will be used as the input string array
    input_arr_size = sg.InputText(tooltip="Size of your array", key = "array_size",font=font_std)

    #This var will be used as the userprompt for entering an array
    user_prompt_arr = sg.Text('Enter size of your array',font=font_std,text_color='Orange',background_color='#2C2825')
    
    #This var will be used as the button to view file with input and output
    view_file_button = sg.Button('View file',font=font_std)

    window = sg.Window("Random Input",layout=[[user_prompt_arr,input_arr_size],
                                              [user_prompt_num,input_num],
                                              [count_button,result],
                                              [view_file_button]])
    while True:
        events, vals = window.read()
        match events:
            case "Count":
                try:
                    cmp_num = int(vals['cmp_num'])
                    arr_size = int(vals['array_size'])
                    arr = []
                    for i in range(arr_size):
                       arr.append(random.randint(0,100))
                    tm1 = datetime.now()
                    cnt = 0
                    for arr_el in arr:
                        if arr_el > cmp_num:
                            cnt += 1
                    tm2 = datetime.now()
                    Log.writelog(str(tm2 - tm1),arr,cnt,cmp_num)
                    result.update(f"Result: {cnt}")
                except:
                    Log.writelog("ERROR-INPUT","ERROR-INPUT","ERROR-INPUT","ERROR-INPUT")
                    result.update("Wrong input")
            case "View file":
                try:
                    webbrowser.open(os.getcwd() + "/logfile")
                except:
                    result.update("There's no logfile")
            case sg.WIN_CLOSED:
                break
        print("Event:", events, "Vals: ", vals)
    window.close()

if __name__ == "__main__":
    randomInputSol()