class A:
    a, b =56,60
    def __init__(self):
         pass
    @classmethod
    def sub(self):
        return self.a - self.b
    @staticmethod
    def test(self):
        print("from test...")





print(A.sub())
print(test())

a = A()
print(a.sub())
b=A()
print(b.sub())
