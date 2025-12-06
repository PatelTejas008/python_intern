name=["panda","Tejaa","Patel","Jadu","demon"]

def list_element(lis,idx=0):
    if(idx==len(lis)):
        return 1
    print(lis[idx].capitalize())
    list_element(lis,idx+1)
    return

list_element(name)