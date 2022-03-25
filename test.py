lis = []
def even_num():
    for i in range(51):
        if i % 2 == 0:
            lis.append(i)
    return(lis) 
        
print(even_num())