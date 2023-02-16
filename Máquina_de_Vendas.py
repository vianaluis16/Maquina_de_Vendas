def recebePagamento(valor, somaValorPago = 0):
    """
    Recebe o valor pago e o armazena em uma soma(caso possível)
    """
    if somaValorPago >= valor:
        return somaValorPago
    else:
        valorPago = float(input("Qual valor a ser pago? "))
        if valorPago>0:
            return recebePagamento(valor, somaValorPago+valorPago)
        else:
            print("Valor inexistente.")
            return recebePagamento(valor, somaValorPago)


def devolveTroco(troco):
    """
    imprime as notas do troco
    """
    troco = round(troco, 2)
    if troco >= 100: 
        print("R$100,00")
        devolveTroco(troco - 100)
    elif troco >= 50: 
        print("R$50,00")
        devolveTroco(troco - 50)
    elif troco >= 20:
        print("R$20,00")
        devolveTroco(troco - 20)
    elif troco >= 10:
        print("R$10,00")
        devolveTroco(troco - 10)
    elif troco >= 5:
        print("R$5,00")
        devolveTroco(troco - 5)
    elif troco >= 2:
        print("R$2,00")
        devolveTroco(troco - 2)
    elif troco >= 1:
        print("R$1,00")
        devolveTroco(troco - 1)
    elif troco >= 0.50:
        print("R$0,50")
        devolveTroco(troco - 0.50)
    elif troco >= 0.25:
        print("R$0,25")
        devolveTroco(troco - 0.25)
    elif troco >= 0.10:
        print("R$,10")
        devolveTroco(troco - 0.10)
    elif troco >= 0.05:
        print("R$0,05")
        devolveTroco(troco - 0.05)
    elif troco >= 0.01:
        print("R$0,01")
        devolveTroco(troco - 0.01)

def maquina(prod1, prod2, prod3, prod4, prod5):
    """
    Verifica e atualiza o estoque dos produtos, registra a compra e define o troco


    Parâmetros : estoque dos prods (5)

    """
    if prod1==0 and prod2==0 and prod3==0 and prod4==0 and prod5==0:
        print("Desculpe, a maquina está sem produtos")
        exit()
    precoP1 = 3.7
    precoP2 = 3.5
    precoP3 = 2.4
    precoP4 = 2.5
    precoP5 = 1.75
    precoProdutoEscolhido = 0
    print(f"1 - Batata   - R${precoP1:.2f} - Estoque: {prod1}")
    print(f"2 - Coca     - R${precoP2:.2f} - Estoque: {prod2}")
    print(f"3 - Chiclete - R${precoP3:.2f} - Estoque: {prod3}")
    print(f"4 - Biscoito - R${precoP4:.2f} - Estoque: {prod4}")
    print(f"5 - Bombom   - R${precoP5:.2f} - Estoque: {prod5}")
    pedido = int(input("Escolha o produto: "))
    if 1 <= pedido <= 5:
        if pedido == 1:
            if prod1 == 0:
                print("Desculpe mas Batata está indisponivel")
            else:
                print(f"Batata - Preço: R${precoP1:.2f}")
                prod1 -= 1
                precoProdutoEscolhido = precoP1
        elif pedido == 2:
            if prod2 == 0:
                print("Desculpe mas Coca está indisponivel")
            else:
                print(f"Coca - Preço: R${precoP2:.2f}")
                prod2 -= 1
                precoProdutoEscolhido = precoP2
        elif pedido == 3:
            if prod3 == 0:
                print("Desculpe mas Chiclete está indisponivel")
            else:
                print(f"Chiclete - Preço: R${precoP3:.2f}")
                prod3 -= 1
                precoProdutoEscolhido = precoP3
        elif pedido == 4:
            if prod4 == 0:
                print("Desculpe mas Biscoito está indisponivel")
            else:
                print(f"Biscoito - Preço: R${precoP4:.2f}")
                prod4 -= 1
                precoProdutoEscolhido = precoP4
        elif pedido == 5:
            if prod5 == 0:
                print("Desculpe mas Bombom está indisponivel")
            else:
                print(f"Bombom - Preço: R${precoP5:.2f}")
                prod5 -= 1
                precoProdutoEscolhido = precoP5

        valorPago = recebePagamento(precoProdutoEscolhido)
        print(f"Valor pago: R${valorPago:.2f}")
        trocoCliente = round(valorPago - precoProdutoEscolhido, 2)
        if trocoCliente != 0:
            print(f"Troco: R${trocoCliente:.2f}")
            devolveTroco(trocoCliente)
        else:
            print("Não existe troco!")
    else:
        print("Produto inexistente.")
    outro = input("Deseja escolher outro produto? ")  # S/N
    if outro == "S" or outro == "s":
        return maquina(prod1, prod2, prod3, prod4, prod5)
    else:
        exit()


maquina(5,5,5,5,5)
