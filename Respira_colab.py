# Versão simplificada para rodar no Google Colab

import unicodedata

def remover_acentos(texto):
    return ''.join(c for c in unicodedata.normalize('NFD', texto)
                   if unicodedata.category(c) != 'Mn')

print("Como você está se sentindo hoje?")
print("Digite: cansado, estressado, ansioso ou outro sentimento.")
sentimento = input(">>> ")


sentimento = remover_acentos(sentimento.strip().lower())

if sentimento in ["cansado", "estressado", "ansioso"]:
    print("Entendo. Que tal uma pausa para respirar profundamente por um minuto?")
else:
    print("Ótimo! Continue se cuidando e lembre-se de fazer pausas regulares.")