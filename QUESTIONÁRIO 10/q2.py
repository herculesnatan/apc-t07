n = int(input())
aluno = {}
alunos_mesma_nota = []
for _ in range(n):
    nome, nota = input().split(",")
    aluno[nome.strip()] = float(nota.strip())
nota_escolhida = float(input())

for key, value in aluno.items():
    if value == nota_escolhida:
        alunos_mesma_nota.append(key)

if len(alunos_mesma_nota) > 0:
    print("/".join(sorted(alunos_mesma_nota)))
else:
    print("Você foi o único aluno com essa nota.")
