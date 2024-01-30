def numbers(line, num):  # um dicionario com cada key tendo uma lista espeficicando quais segmentos devem ser ligados
    if line == 1:
        linn = {1: '  #', 2: '###', 3: '###', 4: '# #', 5: '###', 6: '###', 7: '###', 8: '###', 9: '###', 0: '###'}
        return linn[num]
    elif line == 2:
        linn = {1: '  #', 2: '  #', 3: '  #', 4: '# #', 5: '#  ', 6: '#  ', 7: '  #', 8: '# #', 9: '# #', 0: '# #'}
        return linn[num]
    elif line == 3:
        linn = {1: '  #', 2: '###', 3: '###', 4: '###', 5: '###', 6: '###', 7: '  #', 8: '###', 9: '###', 0: '# #'}
        return linn[num]
    elif line == 4:
        linn = {1: '  #', 2: '#  ', 3: '  #', 4: '  #', 5: '  #', 6: '# #', 7: '  #', 8: '# #', 9: '  #', 0: '# #'}
        return linn[num]
    else:
        linn = {1: '  #', 2: '###', 3: '###', 4: '  #', 5: '###', 6: '###', 7: '  #', 8: '###', 9: '###', 0: '###'}
        return linn[num]
