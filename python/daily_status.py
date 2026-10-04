# idea is to print + email myself with something like:  if I commit today, it will make my streak X
# ? does digital ocean work with emails atm?  days since May 30, 2011 ?
# also = "2025: 162 2024: 125 (total : 350)  - 2024 avg: 2.78 2025 avg: 3.12"
also = " 2026-08-30 13:10:58.548849 2026: 101 2025: 163 2024: 125 total fitness entries: 452  - 2024 avg: 2.78 2025 avg: 3.13 2026 avg: 1.94  "
also = " 2026-10-03 12:49:00.019392 2026: 112 2025: 163 2024: 125 total fitness entries: 463  - 2024 avg: 2.78 2025 avg: 3.13 2026 avg: 2.8 "
itsok = "(invalid)" #"streak KAPUTT, but thats OK"
from datetime import date
today = date.today()
print ('---', today, '---')

work = date(2011, 5, 30)
delta = today - work
print("1. work:", int(delta.days/365), '-', int((delta.days%365)/30))

'''
coding = date(2025, 11, 4)
delta = today - coding
print("2. coding:", delta.days, itsok)

planks = date(2025, 11, 16)
delta = today - planks
print("3. planks:", delta.days, itsok)
'''

lifting = date(2026, 8, 7)
delta = today - lifting
print("2. lifting:", delta.days+1, ' (somehow replaced planks...)')

fitness = date(2024, 2, 15)
delta = today - fitness
print("3. fitness:", round((delta.days/7), 1), "(weeks)", (delta.days), "(days)")

print("  >", also)
print("  > ",  round(400 / (delta.days/7), 2), "hardcoded 400! 112+163+125")

print("______")

print("<<< other reminders :  up and not crying at the fates + harmless people >>> ")
print(" a. I already know a lot, but tend to forget my habits under stress ")
print(" b. less is more - oftentimes... kalma")
print(" c. delegate more, way more - can I show you? am I doing this right? do you have a minute?")
print(" d. be more brave and take risks like a chad, and just look cool doing normal things")
print(" e. smaller portions - eating healthy is the hard part:  practice denying myself sweets")

print("______         \_(ツ)_/¯")
