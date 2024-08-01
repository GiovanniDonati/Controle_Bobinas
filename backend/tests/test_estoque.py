def __gerar_enderecos_validos():
    enderecos = []
    
    for letra in 'ABCD':
        for number in range(1,96):
            enderecos.append(f'{letra}{number}')
            
    for number in range(17, 96):
        enderecos.append(f'E{number}')

    for number in range(47, 96):
        enderecos.append(f'F{number}')

    for number in range(82, 96):
        enderecos.append(f'G{number}')

    for letra in 'ABCDE':
        for number in range(1, 5):
            enderecos.append(f'G1-{letra}{number}')
    
    for letra in 'ABCD':
        for number in range(1, 6):
            enderecos.append(f'G2-{letra}{number}')
    
    for letra in 'AB':
        for number in range(1, 12):
            enderecos.append(f'G3-{letra}{number}')
    
    return enderecos  

