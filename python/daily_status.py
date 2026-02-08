# idea is to print + email myself with something like:  if I commit today, it will make my streak X
# ? does digital ocean work with emails atm?  days since May 30, 2011 ? 
also = "2025: 162 2024: 125 (total : 350)  - 2024 avg: 2.78 2025 avg: 3.12"

from datetime import date
today = date.today()
print ('---', today, '---')

work = date(2011, 5, 30)
delta = today - work
print("1. work:", int(delta.days/365), '-', int((delta.days%365)/30))

coding = date(2025, 11, 4)
delta = today - coding
print("2. coding:", delta.days)

planks = date(2025, 11, 16)
delta = today - planks
print("3. planks:", delta.days, "KAPUTT!")

fitness = date(2024, 2, 15)
delta = today - fitness
print("4. fitness:", round((delta.days/7), 1))

print("  ", also)