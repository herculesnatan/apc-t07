def nota(estrelinha):
    estrelinha_vazia = "☆" * (10 - estrelinha)
    estrelinha_cheia = "★" * estrelinha

    resultado = f"|{estrelinha_cheia}{estrelinha_vazia}|"
    print(resultado)
