num_int = int(input("Input a number: "))  
max_int = 0
while num_int >= 0:
    if max_int < num_int:
        max_int = num_int
    num_int = int(input("Input a number: "))
print("The maximum is", max_int)

