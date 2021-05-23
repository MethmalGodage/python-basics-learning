names = ["John", "Kevin", "Melissa"]

for name in names:
    print("Are you {}?".format(name))

for number in range(1, 8):
    if number == 6:
        print("<<Skipping {}>>".format(number))
        continue
    print("Number {}".format(number))

for number in range(1, 10):
    if number == 3:
        pass
    else:
        print("Number {}".format(number))