def f1 (arg):
    if arg ==1:
        return 0
    elif arg ==2:
        return 1
    else :
        return f1(arg-1)+f1(arg-2)
