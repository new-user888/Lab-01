import PySimpleGUI as sg
from Converter import convert_file
from datetime import datetime
import Log

#setting standard font
font_std = ("Calibri", 14)

def fileSol():
    #This var will be used as the userprompt for entering a number
    user_prompt_num = sg.Text('Enter number to count',font=font_std,text_color='Orange',background_color='#2C2825')
    #This var will be used as the input string num
    input_num = sg.InputText(tooltip="Enter number", key = "number",font=font_std)
    #This var will be used as a result output
    result = sg.Text(background_color='#2C2825',text_color='Orange',font=font_std)
    #This var will be used as the count button
    count_button = sg.Button('Count',font=font_std)
    #This var is used as the file_browser
    file_browser = sg.FileBrowse(file_types=(("Text Files", "*.txt"),),key="path")
    #This var is var browser prompt
    file_browser_prompt = sg.Text("Path/to/a/file",font=font_std,text_color='Orange',background_color='#2C2825')
    #Creating a window
    win = sg.Window("Lab Program",layout=[[file_browser,file_browser_prompt],
                                          [user_prompt_num,input_num],
                                          [count_button,result]])
    while True:
        events, vals = win.read()
        match events:
            case "Count":
                try:
                    int_arr = convert_file(vals['path'])
                    cmp_num = int(vals['number'])
                    tm1 = datetime.now()
                    cnt = 0
                    for i in int_arr:
                        if i > cmp_num:
                            cnt += 1
                    tm2 = datetime.now()
                    Log.writelog(str(tm2 - tm1),int_arr,cnt,cmp_num)
                    result.update(f"Result is: {cnt}")
                except:
                    Log.writelog("ERROR-INPUT","ERROR-INPUT","ERROR-INPUT","ERROR-INPUT")
                    result.update("Wrong input")
            case sg.WIN_CLOSED:
                break
        print(events, "\n", vals)
    win.close()

if __name__ == "__main__":
    fileSol()