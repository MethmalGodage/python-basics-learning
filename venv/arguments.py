def user_info(name, age, city):
    ''' This functions prints the name, age and city '''

    print("{} is {} years old, from {}".format(name, age, city))


def user_info(name, age=0, city="Colombo"):
    ''' This functions prints the name, age and city '''

    print("{} is {} years old, from {}".format(name, age, city))


user_info("Robert", 40, "Dakota")
user_info(age=20, name="Julia")
