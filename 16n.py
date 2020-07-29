#16
a=input('is it raining ?')
a=a.lower()
if (a=='yes'):
    b=input('it is windy ? ')
    b=b.lower()
    if(b=='yes'):
        print('it is too windy for an umbrella ')
    else:
        print('take an umbrella')
else:
    print('enjoy de day ')
