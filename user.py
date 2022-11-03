class User:

    # constructor for user object
    def __init__(self, lamt=0, ir=0.0, file='AmortizedValues'):
        self.lamt = lamt
        self.ir = ir
        self.file = file

    # getter and setter methods for lamt, ir, and file name
    def get_lamt(self):
        return self.lamt

    def set_lamt(self, x1):
        self.lamt = x1

    def get_ir(self):
        return self.ir

    def set_ir(self, x2):
        self.ir = x2

    def get_file(self):
        return self.file

    def set_file(self, x3):
        self.file = x3
