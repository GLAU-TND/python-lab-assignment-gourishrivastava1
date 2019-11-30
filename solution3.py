try:
    c=int(input())
    d=int(input())
except KeyboardInterrupt as e:
    print ('KeyboardInterrupt',e)
except EOF as e:
    print("End of file error",e)
except ValueError as e:
    print("ValueError:",e)
