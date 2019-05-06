def get_count(num_list):
    count=0
    x=0
    y=len(num_list)
    
    while(x<(y-1)):
        if(num_list[x]==num_list[x+1]):
            count+=1
            x=x+1
        else:
            x=x+1
        
    
    return count


num_list=[1,1,5,100,-20,-20,6,0,0]
print(get_count(num_list))
