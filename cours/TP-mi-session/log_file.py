class LogFile:
    def __init__(self, filename):
        print("Nous sommes dans LogFile")
        self.filename = filename

    def __enter__(self):
        self.file = open(self.filename, 'a')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.file.close()


if __name__ == "__main__":
    # Test du context manager
    with LogFile("logfile.txt") as file:
        file.write("Test log file.")
