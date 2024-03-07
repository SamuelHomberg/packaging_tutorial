def add_one(number: int):
    """A function to add one to a number.

    Args:
        number (int): A number.

    Returns:
        int: number + 1
    """
    return number + 1

class ExampleClass():
    """An example class doing example things.
    """
    def __init__(self):
        self.var = 1

    def get_var(self) -> int:
        """Gets a variable of the class.

        Returns:
            int: Variable.
        """
        return self.var