def paron(frase):
    frases_pares = []
    for i in frase:
        to_lower = i.lower()
        vogal_a, vogal_e, vogal_i, vogal_o, vogal_u = to_lower.count("a"),to_lower.count("e"), to_lower.count("i"), to_lower.count("o"), to_lower.count("u")
        total = vogal_a + vogal_e + vogal_i + vogal_o + vogal_u
        if total % 2 == 0:
            frases_pares.append(i)
    return frases_pares
        
        
print(paron(['palavra', 'escrever', 'detesta', 'lista', 'todas']))

print(paron(['Leandro', 'Maristela', 'Bruno', 'Ana', 'Edison', 'Lucas', 'Alexandre', 'Iago']))

print(paron(['Compor', 'MuSicas', 'PercuSsao', 'COMPLEXO', 'NoTas', 'MusicaIS', 'LA', 'Si', 'DO', 'RE']))