def prime(starting_range, end_range):
    lst=[]
    flag=0
    for i in range(starting_range, end_range):
        for j in range(2,i):
            if (i%j==0):
                flag=1
                break
            else:
                flag=0
        if flag==0:
            lst.append(i)
    return lst

# Driver program
starting_range = 2
end_range = 7
lst = prime(starting_range, end_range)
if len(lst) == 0:
    print("There are no prime numbers in this range")
else:
    print("The prime numbers in this range are: ", lst)


#check number is prime or not
num = 11
# If given number is greater than 1
if num > 1:
	# Iterate from 2 to n / 2
	for i in range(2, int(num/2)+1):
		# If num is divisible by any number between
		# 2 and n / 2, it is not prime
		if (num % i) == 0:
			print(num, "is not a prime number")
			break
	else:
		print(num, "is a prime number")
else:
	print(num, "is not a prime number")
