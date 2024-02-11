import PySimpleGUI as sg
from Converter import convert
from datetime import datetime
import Log

#setting standard font
font_std = ("Calibri", 14)

def windowSol():
    #This var will be used as the userprompt for entering an array
    user_prompt_arr = sg.Text('Enter your array with spaces and nums',font=font_std,text_color='Orange',background_color='#2C2825')

    #This var will be used as the userprompt for entering a number
    user_prompt_num = sg.Text('Enter number to count',font=font_std,text_color='Orange',background_color='#2C2825')

    #This var will be used as a result output
    result = sg.Text(background_color='#2C2825',text_color='Orange',font=font_std)

    #This var will be used as the input string array
    input_arr = sg.InputText(tooltip="Enter your array", key = "array",font=font_std)

    #This var will be used as the input string num
    input_num = sg.InputText(tooltip="Enter your number", key = "number",font=font_std)

    #This var will be used as the count button
    count_button = sg.Button('Count',font=font_std)

    window = sg.Window("Lab Program", layout=[[user_prompt_arr,input_arr],
                                            [user_prompt_num,input_num],
                                        [count_button,result]])

    #An algorithm that will make the lab task
    
    Log.writelog("PROGRAM EXECUTION")
    while True:
        events, vals = window.read()
        match events:
            case "Count":
                try:
                    #cnt_arr is for storing input array
                    cnt_arr = convert(vals["array"].split(' '))
                    #num_cmp is for storing input number
                    num_cmp = int(vals["number"])
                    #cnt stands for counter
                    tm1 = datetime.now()
                    cnt = 0
                    for i in cnt_arr:
                        if i > num_cmp:
                            cnt += 1
                    tm2 = datetime.now()
                    Log.writelog(str(tm2 - tm1))
                    result.update(f"Result is: {cnt}") 
                except:
                    Log.writelog("ERROR INPUT")
                    result.update("Wrong input")
            case sg.WIN_CLOSED:
                break
        print(events, "\n", vals)
    Log.writelog("PROGRAM CLOSED")
    window.close()