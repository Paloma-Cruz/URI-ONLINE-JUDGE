troco = int(input())
print(troco)
lista = [1, 2, 5, 10, 20, 50, 100]
lista = lista[::-1]
for i in lista:
    contador = 0
    if troco < i:
        print('{} nota(s) de R$ {},00' .format(contador, i))
    else:
        while troco >= i:
            troco -= i
            contador += 1
        print('{} nota(s) de R$ {},00' .format(contador, i))
