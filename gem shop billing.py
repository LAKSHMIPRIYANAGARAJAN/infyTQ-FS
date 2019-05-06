def calculate_bill_amount(gems_list, price_list, reqd_gems,reqd_quantity):
    bill_amount=0
    #Write your logic here
    a=len(gems_list)
    b=len(reqd_gems)
    i=0
    for i in range(b):
        j=0
        for j in range(a):
            if(reqd_gems[i]==gems_list[j]):
                bill_amount=(bill_amount+(price_list[j]*reqd_quantity[i]))
                break
        if(bill_amount>30000):
              bill_amount=bill_amount-(bill_amount*0.05)
        if(bill_amount==0):
            bill_amount=-1
            break
    return bill_amount


gems_list=["Emerald","Ivory","Jasper","Ruby","Garnet"]
price_list=[1760,2119,1599,3920,3999]
reqd_gems=["Ivory","Emerald","Garnet"]
reqd_quantity=[3,10,12]

bill_amount=calculate_bill_amount(gems_list, price_list, reqd_gems, reqd_quantity)
print(bill_amount)
