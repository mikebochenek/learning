'''
would be cool to publish: https://www.gradio.app/guides/quickstart#building-your-first-demo
https://pbpython.com/amortization-model-revised.html
https://ron.sh/calculating-amortization-with-python/
'''
import pandas as pd

def affordability(income, price, down):
    equity = down / price

    # First mortgage: max. 67% of the property value
    # Second mortgage: max. 13% of the property value
    # must be payed back within 15 years or until you reach retirement age (whichever comes first)
    amortization = 0
    if (equity < 0.33):
        s = price*0.33-down
        amortization = calculate_amortization(s, 0.03) # TODO should not be hardcoded
        print ('   !equity too low', equity, int(amortization), 'second m=', s)

    # incidental expenses is 1% of the purchase price.
    # imputed mortgage interest is based on a long-term average interest rate of 5%.
    mortgage = price - down
    monthly_cost = int((mortgage * 0.06 + amortization*12) / 12)
    monthly_income = income/12*0.33 # how much can be afforded monthly

    print ('  own equity', equity, 'monthly', monthly_cost, 'vs.', monthly_income)

    return (equity >= 0.2) and (monthly_cost <= monthly_income)

# https://sidhanthk9.medium.com/how-to-code-an-amortization-schedule-in-python-e2d2b417c61a
def calculate_amortization(PV, r):
    n = 15
    output= -1 * (PV*r)/(((1/(1+r)**n))-1)  # formula calculated using sum of infinite GP series
    return output/12

assert (affordability(150000, 800000, 300000))
assert (False == affordability(150000, 800000, 100000)) # not enough downpayment
assert (False == affordability(101000, 800000, 200000)) # not enough income

assert (calculate_amortization(15000, 0.07) > 120)