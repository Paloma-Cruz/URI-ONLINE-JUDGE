def diamantes_e_areia(comb):
    pilha = []
    extraido = 0
    for elemento in comb:
        if elemento == '<':
            pilha.append(elemento)
        elif elemento == '>':
            if len(pilha) > 0:
                pilha.pop()
                extraido += 1
            else:
                return extraido
    return extraido
print(diamantes_e_areia('<<<..<......<<<<....>'))
