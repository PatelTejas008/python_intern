num=[1,45,77,99,45,87,28,90,34,87,12,89]

#method of 1 short cut
# def large(ty):
#     print(f"The Large number in list is :{max(ty)} ")
#     return max(ty) 

# large(num)

#method of 2 logic use


def large_find(list_name):
    large_value=list_name[0]
    for i in list_name:
        if i > large_value:
            large_value = i
    print(large_value)
    return large_value


up(num)