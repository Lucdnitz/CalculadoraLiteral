def verEquacao(equacao):
    equacao = list(equacao)
    equacaoFim = []
    numero = []
    num = True
    try:
        for i in range(len(equacao)):
            if num:
                if equacao[i]=='-' and i==0:
                    numero.append('-')
                else:
                    numero.append(str(int(equacao[i])))
                    num=False
            else:
                if equacao[i] not in ['+','-','*','/','.'] or i == len(equacao)-1:
                    numero.append(str(int(equacao[i])))
                elif equacao[i]=='.':
                    numero.append(equacao[i])
                else:
                    equacaoFim.append(float(''.join(numero)))
                    equacaoFim.append(equacao[i])
                    numero=[]
                    num=True
        
        equacaoFim.append(float(''.join(numero)))

    except:
        return 0
    return equacaoFim

def console():
    console = '''
----------------------------------------------------------
Digite o número correspondente (0 ou 1):
0 - Sair
1 - Realizar alguma operação
----------------------------------------------------------
'''
    try:
        calcConsole = int(input(console))
        if calcConsole not in [0,1]:
            print('Número inválido. Encerrando programa...')
            calcConsole=0
    except:
        calcConsole=0
        print('Caractere inválido. Encerrando programa...')
    return calcConsole

def calculo(equacao):
    passo = 1
    string_equacao = [str(equacao[j]) for j in range(len(equacao)) if type(equacao[j])==float or type(equacao[j])==str]
    print(f'\nResolução da equação "{"".join(string_equacao)}":')
    if len(equacao)==1:
        string_equacao = [str(equacao[i]) for i in range(len(equacao)) if type(equacao[i])==float]
        print(f"{passo}° passo: {''.join(string_equacao)}")
    else:
        teste = True
        while teste:
            teste= False
            for i in range(len(equacao)):
                if equacao[i]=='*':
                    equacao.insert(i-1, equacao[i-1]*equacao[i+1])
                    for j in range(3):
                        equacao.pop(i)
                    teste = True
                    string_equacao = [str(equacao[j]) for j in range(len(equacao)) if type(equacao[j])==float or type(equacao[j])==str]
                    print(f"{passo}° passo: {''.join(string_equacao)}")
                    passo+=1
                    break
                elif equacao[i]=='/':
                    equacao.insert(i-1, equacao[i-1]/equacao[i+1])
                    for j in range(3):
                        equacao.pop(i)
                    teste = True
                    string_equacao = [str(equacao[j]) for j in range(len(equacao)) if type(equacao[j])==float or type(equacao[j])==str]
                    print(f"{passo}° passo: {''.join(string_equacao)}")
                    passo+=1
                    break
        
        teste = True
        while teste:
            teste= False
            for i in range(len(equacao)):
                if equacao[i]=='+':
                    equacao.insert(i-1, equacao[i-1]+equacao[i+1])
                    for j in range(3):
                        equacao.pop(i)
                    teste = True
                    string_equacao = [str(equacao[j]) for j in range(len(equacao)) if type(equacao[j])==float or type(equacao[j])==str]
                    print(f"{passo}° passo: {''.join(string_equacao)}")
                    passo+=1
                    break
                elif equacao[i]=='-':
                    equacao.insert(i-1, equacao[i-1]-equacao[i+1])
                    for j in range(3):
                        equacao.pop(i)
                    teste = True
                    string_equacao = [str(equacao[j]) for j in range(len(equacao)) if type(equacao[j])==float or type(equacao[j])==str]
                    print(f"{passo}° passo: {''.join(string_equacao)}")
                    passo+=1
                    break

calcConsole = console()

while(calcConsole):
    conta = input('\n----------------------------------------------------------\nDigite a equação (operações permitidas: *,/,+,-):\nExemplo: 10*20.2+10.8*2\n----------------------------------------------------------\n')
    conta = verEquacao(conta)
    if conta == 0:
        print('\nErro: foi inserido uma formatação errada da equação.')
    else:
        calculo(conta)
    calcConsole = console()
