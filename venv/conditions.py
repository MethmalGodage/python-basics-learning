def calculator():
    on = True

    while on:
        operator_value = input("Operator (+ or - or * or /) or q to quit): ")
        if operator_value == "q":
            print("Bye, Thank You!")
            pass
            on = False
        else:
            first_value = float(input("First Value: "))
            second_value = float(input("Second Value: "))

            if operator_value == "+":
                print("Addition is {}".format(first_value + second_value))
            elif operator_value == "-":
                print("Subtraction is {}".format(first_value - second_value))
            elif operator_value == "*":
                print("Multiply is {}".format(first_value * second_value))
            elif operator_value == "/":
                print("Divide is {}".format(first_value / second_value))
            else:
                print("Invalid operator. Please try again!")


calculator()
