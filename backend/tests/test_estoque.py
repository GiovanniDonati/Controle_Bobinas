def __gerar_enderecos_validos():
    enderecos = []
    
    for number in range(1, 96):
        for letra in 'ABCD':
            enderecos.append(f'{letra}{number}')

        if number >= 17:  # Adiciona E, F, G após cada bloco de A-D
            enderecos.append(f'E{number}')
            if number >= 47:
                enderecos.append(f'F{number}')
                if number >= 82:
                    enderecos.append(f'G{number}')

    for number in range(1, 5):
        for letra in 'ABCDE':
            enderecos.append(f'G1-{letra}{number}')

    for number in range(1, 6):
        for letra in 'ABCD':
            enderecos.append(f'G2-{letra}{number}')

    for number in range(1, 12):
        for letra in 'AB':
            enderecos.append(f'G3-{letra}{number}')
    
    return enderecos

print(__gerar_enderecos_validos())
