from math import sqrt
a,b =map(int, input('ikkita son kiriting: ').split(' '))
c = input(' +\n - \n * \n /\n V\n sinus\ncos\n **\n,Amalni tanlang: ')
if c == '+':
    print(f'siz kiritgan sonlarning yigindis {a + b}-ga teng')
elif c == '-':
    print(f'siz kiritgan sonlarning ayirmasi {a - b}-ga teng')
elif c == '*':
    print(f'siz kiritgan sonlarning kupaytmasi {a * b}-ga teng')
elif c == '/':
    print(f'siz kiritgan sonlarning bulinmasi {a / b}-ga teng')
elif c == 'V':
    print(f'siz kiritgan sonning ildizi {sqrt(a)}-ga teng')
    print(f'siz kiritgan sonning ildizi {sqrt(b)}-ga teng')
elif c == 'sin':
     print(f'siz kiritgan sonning sinusi{sqrt(a)}-ga teng')
     print(f'siz kiritgan sonning sinusi{sqrt(b)}-ga teng')
elif c == 'cos':
     print(f'siz kiritgan sonning cosinusi {sqrt(a)}-ga teng')
     print(f'siz kiritgan sonning cosinusi {sqrt(b)}-ga teng')
elif c == '**':
    print(f'siz kiritgan sonnig kvadrati {sqrt(a ** a)}-ga teng')
    print(f'siz kiritgan sonning kvadrati {sqrt(b ** b)}-ga teng')
else:
    print('skaji e')
