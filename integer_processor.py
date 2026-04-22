class IntegerProcessor:
    def __init__(self, input_filename):
        self.input_filename = input_filename

    def process_integers(self):
        input_file = open(self.input_filename, "r")

        double_file = open("double.txt", "w")
        triple_file = open("triple.txt", "w")
