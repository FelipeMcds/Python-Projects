print("**************Calculadora**************"'\n')
print("Selecione o número da operação desejada:"'\n\n''1 - Adição\n''2 - Subtração\n''3 - Multiplicação\n''4 - Divisão\n')
seletor = int(input("Digite a opção desejada (1/2/3/4): "))

while (seletor !=1 and seletor !=2 and seletor !=3 and seletor !=4):
    print("Opção inválida")
    seletor = int(input("Digite a opção desejada (1/2/3/4): "))

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

if(seletor==1):
    print(f'{num1} + {num2} = {num1+num2}')
elif(seletor==2):
    print(f'{num1} - {num2} = {num1-num2}')
elif(seletor==3):
    print(f'{num1} x {num2} = {num1*num2}')
elif(seletor==4):
    print(f'{num1} / {num2} = {num1/num2}')

print("Fim!")
