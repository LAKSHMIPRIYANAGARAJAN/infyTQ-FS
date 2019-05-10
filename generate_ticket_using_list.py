

def generate_ticket(airline,source,destination,no_of_passengers):
    ticket_number_list=[]
    src=source[0:3]
    des=destination[0:3]
    x=101
    while(x<101+no_of_passengers):
        j=str(x)
        k=airline+":"+src+":"+des+":"+j
        ticket_number_list.append(k)
        x=x+1
    if(no_of_passengers>5):
        ticket_number_list=ticket_number_list[-5:]
    return ticket_number_list
print(generate_ticket("AI","Bangalore","London",2))
