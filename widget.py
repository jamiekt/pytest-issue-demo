import os


class Widget():
    def __init__(
            self,
            foo: str = None
    ):
        self.bar = foo if foo is not None else os.environ['SOME_VAR']

    def func1(self):
        return self.bar
