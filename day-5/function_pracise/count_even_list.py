# in list number find even all

lt=[1,0,45,23,3,7,98,34,12]

def cot(lit):
    count=0
    for i in lt:
        if(i&2==0):
            count+=1
        print(f"In list total {count} numbers are Even")
        
    return count

cot(lt)

