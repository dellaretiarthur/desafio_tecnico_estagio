""" 
escreva um programa que verifique, em uma string, a existência da letra "a", seja maiuscula ou minuscula, além de informar a quantidade de vezes em que ela ocorre
 """

def verificar_letra_a():
    palavra = input("Digite uma palavra: ").lower()
    contador = 0 
    for letra in palavra:
        if letra == "a":
            contador += 1
    print(f"A letra 'a' aparece {contador} vezes na palavra '{palavra}'")


verificar_letra_a()


