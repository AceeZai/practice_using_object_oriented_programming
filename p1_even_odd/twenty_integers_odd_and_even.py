# Separate even and odd numbers from numbers.txt

class NumberSeparator:
    def __init__(self, filename):
        self.input_filename = filename

    def separate_even_and_odd(self):
        with open(self.input_filename, "r") as input_file, \
             open("even.txt", "w") as even_file, \
             open("odd.txt", "w") as odd_file:

            for number_line in input_file:
                number_value = int(number_line.strip())

                if number_value % 2 == 0:
                    even_file.write(f"{number_value}\n")
                else:
                    odd_file.write(f"{number_value}\n")

        print("Done creating even.txt and odd.txt")


# RUN
number_separator = NumberSeparator("numbers.txt")
number_separator.separate_even_and_odd()