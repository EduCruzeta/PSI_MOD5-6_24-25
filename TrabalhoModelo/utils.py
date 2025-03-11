def ler_numero_inteiro(mensagem="Introduza um valor inteiro: ") -> int:
    """
    Função que lê do utilizador um nº inteiro. A função garante que o valor inserido é um valor válido.
    """
    while True:
        dados = input(mensagem)
        if len(dados)==0:
            continue
        # verificar se existe um - no inicio da str (valor negativo)
        if dados[0] == '-':
            testar = dados.replace('-','')
        else:
            testar = dados
        if testar.isdigit():
            return int(dados)
        print("Erro: o valor inserido não é válido.")

def ler_numero_inteiro_limites(valor_min,valor_max=None, mensagem="Introduza um valor inteiro: ") -> int:
    """
    Função que recebe o valor minimo e máximo a ler do utilizador. A função devolve o valor quando é um inteiro válido.
    """
    while True:
        numero = ler_numero_inteiro(mensagem)
        if numero >= valor_min and (valor_max is None or numero <= valor_max ):
            return numero
        print("Erro: O valor não é válido.")

def ler_numero_decimal(mensagem="Introduza um valor decimal: ") -> float:
    """
    Função para ler um nº decimal. A função garante que o valor é válido e aceita como separador das casas decimais . ou ,
    """
    while True:
        dados = input(mensagem)
        if len(dados)==0:
            continue
        # substituir as virgulas por pontos
        dados = dados.replace(',','.')
        # verificar se existe um - no inicio da str (valor negativo)
        if dados[0] == '-':
            testar = dados.replace('-','')
        else:
            testar = dados
        # contar os pontos decimais
        pontos = testar.count('.')
        # remover os pontos decimais
        testar = testar.replace('.','')
        # não pode ter mais do que 1 ponto decimal e só pode ter digitos
        if testar.isdigit() and pontos<=1:
            return float(dados)
        print("Erro: O valor inserido não é válido.")

def ler_numero_decimal_limites(valor_min,valor_max=None,mensagem="Introduza um valor: ") -> float:
    """
    Função para ler um valor decimal dentro de limites. Função garante a validade do valor.
    """
    while True:
        valor = ler_numero_decimal(mensagem)
        if valor >= valor_min and (valor_max is None or valor <= valor_max):
            return valor
        print("Erro: valor não é válido")

def Menu(opcoes,titulo=""):
    """Função recebe as opções a mostrar de um menu. Lê a opção do utilizar e se for válida devolve essa opção"""
    #mostrar o título do menu
    if titulo!="":
        print(titulo)
    #mostrar as opções com um nº ao lado
    for i in range(len(opcoes)):
        print(f"{i+1}.{opcoes[i]}")
    #ler a opção do utilizador
    op = ler_numero_inteiro_limites(1,len(opcoes),"Opção:")
    #se for válida devolvemos a opção escolhida
    return op

def Media(valores):
    """Devolve a média dos valores de um tuple ou list"""
    return sum(valores)/len(valores)