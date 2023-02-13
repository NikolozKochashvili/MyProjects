import sys
import Single
import MarriedFilingJointly
import MarriedFilingSeparately
import HeadOfHousehold

status = int(input("0 - Single filer\n" + \
                   "1 - Married jointly\n" + \
                   "2 - Married separately\n" + \
                   "3 - Head of household\n\n" + \
                   "Enter the filing status: "))

if status < 0 or status > 3:
  print("Error: invalid status")
  input()
  sys.exit()

income = eval(input("Enter income: "))

if status == 0:
    tax = Single.tax(income)
elif status == 1:
    tax = MarriedFilingJointly.tax(income)
elif status == 2:
    tax = MarriedFilingSeparately.tax(income)
else:
    tax = HeadOfHousehold.tax(income)



print(f"\nTax: {tax:.2f}\n" + \
      f"Remaining income: {(income - tax):.2f}")

input()