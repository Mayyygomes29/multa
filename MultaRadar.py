#Calcula a multa mediante os km ultrapassados
vel = int(input("Digite a velocidade do carro: KM "))
if vel >= 80:
    print("O carro foi multado! Com isso irá pagar {:.2f} de multa".format((vel -79)*7))

print("Tenha um bom dia e dirija com segurança!")    