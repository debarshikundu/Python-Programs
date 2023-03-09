num_list = [n for n in range(1,10)]
string_arr = []
for i in num_list:
    if i == 1:
       string_arr.append(str(i) + 'st') 
    elif i == 2:
        string_arr.append(str(i) + 'nd') 
    elif i ==3:
        string_arr.append(str(i) + 'rd') 
    else:
        string_arr.append(str(i) + 'th')
        
for string in string_arr:
    print(string)
