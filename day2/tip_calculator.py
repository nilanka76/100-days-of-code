print("Tip Calculator")
bill = float(input("What was the Total Bill Amount? "))
tip = float(input(r"How much tip you want to give? 10%, 12% or 15% :"))
people = float(input("How many people to split the bill? "))
bill_with_tip = tip/100 * bill + bill
bill_per_persone = bill_with_tip / people
print(f"Total bill: {bill_with_tip:.2f}")
print(f"Each person will pay: {round(bill_per_persone, 2)}")