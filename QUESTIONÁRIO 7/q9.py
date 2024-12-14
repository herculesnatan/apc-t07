def não_possui_a_letra_u(palavra):
    for letra in palavra:
        if letra.lower() in"uúüûù":
            return False
    return True

print(não_possui_a_letra_u("Universidade"))
print(não_possui_a_letra_u("sükûnet"))
print(não_possui_a_letra_u("Baú"))
print(não_possui_a_letra_u("ù"))
print(não_possui_a_letra_u("Úrsula"))
print(não_possui_a_letra_u('Latex'))
print(não_possui_a_letra_u(""))
print(não_possui_a_letra_u('Litro'))    