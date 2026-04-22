class LifeWriter:
    def __init__(self):
        self.filename = r"Traceback (most recent call last):
  File "C:\Users\Acee Zai Mendez\PycharmProjects\PythonProject\p3_life_writer\life_writer.py", line 16, in <module>
    life_writer = LifeWriter("p3_life_writer/mylife.txt")
TypeError: LifeWriter.__init__() takes 1 positional argument but 2 were given

Process finished with exit code 1

    def write_lines(self):
        with open(self.filename, "w") as output_file:
            while True:
                line_input = input("Enter line: ")
                output_file.write(line_input + "\n")

                more_lines = input("Are there more lines y/n? ")
                if more_lines.lower() == "n":
                    break
        print("File writing complete at:", self.filename)

life_writer = LifeWriter("p3_life_writer/mylife.txt")
life_writer.write_lines()