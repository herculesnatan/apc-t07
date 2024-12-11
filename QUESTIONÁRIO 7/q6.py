frase = input()
troca_na_frase = input()

def stop_word(palavra, troca="*"):
    nova_frase = frase.replace(palavra, troca)
    return nova_frase

if troca_na_frase in frase:
    chama_troca = stop_word(troca_na_frase)
    print(chama_troca)
else:
    print("tudo certo :)")
    