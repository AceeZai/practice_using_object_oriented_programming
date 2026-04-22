#Separate even and odd numbers from numbers.txt

class NumberSeparator:
    def __init__(self, filename):
        self.input_filename = filename

    def separate_even_and_odd(self):
        even_file = open("even.txt", "w")
        odd_file = open("odd.txt", "w")
        input_file = open(self.input_filename, "r")

        for number_line in input_file:
            num = int(number_line.strip())

            if num % 2 == 0:
                even_file.write(str(num) + "\n")
            else:
                odd_file.write(str(num) + "\n")

