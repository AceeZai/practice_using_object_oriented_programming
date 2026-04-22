class IntegerProcessor:
    def __init__(self, input_filename):
        self.input_filename = input_filename

    def process_integers(self):
        input_file = open(self.input_filename, "r")

        double_file = open("double.txt", "w")
        triple_file = open("triple.txt", "w")


        for number_line in input_file:
            number = int(number_line.strip())

            if number % 2 == 0:
                squared_value = number ** 2
                double_file.write(str(squared_value) + "\n")
            else:
                cubed_value = number ** 3
                triple_file.write(str(cubed_value) + "\n")