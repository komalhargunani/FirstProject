print("Halo World")


#how to take input and arithmetic operations
first_number = input("enter the value for first number: ")
second_number = input("enter the value for second number: ")
sum = float(first_number) + float(second_number)
print("Sum is:" +str(sum))

# if-else example
weight = int(input("Weight: "))
unit = input("(K)g or (L)bs: ")
if unit.upper() == "K":
    converted = weight / 0.45
    print("weight in Lbs: " +str(converted))
else:
    converted = weight * 0.45
    print("weight in kg: " +str(converted))

#while loop
i = 1
while(i <= 10):
    print(i * '*')
    i = i + 1

#for_loop

numbers = [1,2,3,4,5,6]
for item in numbers:
    print(item)

i=0
while i< len(numbers):
    print(numbers[i])
    i=i+1


