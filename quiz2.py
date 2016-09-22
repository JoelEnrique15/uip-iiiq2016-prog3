#quiz2

print("convercion de monedad")

"""
Dolar: 1USD
EUR: 1USD =0.8965 EUR
YEN: 1USD =101.5744 YEN
BP: 1USD = 0.7702 BP
MXN: 1USD = 19.7843
"""
print("Introduce la cantidad de monedas que deseas convertir ")
i= int(input("valor monetario en centavos:"))
Dolar= i/100
print(str(Dolar) + "dolares")

EUR= Dolar*0.8965
print(str(EUR)+ "Euros")

YEN= Dolar*101.5744
print(str(YEN)+ "Yenes")

BP= Dolar*0.7702
print(str(BP)+ "Libras Britanicas")

MXN= Dolar*19.7843
print(str(MXN) + "pesos mexicanos")
