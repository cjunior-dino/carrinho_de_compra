
import random
import importa_arquivo

resultado = []
def busca_produto(busca):
    conta = 0
    resultado.clear()
    if busca == '':
        print(' ')
        print('BUSCA INVALIDA')
        print(' ')
        
    else:
        for pesquisa in importa_arquivo.produto:
            nome, categoria, valor, quantidade, codigo = pesquisa       
            if busca in nome.lower() or busca == codigo.lower() or busca == categoria.lower():
                    resultado.append(pesquisa)
        
        if len(resultado) == 0:
            print(' ')
            print('PRODUTO NÃO ENCONTRADO')

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
    return True