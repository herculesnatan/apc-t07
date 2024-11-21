
entrada = str(input("O programa funciona?\n"))

if entrada == "SIM":
    caso_1 = input("Você entende o que fez?\n")
    if caso_1 == "SIM":
        print("Ótimo. Então não mexe!")
    else:
        caso_2 = input("Já foi na tutoria?\n")
        if caso_2 == "SIM":
            print("Choremos!")
        else: 
            print("Temos um time a disposição!")
else:
    erro = input("Você sabe onde está o erro?\n")
    if erro == "SIM":
        solucionar_sozinho = input("Acha que pode solucionar sozinho?\n")
        if solucionar_sozinho == "SIM":
            print("Então mão na massa!")
        else: 
            pesquisa_google = input("Já pesquisou no Google?\n")
            if pesquisa_google == "SIM":
                caso_2 = input("Já foi na tutoria?\n")
                if caso_2 == "SIM":
                    print("Choremos!")
                else: 
                    print("Temos um time a disposição!")
            else:
                print("Corre lá então!")
    else:
        caso_2 = input("Já foi na tutoria?\n")
        if caso_2 == "SIM":
            print("Choremos!")
        else: 
            print("Temos um time a disposição!")