import os


class Widget():
    def __init__(
            self,
            foo: str = os.environ['SOME_VAR']
    ):
        self.bar = foo

    def func1(self):
        return self.bar
