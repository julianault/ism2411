# Exercise 1
inventory = ["pen", "notebook", "stapler", "tape", "marker"]

print(inventory)
print(len(inventory))


# Exercise 2
print(inventory[0])
print(inventory[-1])
print(inventory[len(inventory) // 2])


# Exercise 3
print(inventory[:3])
print(inventory[-2:])
print(inventory[::2])


# Exercise 4
inventory.append("envelope")
print(inventory)
inventory.remove("tape")
print(inventory)
inventory.sort()
print(inventory)


# Exercise 5
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("Tuples are useful for coordinates because their values cannot be changed.")

print(coords)


# Exercise 6
sales = [100, 250, 75, 480, 200]

total = sum(sales)
count = len(sales)
average = total / count

print(total)
print(count)
print(average)
print(max(sales))
print(min(sales))


# Exercise 7
prices = [9.99, 14.99, 4.99, 24.99, 1.99]

discounted = []

for price in prices:
    discounted.append(round(price * 0.90, 2))

print(prices)
print(discounted)


# Exercise 8
sales = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]

high_sales = []

for sale in sales:
    if sale > 300:
        high_sales.append(sale)

print(high_sales)
print(len(high_sales))
print(sum(high_sales) / len(high_sales))