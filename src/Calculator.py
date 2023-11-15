class Calculator:
    num1 = 0
    num2 = 0
    result = 0

    def __init__ (self, n1, n2):
        self.num1 = n1
        self.num2 = n2

    def add(self):
        self.result = self.num1 + self.num2

    def sub(self):
        self.result = self.num1 - self.num2

    def mul(self):
        self.result = self.num1 * self.num2

    def div(self):
        self.result = self.num1 / self.num2

    def get_result(self):
        return self.result