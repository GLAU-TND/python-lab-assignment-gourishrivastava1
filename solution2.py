try:
    a='34'+54
except TypeError as e:
    print("TypeError:",e)
try:
    g=int('vsAH')
except ValueError as e:
    print("ValueError:",e)
try:
    obj='Hi'
    obj.remove()
except AttributeError as e:
    print("AttributeError:",e)
