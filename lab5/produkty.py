def analiza_produktow(produkty):
  lista_produktow = [
      {"nazwa": nazwa, "cena": cena} for nazwa, cena in produkty.items()
  ]

  produkty_filtr = [p for p in lista_produktow if p["cena"] > 100]
  produkty_sort = sorted(produkty_filtr, key=lambda x: x["cena"], reverse=True)

  produkty_rabat = []
  for p in produkty_sort:
    nowy_produkt = {
        "nazwa": p["nazwa"].upper(),
        "cena": round(p["cena"] * 0.9, 2),
    }

    produkty_rabat.append(nowy_produkt)

  return produkty_rabat