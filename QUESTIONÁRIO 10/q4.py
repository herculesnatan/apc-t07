turma = {}
n = int(input())

for _ in range(n):
    entrada = input().split()
    nome = entrada[0]
    email = entrada[1]
    notas = list(map(float, entrada[2:]))
    media = sum(notas) / len(notas)
    situacao = "aprovado" if media >= 5 else "reprovado"
    turma[nome] = {"email": email, "media": media, "situacao": situacao}


aluno_busca = input()


if aluno_busca in turma:
    aluno = turma[aluno_busca]
    print(f"Destinatário: {aluno['email']}")
    print(f"O aluno {aluno_busca} foi {aluno['situacao']} com média {aluno['media']:.2f}.")
else:
    print(f"O aluno {aluno_busca} não está na turma.")
