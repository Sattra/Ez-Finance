def tablea_1(k, n, money):
    values = (1+k)**n
    return values*money

def table_2(k, n, money):
    values = (((1+k)**n)-1)/k
    return values*money

def table_3(k, n):
    values = 1/((1+k)**n)
    return values

def table_4(k, n, money):
    values = (1-(1/((1+k)**n)))/k
    return values*money

aaa
