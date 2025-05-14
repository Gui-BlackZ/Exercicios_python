import random
 
 
comidas = ["Lasanha","Torta Holandesa","Pizza","Croissant","Sushi","Estrogonofe","Batata-Frita","Ovo","Hamburguer","Macarrão","Milho","Frango","Linguiça","EasterEgg"]
pratos = random.choice(comidas).lower()
print(pratos)
limite_de_tentativas = 5
chances = 1
 
#----------------------
for prato in comidas:
    print(prato)
    print(18*"=")
#----------------------
 
while chances+1:
    print(f"Tentativas: ({chances} de {limite_de_tentativas}) ")
    palpite = str(input("\nPor favor, escolha seu prato: ").lower())
 
 
    if limite_de_tentativas == chances:
        print(f"\nSuas tentativas acabaram!!😢\nSeu Prato_Secreto era: {pratos}")
        break
    else:
 
        if palpite == pratos:
            print("Você Acertou✔✔! ✨Bela jogada✨")
            break
        else:
            print(f"😢Você Errou❌❌!")
        chances += 1