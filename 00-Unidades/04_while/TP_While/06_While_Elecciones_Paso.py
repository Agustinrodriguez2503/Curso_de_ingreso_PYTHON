import tkinter
from tkinter.messagebox import showinfo as alert
from tkinter.messagebox import askyesno as question
from tkinter.simpledialog import askstring as prompt
import customtkinter

'''
nombre: agustin 
apellido: rodriguez
---
TP: While_elecciones_paso
---
Enunciado:
De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
Informar: 
a. nombre del candidato con más votos
b. nombre y edad del candidato con menos votos
c. el promedio de edades de los candidatos
d. total de votos emitidos.
Todos los datos se ingresan por prompt y los resultados por alert

'''

class App(customtkinter.CTk):

    def __init__(self):
        super().__init__()

        # configure window
        self.title("UTN Fra")

        self.btn_validar = customtkinter.CTkButton(
            master=self, text="Validar", command=self.btn_validar_on_click)
        self.btn_validar.grid(row=4, pady=20, columnspan=2, sticky="nsew")

    def btn_validar_on_click(self):
        bandera = True
        candidato_mas_votado = 0
        edad_candidato_menos_votado = 0
        contador_edad = 0
        acumulador_edad = 0
        acumulador_votos = 0
        contador_votos = 0
        
        while True:
            nombre = prompt("Nombre" , "Ingrese un nombre.")
            if nombre == None:
                break
            edad = prompt("Edad" , "Ingrese la edad de " + nombre)
            edad = int(edad)
            if (edad >= 25):
                contador_edad += 1
                acumulador_edad += edad
            if edad == None:
                break
            while (edad < 25):
                edad = prompt("Edad" , "Reingrese la edad de " + nombre + ", ésta debe ser mayor a 25 años.")
                edad = int(edad)
            votos = prompt("Votos" , "Ingrese la cantidad de votos que obtuvo " + nombre)
            votos = int(votos)
            if (votos > 0):
                acumulador_votos += votos
            #if(bandera or votos < minimo):
                #minimo = votos
                #edad_candidato_menos_votado = minimo
            if (votos == None):
                break
            while(votos < 0):
                votos = prompt("Votos" , "Reingrese la cantidad de votos que obtuvo " + nombre + ", ésta debe ser mayor a 0 votos.")
                votos = int(votos)
        
        promedio_edad = acumulador_edad/ contador_edad
        mensaje = f"El nombre del candidato con menos votos es: y tiene {edad_candidato_menos_votado} años. \nEl promedio de edades de los candidatos es: {promedio_edad}. \nEl total de votos emitidos fue: {acumulador_votos}"
        alert("PASO", mensaje)






#De los candidatos a las paso del mes de Octubre (no sabemos cuantos), se registra:
#nombre, la edad (mayor 25) y la cantidad de votos (no menor a cero) que recibio en las elecciones.
#Informar: 
#a. nombre del candidato con más votos
#b. nombre y edad del candidato con menos votos
#c. el promedio de edades de los candidatos
#d. total de votos emitidos.
#Todos los datos se ingresan por prompt y los resultados por alert

if __name__ == "__main__":
    app = App()
    app.geometry("300x300")
    app.mainloop()
