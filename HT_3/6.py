########################################################
'''Task 6. Вводиться число. Якщо це число додатне,
знайти його квадрат, якщо від'ємне, збільшити його
на 100, якщо дорівнює 0, не змінювати.'''
def my_fun(a):
    if a>0:
        a=a**2
    elif a<0:
        a+=100
    else:
        a
    return a
###############################
x=float(input('Input numeric x = '))
print('Output: ',my_fun(x))