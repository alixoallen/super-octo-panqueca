
lista=('lápis', 1.75,
       'borracha',2.00,
       'caderno',22.00,
       'estojo',15.65,
       'transferidor',3.25,
       'compasso',9.99,
       'mochila',25.58,
       'canetas',2.75,
       'livros',45.00)
print('-'*50)
print(f'{"listagem de preços":^40}')
print('-'*50)
for pos in range(0,len(lista)):
    if pos%2==0:
        print(f'{lista[pos]:.<30}', end='')
    else:
        print(f'{lista[pos]:.>7.2f}')