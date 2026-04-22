#Separate even and odd numbers from numbers.txt

#Make a list for even and odd nums
even_numbers = []
odd_numbers = []

for num in numbers:
    num = int(num.strip())

    if num % 2 == 0:
        even_numbers.append(str(num))
    else:
        odd_numbers.append(str(num))
