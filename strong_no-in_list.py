#PF-Exer-26

def factorial(number):
    fact=1 
    while number>=1:
        fact=fact*number
        number=number-1
    return fact
def digit_sum(x):
    sum=0 
    while x!=0:
        rem=x%10
        sum=sum+factorial(rem)
        x=x//10
    return sum


def find_strong_numbers(num_list):
    s=[]
    i=0
    
    if(num_list[i]==digit_sum(num_list[i])):
        k=digit_sum(num_list[i])
        s.append(k)
        i=i+1
        return s
    else:
        i+i+1
num_list=[145,375,100,2,10]
strong_num_list=find_strong_numbers(num_list)
print(strong_num_list)
