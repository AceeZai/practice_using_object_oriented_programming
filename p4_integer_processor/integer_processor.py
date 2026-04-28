import os

class IntegerProcessor:
    def __init__(self, input_filename):
        # Make path always correct regardless of where you run the script
        base_dir = os.path.dirname(__file__)
        self.input_filename = os.path.join(base_dir, input_filename)

    def process_integers(self):
        try:
            with open(self.input_filename, "r") as input_file, \
                 open("double.txt", "w") as double_file, \
                 open("triple.txt", "w") as triple_file:

                for number_line in input_file:
                    number_line = number_line.strip()

                    if number_line == "":
                        continue

                    number = int(number_line)

                    if number % 2 == 0:
                        double_file.write(str(number ** 2) + "\n")
                    else:
                        triple_file.write(str(number ** 3) + "\n")

            print("Done: files created successfully.")

        except FileNotFoundError:
            print("Error: integers.txt file not found.")


# RUN
processor = IntegerProcessor("integers.txt")
processor.process_integers()