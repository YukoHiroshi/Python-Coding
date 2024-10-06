amount=int(input("Enter the amount to withdraw:"))

dollar1=amount//100
dollar2=(amount%100)//50
dollar3=((amount%100)%50)//10

print("dollar of 100:", dollar1)
print("dollar of 50:", dollar2)
print("dollar of 10:", dollar3)