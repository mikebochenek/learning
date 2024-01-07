import pandas as pd

# would be cool to publish: https://www.gradio.app/guides/quickstart#building-your-first-demo

def affordability(income, price, down):
    equity = down / price

    # First mortgage: max. 67% of the property value
    # Second mortgage: max. 13% of the property value
    # must be payed back within 15 years or until you reach retirement age (whichever comes first)
    amortization = 0 # TODO

    # incidental expenses is 1% of the purchase price.
    # imputed mortgage interest is based on a long-term average interest rate of 5%.
    mortgage = price - down
    monthly_cost = (mortgage * 0.06 + amortization) / 12
    monthly_income = income/12*0.33 # how much can be afforded monthly

    print ('  own equity', equity, 'monthly', monthly_cost, 'vs.', monthly_income)

    return (equity >= 0.2) and (monthly_cost <= monthly_income)

assert (affordability(150000, 800000, 300000))
assert (False == affordability(150000, 800000, 100000)) # not enough downpayment
assert (False == affordability(101000, 800000, 200000)) # not enough income