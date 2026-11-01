# 1 - The first bug I spotted was the missing colon because it was easy to spot, as every other function had a colon at the end of the function. I found it from simply looking over the code. This tells me that a lot of the common errors can be found without asking AI and just taking a second to observe.
# 2 - This applies the discount based off of how much money they spend and therefore what tier they are apart of. The inputs are the amount spent/tier and the returns are the discount they get.
# 3 - I did not use AI for this exercise.
# Exercise 1
def calculate_tax(price, rate):
    return price * rate

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print(f"Tax for $100 at 7%: ${tax1:.2f}")
print(f"Tax for $250 at 8%: ${tax2:.2f}")
print(f"Tax for $350 at 5%: ${calculate_tax(350, 0.05):.2f}")

# Exercise 2
def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

original_price = 200

for tier in ["gold", "silver", "bronze", "none"]:
    print(f"{tier}: ${apply_discount(original_price, tier):.2f}")

# Exercise 3
def final_price(price, tax_rate, discount_tier):
    discounted_price = apply_discount(price, discount_tier)
    tax = calculate_tax(discounted_price, tax_rate)
    return discounted_price + tax
print(f"final_price(200, 0.07, 'gold') = {final_price(200, 0.07, 'gold'):.2f}")

# Exercise 4
orders = [(200, 'gold'), (150, 'silver'), (80, 'bronze'), (500, 'none')]

rate = 0.07
for price, tier in orders:
    total = final_price(price, 0.07, tier)
    print(f"Price: ${price} | Tier: {tier} | Total: ${total:.2f}")

# Exercise 6
x = 100
def double_it():
    x = 999
    return x * 2
print(x) # 100 prints here because the x inside the function is a local variable and does not affect the global x
print(double_it()) # 1998 because that is 999 * 2, aka doubled
print(x) # 100 prints again because the x inside the function is a local variable and does not affect the global x
