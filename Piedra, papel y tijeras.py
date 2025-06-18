# -*- coding: utf-8 -*-
"""
Created on Sat Jun 14 15:28:19 2025

@author: Steeven
"""

import random
import time

def mostrar_inicio():
    print("╔══════════════════════════════╗")
    print("║     PIEDRA, PAPEL O TIJERAS  ║")
    print("╚══════════════════════════════╝")
    print("Reglas:")
    print(" - Piedra gana a Tijeras")
    print(" - Tijeras gana a Papel")
    print(" - Papel gana a Piedra")
    print("¡Prepárate para jugar!\n")
    time.sleep(1)

def obtener_eleccion_usuario():
    opciones = ['piedra', 'papel', 'tijeras']
    eleccion = input("Elige piedra, papel o tijeras: ").lower()
    while eleccion not in opciones:
        eleccion = input("Opción no válida. Intenta con piedra, papel o tijeras: ").lower()
    return eleccion

def determinar_ganador(usuario, computadora):
    if usuario == computadora:
        return "empate"
    elif (
        (usuario == "piedra" and computadora == "tijeras") or
        (usuario == "papel" and computadora == "piedra") or
        (usuario == "tijeras" and computadora == "papel")
    ):
        return "usuario"
    else:
        return "computadora"

def jugar():
    mostrar_inicio()
    while True:
        usuario = obtener_eleccion_usuario()
        computadora = random.choice(['piedra', 'papel', 'tijeras'])

        print(f"\nTu elección: {usuario}")
        print(f"Elección de la computadora: {computadora}")
        resultado = determinar_ganador(usuario, computadora)

        if resultado == "empate":
            print("¡Es un empate! Vamos de nuevo...\n")
            time.sleep(1)
            continue
        elif resultado == "usuario":
            print("🎉 ¡Ganaste esta ronda!")
        else:
            print("😢 Perdiste esta ronda.")

        jugar_otra = input("\n¿Quieres jugar otra vez? (s/n): ").lower()
        if jugar_otra != 's':
            print("¡Gracias por jugar! Hasta la próxima.")
            break
        print("\n" + "="*30 + "\n")

# Inicia el juego
jugar()
