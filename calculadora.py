a = [10, 85, 96, 51, 2]

b = []

def cal(val,op):

    for i in a:
        if op == 'sum':
            operacion = val + i
            b.append(operacion)

        if  op == 'res':
            operacion = val - i
            b.append(operacion)

        if  op == 'multi':
            operacion = val * i
            b.append(operacion)

        if  op == 'div':
            operacion = val / i
            b.append(operacion)

cal(10, 'sum')

print(b)
