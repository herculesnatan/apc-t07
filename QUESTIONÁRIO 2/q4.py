hora, minuto, segundo = map(int, input().split(":"))
valor_h = 3600
valor_m = 60
conta = (hora * valor_h) + (minuto * valor_m) + segundo
print(f"La se foram %i segundos que nao voltam mais..."%conta)