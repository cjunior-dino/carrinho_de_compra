import adiciona_carrinho
def fechar_compra():
    if len(adiciona_carrinho.carrinho) != 0:
        total = 0
        print(' ')
        print('----------------NF----------------')
        print('CODIGO   | NOME | CATEGORIA  | VALOR')
        for posicao in range(0, len(adiciona_carrinho.carrinho)):
            print(adiciona_carrinho.carrinho[posicao][4] + '\t' + adiciona_carrinho.carrinho[posicao][0] + '\t' + adiciona_carrinho.carrinho[posicao][1] + '\t' + adiciona_carrinho.carrinho[posicao][2])
        print('QUANTIDADE DE ITENS: ', len(adiciona_carrinho.carrinho))
        for item in adiciona_carrinho.carrinho:
            nome, categoria, valor, quantidade, codigo = item
            total = total + float(valor)
        print('TOTAL DO CARRINHO: ', round(total,2))
        print(' ')
        print('OBRIGADO POR COMPRAR CONOSCO, VOLTE SEMPRE!')
    else:
        print(' ')
        print('OBRIGADO POR USAR O SISTEMA !')
        print(' ')
    return False
        