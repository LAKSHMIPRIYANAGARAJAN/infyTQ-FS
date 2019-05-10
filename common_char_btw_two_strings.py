#PF-Assgn-33
    
def find_common_characters(msg1,msg2):
    
    st=""
    for i in msg1:
        for j in msg2:
            if(i==j and i!=" " and j!=" "):
                st=st+j
    
                
    return st            
msg1="I like Python"
msg2="Java is a very popular language"
common_characters=find_common_characters(msg1,msg2)
print(common_characters)
