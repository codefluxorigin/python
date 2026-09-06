def print_list(list,idx):
    if(idx==len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
list1=[454,56456,4,64,65456,456,4,56456,4,56456,56,564,56456,4,564]
print_list(list1,0)