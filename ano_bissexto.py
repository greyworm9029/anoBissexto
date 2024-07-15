# Verifica se um ano é bissexto ou nao
def anoBissexto():
  ano = int(input("Digite um ano: "))
  

  # Forma simples
  """
  if ano % 4 == 0:
    if ano % 100 == 0:
      if ano % 400 == 0:
        print(f"{ano} é um ano bissexto.")
      else:
        print(f"{ano} nao é um ano bissexto.")
    else:
      print(f"{ano} é um ano bissexto.")
  else:
    print(f"{ano} nao é um ano bissexto.")
    """

    
  # Usando operador ternário para verificar se o ano é bissexto
  resultado = (
  f"{ano} é um ano bissexto." if (ano % 4 == 0 and ano % 100 != 0) or (ano % 400 == 0)
    else f"{ano} não é um ano bissexto."
    )
    
  print(resultado)

anoBissexto()
