n = int(input("Enter the length of the sequence: ")) # Do not change this line
#Design an algorithm that generates the first n numbers in the following sequence:; 1, 2, 3, 6, 11, 20, 37, ___, ___, ___, …
# Sequencið virkar þannig að fyrstu 3 tölurnar eru alltaf plúsaðar saman

first_num = 1
second_num = 2
third_num = 3

for i in range (n):
    if i == 0  or i == 1 or i == 2:
        print(i+1, end=', ')
    else:
        print(first_num + second_num + third_num, end=', ')
        first_num = second_num
        second_num = third_num

        third_num = third_num + second_num + first_num