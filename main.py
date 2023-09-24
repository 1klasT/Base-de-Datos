# %%
from rpg import *

habilidad_1 = Habilidad("Ataque Fuego", 20, 15)
habilidad_2 = Habilidad("Golpe Crítico", 30, 20)
habilidad_3 = Habilidad("Defensa", 0, 10)

objeto_1 = Objeto("Espada", "Una espada afilada", 50)
objeto_2 = Objeto("Armadura", "Es pesada, pero te protegerá", 75)

pocion_salud = Pocion("Poción de Salud", "Recupera 10 puntos de salud", "salud", 1, 10)
pocion_energia = Pocion("Poción de Energía", "Recupera 5 puntos de energía", "energia", 1, 10)

jugador_1 = Personaje("klasT", 100, 50, 15, 10, [habilidad_1], 100, 1, 0)
jugador_2 = Personaje("Nico", 80, 60, 10, 15, [habilidad_2, habilidad_3], 150, 1, 0)

enemigo_1 = Enemigo("Lobo", 80, 40, 12, 5, 50, 20, objeto_1)
enemigo_2 = Enemigo("León", 60, 30, 10, 8, 40, 15, objeto_2)

tienda = Tienda()
tienda.agregar_objeto(objeto_1)
tienda.agregar_objeto(objeto_2)
tienda.agregar_pocion(pocion_salud)
tienda.agregar_pocion(pocion_energia)

jugador_1.aprender_habilidad(habilidad_2)

tienda.vender_objeto(jugador_1, objeto_1)

jugador_2.derrotar_enemigo(enemigo_1)

jugador_2.recibir_experiencia(150)

jugador_1.usar_pocion(pocion_salud)

tienda.vender_pocion(jugador_2, pocion_energia)

jugador_1.descansar()

jugador_1.listar_objetos()

jugador_1.olvidar_habilidad(habilidad_3)