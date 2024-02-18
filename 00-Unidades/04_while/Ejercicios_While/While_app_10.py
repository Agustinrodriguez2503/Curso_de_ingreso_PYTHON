import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: agustin
apellido: rodriguez
tutor: marina/albana
---
Ejercicio: while_10
---
Enunciado:
Al presionar el botón ‘Comenzar ingreso’, solicitar mediante prompt todos los números que el usuario 
quiera hasta que presione el botón Cancelar (en el prompt). 
Luego calcular:
    A. La suma acumulada de los negativos
    B. La suma acumulada de los positivos
    C. Cantidad de números positivos ingresados
    D. Cantidad de números negativos ingresados
    E. Cantidad de ceros
    F. Diferencia entre la cantidad de los números positivos ingresados y los negativos

Informar los resultados mediante alert()

'''

class App(customtkinter.CTk):
    
    def __init__(self):
        super().__init__()

        self.title("UTN FRA")
    
        self.btn_mostrar = customtkinter.CTkButton(master=self, text="Comenzar Ingreso", command=self.btn_comenzar_ingreso_on_click)
        self.btn_mostrar.grid(row=2, padx=20, pady=20, columnspan=2, sticky="nsew")


    def btn_comenzar_ingreso_on_click(self):
        suma_negativos = 0
        suma_positivos = 0
        cantidad_positivos = 0
        cantidad_negativos = 0
        cantidad_ceros = 0
        diferencia = 0

        while True:
            numero = prompt("Datos" , "Ingrese un numero")
            
            if numero == None:
                break
            numero = int(numero)

            if (numero < 0):
                suma_negativos += numero
                cantidad_negativos += 1
            elif (numero > 0):
                suma_positivos += numero
                cantidad_positivos += 1
            elif (numero == 0):
                cantidad_ceros += 1
        diferencia = cantidad_positivos - cantidad_negativos
        mensaje = "La suma de los numeros negativos es {0} y se ingresaron {1} numeros negativos. \nLa suma de los numeros positivos es {2} y se ingresaron {3} numeros positivos. \nSe ingresaron {4} ceros. \nLa diferencia entre la cantidad de numeros positivos y la cantidad de numeros negativos es: {5}".format(suma_negativos,cantidad_negativos,suma_positivos,cantidad_positivos,cantidad_ceros,diferencia)
        alert("UTN" , mensaje)

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
