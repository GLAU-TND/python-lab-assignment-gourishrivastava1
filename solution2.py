try:
    a='34'+54
    g=int('vsAH')
    obj='Hi'
    obj.remove()
except TypeError as e:
    print("TypeError:",e)
except ValueError as e:
    print("ValueError:",e)
except AttributeError as e:
    print("AttributeError:",e)
