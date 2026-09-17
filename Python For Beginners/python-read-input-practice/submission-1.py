def add_two_numbers() -> int:
    line=input()
    splits=line.split(",")
    num1 = int(splits[0])
    num2 = int(splits[1])
    return num1 + num2


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
