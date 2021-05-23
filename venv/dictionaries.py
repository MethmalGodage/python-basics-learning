stuff = {"food": 15, "energy": 100, "protein": 22.5}

# print(stuff.get("protein"))
# print(stuff.items())
# print(stuff.keys())
# print(stuff.values())

# print(stuff.popitem())
# print(stuff)

# print(stuff.setdefault("food"))
# print(stuff)

new_items = {"fat": 33.54, "vitamin": 1.44}
stuff.update(new_items)
print(stuff)

new_items = {"fat": 32.1, "vitamin": 55}
stuff.update(new_items)
print(stuff)

stuff.update(fat=5.32)
print(stuff)

stuff.update(carbohydrate=33.2)
print(stuff)
