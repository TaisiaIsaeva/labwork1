def bin_search(p, a, l, r):
    while l<r :
        m = (l+r)//2
        if a[m] == p:
            return True
        if a[m]>p:
            return bin_search(p, a, l, m)
        if a[m]<p:
            return bin_search(p, a, m+1, r)
    return False

def bin_s_exp (p, a, l, r):
    while l < r:
        m = (l + r) // 2
        if a[m] == p:
            return m
        if a[m] > p:
            return bin_s_exp(p, a, l, m)
        if a[m] < p:
            return bin_s_exp(p, a, m + 1, r)
    return 'Числа в массиве нет'


a= list(map(int, input('Введите числа массива в порядке возрастания \n').split( )))
p = int(input('Введите число для поиска \n'))

if bin_search(p, a, 0, len(a)):
    print('Число есть в массиве')
    print('Хотите узнать, на какой позиции?')
    answ1= input()
    if answ1=='Дa ' or answ1 == 'Да' :
        x = bin_s_exp (p, a, 0, len(a))
        print( f'Позиция: {x}' )
else:
    print('Такого числа в массиве нет')
