# mortgage.py
#
# Exercise 1.7
import os
os.system('cls')
#-----------------------------------------
# EMI calulation formula EMI = [P x R x (1+R)^N]/[(1+R)^N-1]
# P = Principal, R = Interest rate per month (ej. 11% = 11/(12 x 100)), N = Number of installments

principal = 500000.0
rate = 0.05
payment = 2684.11 #monthly payment
total_paid = 0.0
month = 0

extra_payment_start_month = 61
extra_payment_end_month = 108
extra_payment = 1000

while principal > 0:
    month += 1
    payed = principal * (1 + rate/12) - payment
    principal = payed if payed > 0 else 0 #to fix the last payment going negative
    total_paid = total_paid + payment

    if month >= extra_payment_start_month and month <= extra_payment_end_month:
       principal = principal - extra_payment
       total_paid = total_paid + extra_payment

    print(month, round(total_paid, 2), round(principal, 2))

print()
print(f'Total paid {round(total_paid, 2):,}')
print(f'Total months {month}')