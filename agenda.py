#Escribir un programa que vaya solicitando al usuario que ingrese nombres.
#a) Si el nombre se encuentra en la agenda (implementada con un diccionario), debe mostrar
#el teléfono y, opcionalmente, permitir modificarlo si no es correcto.
#b) Si el nombre no se encuentra, debe permitir ingresar el teléfono correspondiente.
#El usuario puede utilizar la cadena ”*”, para salir del programa.

dict = {}
var = input("---BIENVENIDO AL PROGRAMA---\nIngrese un nombre (* para finalizar): ").upper()
while not var.isalpha() and var!="*":
    var = input("\nIngrese un nombre valido. (* para finalizar):" ).upper()


while(var!= "*"):
    if var in dict:
        while True:
            try:
                print("\nEl numero de {} es: {}".format(var, dict[var]))
                condicion = int(input("Desea cambiar el numero de celular de {}? 1--Si  2--No: ".format(var)))
                while(condicion!=1 and condicion!=2):
                    condicion = int(input("\nIngrese una opcion valida. Desea cambiar el numero de celular de {}? 1--Si  2--No: ".format(var)))
                if(condicion==1):
                    while True:
                        try:
                            dict[var] = int(input("\nIngrese numero de celular: "))
                            break
                        except ValueError:
                            print("\nValor invalido.")
                break                      
            except ValueError:
                    print("\nOpcion invalida!")

    else:
        while True:
            try:
                dict[var] = int(input("\nIngrese numero de celular: "))
                break
            except ValueError:
                dict[var] = input("\nValor invalido")
                continue
    
    var = input("\nIngrese otro nombre (* para finalizar): ").upper()
    while not var.isalpha() and var!="*":
        var = input("\nIngrese un nombre valido. (* para finalizar):" ).upper()

print("\nAGENDA\n")
print(dict)