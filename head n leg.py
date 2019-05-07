def solve(heads,legs):
    error_msg="No solution"
    chicken_count=0
    rabbit_count=0
    flag=0
    c=0
    for r in range(heads,-1,-1):
        if((2*c)+(4*r))==legs:
            flag=1
            chicken_count=c
            rabbit_count=r    
            break;
        c=c+1 
    if flag==0:
        print("No solution")
    else:
        print(chicken_count,rabbit_count)
solve(150,400)
