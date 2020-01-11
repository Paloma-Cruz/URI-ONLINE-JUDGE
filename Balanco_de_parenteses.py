comb = str(input())
pilha = []
for elemento in comb:
    if elemento == '(':
        pilha.append(elemento)
    else:
        if len(pilha) > 0:
            pilha.pop()
        else:
            print('incorrect')
if len(pilha) == 0:
    print('correct')
else:
    print('incorrect')
