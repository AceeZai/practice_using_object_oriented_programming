class LifeWriter:
    def __init__(self, filename):
        self.filename = filename

    def write_lines(self):
        output_file = open(self.filename, "r")
