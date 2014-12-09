def tablea_1(interest, year, money):
    n = int(year)
    k = float(interest)
    values = ((1+k)**n)*money
    return values

def table_2(interest, year, money):
    n = int(year)
    k = float(interest)
    values = ((((1+k)**n)-1)/k)*money
    return values

def table_3(interest, year, money):
    n = int(year)
    k = float(interest)
    values = (1/((1+k)**n))*money
    return values

def table_4(interest, year, money):
    n = int(year)
    k = float(interest)
    values = ((1-(1/((1+k)**n)))/k)*money
    return values
