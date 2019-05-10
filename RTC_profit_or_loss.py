#PF-Assgn-29
def calculate(distance,no_of_passengers):
    total_price=no_of_passengers*80
    travelling_cost=(distance/10)*70
    if(total_price>=travelling_cost):
        profit=total_price-travelling_cost
        return profit
    else:
        return -1
distance=20
no_of_passengers=50
print(calculate(distance,no_of_passengers))
