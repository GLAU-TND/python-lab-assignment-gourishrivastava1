class MyException(Exception):
    def __init__(self,v):
        self.v=v
    def __str__(self):
        return str(self.v)
def Xyz(a,b):
    c=a+b
    if c<150:
        raise MyException("Custom Exception Occurred")
    else:
        return c
print(Xyz(20,30))
