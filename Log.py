from datetime import datetime

def writelog(logstring,array,result,cmp_num):
    with open("./logfile",'a') as file:
        file.write(f"DATE: {datetime.now()}\nEXECUTION TIME: {logstring}\nNUMBER TO COMPARE WITH: {cmp_num}\nINPUT ARRAY'S SIZE: {len(array)}\nINPUT ARRAY: {array}\nRESULT: {result}\n##########################\n")
