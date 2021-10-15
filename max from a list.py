
# try block to handle the exception
try:
    my_list = []
     
    while True:
        my_list.append(int(input()))
        max_value = max(my_list)
        max_index = my_list.index(max_value)



# if the input is not-integer, just print the list
except:
    print(max_value)