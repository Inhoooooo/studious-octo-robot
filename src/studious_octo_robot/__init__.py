class Example:
    def __init__(self, bar):
        if bar:
            bar += 1
            bar = bar * bar

        else:
            self.some_string = "foo"


def main() -> None:
    print("Hello from studious-octo-robot!")
