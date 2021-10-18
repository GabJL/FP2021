operando1 = float(input("Dime el primer operando: "))
operando2 = float(input("Dime el segundo operando: "))
operación = input("Dime qué operación hacer: ")

if operación == "+":
    resultado = operando1+operando2
elif operación == "-":
    resultado = operando1-operando2
elif operación == "*":
    resultado = operando1+operando2
elif operación == "/":
    if operando2 == 0:
        resultado = "ERROR"
    else:
        resultado = operando1/operando2
else:
    resultado = "ERROR"
    
if resultado == "ERROR":
    print("Se produjo un error")
else:
    print(operando1, operación, operando2, "=", resultado)
