#This function converts string array to int array
def convert(string_arr):
    int_arr = []
    for i in string_arr:
        int_arr.append(int(i))
    return int_arr

#This function converts string from a file to int array
def convert_file(file_path):
    with open(file_path,"r") as file:
        string_arr = file.readline().split(' ')
    int_arr = []
    for i in string_arr:
        int_arr.append(int(i))
    return int_arr