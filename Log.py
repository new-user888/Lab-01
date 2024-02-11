from datetime import datetime

def writelog(logstring):
    with open("./logfile",'a') as file:
        file.write(f"DATE: {datetime.now()} EXECUTION TIME: {logstring}\n")