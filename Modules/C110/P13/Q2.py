#Q2 Revision

gross_salaey = int(input("Gross salary:"))

if gross_salaey < 10000 :
    print("Tax payable is 0")
elif gross_salaey >= 10000 and gross_salaey < 20000:
    tax = gross_salaey * 5/100 
    tax = round(tax,1)
    print("Tax payable is",tax)
elif gross_salaey >= 20000 and gross_salaey < 40000:
    tax = gross_salaey * 10/100 
    tax = round(tax,1)
    print("Tax payable is",tax)
else:
    print("Tax payable is 5000")
