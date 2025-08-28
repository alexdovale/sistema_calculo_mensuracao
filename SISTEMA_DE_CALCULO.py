# -*- coding: utf-8 -*-

# Constante baseada no Manual de Gestão Documental
LARGURA_CAIXA_ARQUIVO_CM = 13.5


def adicionar_medicao_caixas():
    """
    Calcula a metragem para um conjunto de prateleiras e retorna os valores.
    """
    total_caixas_adicionar = 0
    total_medida_cm_adicionar = 0.0

    while True:
        entrada_prateleiras = input("\nInforme o número de prateleiras para ESTA medição (ou 'fim' para cancelar): ")
        if entrada_prateleiras.lower() == 'fim':
            return None, None  # Retorna None para indicar cancelamento

        try:
            num_prateleiras = int(entrada_prateleiras)
            if num_prateleiras > 0:
                break
            else:
                print("Por favor, insira um número maior que zero.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número inteiro.")

    for i in range(1, num_prateleiras + 1):
        while True:
            entrada_caixas = input(f" - Quantas caixas há na prateleira {i}? (ou 'fim' para cancelar) ")
            if entrada_caixas.lower() == 'fim':
                return None, None  # Retorna None para indicar cancelamento

            try:
                num_caixas_prateleira = int(entrada_caixas)
                if num_caixas_prateleira >= 0:
                    medida_prateleira_cm = num_caixas_prateleira * LARGURA_CAIXA_ARQUIVO_CM
                    print(
                        f"   -> Cálculo da prateleira {i}: {num_caixas_prateleira} caixas * {LARGURA_CAIXA_ARQUIVO_CM} cm = {medida_prateleira_cm:.2f} cm")
                    total_caixas_adicionar += num_caixas_prateleira
                    total_medida_cm_adicionar += medida_prateleira_cm
                    break
                else:
                    print("O número de caixas não pode ser negativo.")
            except ValueError:
                print("Entrada inválida. Por favor, digite um número inteiro.")

    medida_m = total_medida_cm_adicionar / 100
    return medida_m, total_caixas_adicionar


def adicionar_medicao_pilhas():
    """
    Calcula a metragem para um conjunto de pilhas e retorna os valores.
    """
    total_altura_cm_adicionar = 0.0
    contador_pilha = 1

    print("\nInforme a altura de cada pilha em cm para ESTA medição.")
    print("Digite 'fim' quando terminar de adicionar as pilhas.")

    while True:
        entrada = input(f" - Altura da pilha {contador_pilha} (cm): ")
        if entrada.lower() == 'fim':
            break

        try:
            altura_pilha = float(entrada)
            if altura_pilha >= 0:
                total_altura_cm_adicionar += altura_pilha
                contador_pilha += 1
                print(f"   -> Subtotal atual desta medição: {total_altura_cm_adicionar:.2f} cm")
            else:
                print("A altura não pode ser um valor negativo.")
        except ValueError:
            print("Entrada inválida. Por favor, digite um número (ex: 40.5) ou 'fim' para parar.")

    if total_altura_cm_adicionar > 0:
        medida_m = total_altura_cm_adicionar / 100
        return medida_m, contador_pilha - 1
    return 0, 0


def iniciar_sessao_calculo():
    """
    Gerencia uma sessão de cálculo, acumulando valores até o usuário finalizar.
    """
    total_metros_caixas = 0.0
    total_metros_pilhas = 0.0
    total_caixas = 0
    total_pilhas = 0

    print("\n--- Iniciando Cálculo ---")

    while True:
        print("\nO que você deseja adicionar ao cálculo?")
        print("1 - Caixas (em estantes/prateleiras)")
        print("2 - Pilhas de documentos")
        escolha = input("Escolha uma opção: ")

        if escolha == '1':
            medida_m, caixas = adicionar_medicao_caixas()
            if medida_m is not None:
                total_metros_caixas += medida_m
                total_caixas += caixas
                print(f"\nAdicionado: {medida_m:.2f} m e {caixas} caixas.")
            else:
                print("Adição de caixas cancelada.")

        elif escolha == '2':
            medida_m, pilhas = adicionar_medicao_pilhas()
            if medida_m > 0:
                total_metros_pilhas += medida_m
                total_pilhas += pilhas
                print(f"\nAdicionado: {medida_m:.2f} m e {pilhas} pilhas.")
            else:
                print("Nenhuma pilha adicionada nesta medição.")
        else:
            print("\nOpção inválida! Por favor, escolha 1 ou 2.")

        # Pergunta se deseja continuar
        while True:
            resposta = input("\nDeseja adicionar mais no cálculo? (sim/não): ")
            if resposta.lower() in ['sim', 'não', 'nao']:
                break
            else:
                print("\nResposta inválida. Por favor, digite 'sim' ou 'não'.")

        if resposta.lower() == 'não' or resposta.lower() == 'nao':
            break

    # Exibe o resultado final da sessão
    total_geral_metros = total_metros_caixas + total_metros_pilhas
    print("\n=============================================")
    print("--- RESULTADO FINAL DA SESSÃO ---")
    print(f"\nDetalhes do Acondicionamento:")
    print(f"- Total de caixas contabilizadas: {total_caixas} ({total_metros_caixas:.2f} metros lineares)")
    print(f"- Total de pilhas contabilizadas: {total_pilhas} ({total_metros_pilhas:.2f} metros lineares)")
    print("\n---")
    print(f"Medida total do acervo: {total_geral_metros:.2f} metros lineares.")
    print("=============================================")
    if total_geral_metros > 0:
        print("\n*** INSTRUÇÃO ***")
        print(
            f"Lembre-se de adicionar o valor em metros lineares ({total_geral_metros:.2f} m) no campo 'Mensuração Total' da sua Listagem de Eliminação de Documentos.")


def menu_principal():
    """
    Exibe o menu principal e direciona o fluxo do programa.
    """
    print("=============================================")
    print("   Calculadora de Metragem de Acervo Documental   ")
    print("=============================================")

    while True:
        print("\nMENU PRINCIPAL")
        print("1 - Iniciar cálculo")
        print("2 - Sair")

        escolha = input("Escolha uma opção (1 ou 2): ")

        if escolha == '1':
            iniciar_sessao_calculo()
        elif escolha == '2':
            print("\nPrograma finalizado.")
            break
        else:
            print("\nOpção inválida! Por favor, escolha 1 ou 2.")


# Inicia o programa
if __name__ == "__main__":
    menu_principal()