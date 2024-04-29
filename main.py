import random
produto = []
resultado = []
carrinho = []

def fechar_compra():
    if len(carrinho) != 0:
        total = 0
        print(' ')
        print('----------------NF----------------')
        print('CÓDIGO   | NOME | CATEGORIA  | VALOR')
        for posicao in range(0, len(carrinho)):
            print(carrinho[posicao][4] + '\t' + carrinho[posicao][0] + '\t' + carrinho[posicao][1] + '\t' + carrinho[posicao][2])
        print('QUANTIDADE DE ITENS: ', len(carrinho))
        for item in carrinho:
            nome, categoria, valor, quantidade, codigo = item
            total = total + float(valor)
        print('TOTAL DO CARRINHO: ', round(total,2))
        print(' ')
        print('OBRIGADO POR COMPRAR CONOSCO, VOLTE SEMPRE!')
    else:
        print(' ')
        print('OBRIGADO POR USAR O SISTEMA !')
        print(' ')

def ver_carrinho():
    if len(carrinho) != 0:
        total = 0
        print(' ')
        print('CARRINHO:')
        print(' ')
        print('CÓDIGO   | NOME | CATEGORIA  | VALOR')
        print(' ')
        for posicao in range(0, len(carrinho)):
            print(carrinho[posicao][4] + '\t' + carrinho[posicao][0] + '\t' + carrinho[posicao][1] + '\t' + carrinho[posicao][2])
        print(' ')
        print('QUANTIDADE DE ITENS: ', len(carrinho))
        for item in carrinho:
            nome, categoria, valor, quantidade, codigo = item
            total = total + float(valor)
        print(' ')
        print('TOTAL DO CARRINHO: ', round(total,2))
        print(' ')
        menu()
    else:
        print(' ')
        print('CARRINHO VAZIO!!')
        print(' ')
        menu()

def carrinho_de_compra(cod_prod):
    for pesquisa in produto:   
        for item in pesquisa:
            if cod_prod in str(item).lower():
                carrinho.append(pesquisa)
    if len(carrinho) != 0:
        print(' ')
        print('PRODUTO ADICIONADO')
        print(' ')
        menu()
    else:
        print(' ')
        print('CÓDIGO INVALIDO')
        print(' ')
        menu()
    
def menu():
    print(' ')
    print('**DIGITE O CÓDIGO DE ALGUMA DAS OPÇÕES**')
    print('1- FAZER NOVA BUSCA')
    print('2- ADICIONAR ITEM AO CARRINHO')
    print('3- VISUALIZAR OS ITENS DO CARRINHO')
    print('4- FINALIZAR COMPRA')
    print(' ')
    opcao = int(input('Digite apenas o numero da opção: '))
    print(' ')
    if opcao == 1:
        print(' ')
        print('NOVA BUSCA SOLICITADA:')
        print(' ')
        busca2 = input('NFORME NOME DO PRODUTO OU O CÓDIGO DO PRODUTO OU A CATEGORIA DO PRODUTO: ')
        busca_produto(busca2)
    elif opcao == 2:
        cod_prod = str(input('DIGITE O CÓDIGO:')).lower()
        carrinho_de_compra(cod_prod)    
    elif opcao == 3:
        ver_carrinho()
    elif opcao == 4:
        fechar_compra()
    else:
        print(' ')
        print('OPÇÃO INVALIDA')
        print(' ')
        menu()
        
def busca_produto(busca):
    conta = 0
    resultado.clear()
    if busca == '':
        print(' ')
        print('BUSCA INVALIDA')
        print(' ')
        menu()
    else:
        for pesquisa in produto:
            nome, categoria, valor, quantidade, codigo = pesquisa       
            if busca in nome.lower() or busca == codigo.lower() or busca == categoria.lower():
                    resultado.append(pesquisa)
        
        if len(resultado) == 0:
            print(' ')
            print('PRODUTO NÃO ENCONTRADO')
            menu()
        else:
            random.shuffle(resultado)
            print(' ')
            print('RESULTADOS:')           
            print('CODIGO   | NOME | CATEGORIA  | VALOR')
            for posicao in range(0, len(resultado)):
                if conta <= 4:
                    conta += 1
                    print(resultado[posicao][4] + '\t' + resultado[posicao][0] + '\t' + resultado[posicao][1] + '\t' + resultado[posicao][2])
        print(' ')
        menu()




with open('produtos.csv', 'r', encoding="utf-8") as arquivo:
    next(arquivo)
    produtos = arquivo.readlines()
    for i in produtos:
        produto.append(i.strip('\n').split(';'))

    busca = input('NFORME NOME DO PRODUTO OU O CÓDIGO DO PRODUTO OU A CATEGORIA DO PRODUTO: ').lower()
    busca_produto(busca)
    













    
    '''
                                            __
                                           /°_)
                                    .-^^^-/ /
                                 __/       /
                                <__.|_|-|_|
                            By: DinoKaminari
                                '''