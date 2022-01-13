# Question 2
standard_deduction=10000
depend_deduction=3000
gross=input("enter your gross income :")
No_of_dependents=input("Enter your number of dependents :")
taxable_income=int(gross)-int(standard_deduction)-(int(depend_deduction)*int(No_of_dependents))
tax=(float(taxable_income)*0.2)
print("Your income tax is :")
print(float(tax))
