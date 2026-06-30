""" Programa Python para entrar com o cadastro de aluno, fazer 4 provas e acessar
a média aritmética e mostrar a situação do aluno"""

print('+==== SISTEMA ACADÊMICO DE NOTAS ====+')

nome_prof = input('Informe o seu nome: ')
cndb = input(f'Professor(a) {nome_prof}, informe o seu CNDB: ') # Carteira Nacional Docente do Brasil (CNDB)
materia = input(f'Professor(a) {nome_prof}, informe o nome da sua disciplina: ')

notas = []
nome_aluno = ''
media = 0.0

print(f'Seja bem vindo(a), professor(a) {nome_prof} (CNDB: {cndb}) de {materia}!')

while True:
    print('''
          +==== SISTEMA ACADÊMICO DE NOTAS ====+
          [1] Dar notas ao(a) aluno(a)
          [2] Calcular a média do(a) aluno(a)
          [3] Visualizar a média do(a) aluno(a)
          [0] Sair do sistema''')
    opcao = int(input('Digite a opção escolhida: ').strip())
    
    if opcao == 1:
        nome_aluno = input('Informe o nome do(a) aluno(a): ')
        rm = float(input('Informe o RM do(a) aluno(a): ').strip())
        notas.clear()
        
        while len(notas) < 4:
            nota = float(input(f'Digite a {len(notas) + 1}° nota do(a) aluno(a) - até a 4° nota: ').strip())
            
            if 0 <= nota <= 10:
                notas.append(nota)
                print(f'Nota {nota} adicionada ao(a) aluno(a) {nome_aluno}.')
                print(f'Notas do(a) aluno(a) {nome_aluno}: {notas}')
            else:
                print('Nota inválida. Digite uma nova entre 0 e 10.')
                
        print(f'Notas do(a) aluno(a) {nome_aluno}: {notas}')
        
    elif opcao == 2:
        if len(notas) > 0:
            media = sum(notas) / len(notas)
            print(f'A média aritmética do(a) aluno(a) {nome_aluno} é de : {media}')
        
        else:
            print('ERRO: Não há nenhuma nota cadastrada. Cadastre primeiro uma nota.')
    
    elif opcao == 3:
        if nome_aluno == '':
            print('Erro: nenhum aluno cadastrado.')
        elif media == 0.0:
            print('Erro: a média não foi cadastrada.')
        else:
            situacao = 'APROVADO(A)!' if media >= 6 else 'REPROVADO(A)!'
            
            print('+--------------------------+')
            print(f'Aluno: {nome_aluno}')
            print(f'Média: {media:.2f}')
            print(f'Situação: {situacao}')
            print('+--------------------------+')
    
    elif opcao == 0:
        print(f'Encerrando o sistema. Obrigado professor(a) {nome_prof}!')
        break
    
    else:
        print('Opção inválida. Tente novamente:')