import random
 
class Entidad:
    def __init__(self, nombre, salud, energia, ataque_basico, probabilidad_critico):
        self.nombre = nombre
        self.salud = salud
        self.energia = energia
        self.salud_maxima = salud
        self.energia_maxima = energia
        self.ataque_basico = ataque_basico
        self.probabilidad_critico = probabilidad_critico

    def atacar(self, objetivo):
        if self.salud <= 0:
            print(f"{self.nombre} no puede atacar porque no tiene salud.")
            return

        multiplicador = 2 if random.randint(1, 100) <= self.probabilidad_critico else 1

        dano = self.ataque_basico * multiplicador
        objetivo.recibir_dano(dano)

        print(f"{self.nombre} lanzo un ataque a {objetivo.nombre} por {dano} de daño.")

    def recibir_dano(self, cantidad_dano):
        self.salud -= cantidad_dano
        if self.salud <= 0:
            print(f"{self.nombre} ha sido aniquilado.")
            self.salud = 0
        else:
            print(f"{self.nombre} ha recibido {cantidad_dano} puntos de daño. Salud restante: {self.salud}")

    def usar_habilidad(self, habilidad, objetivo):
        if self.salud <= 0:
            print(f"{self.nombre} no puede usar habilidades porque no tiene salud.")
            return

        if self.energia >= habilidad.energia_requerida:
            print(f"{self.nombre} usa la habilidad {habilidad.nombre} contra {objetivo.nombre}.")
            objetivo.recibir_dano(habilidad.ataque)
            self.energia -= habilidad.energia_requerida
        else:
            print(f"{self.nombre} no tiene suficiente energía para usar la habilidad {habilidad.nombre}.")

    def descansar(self):
        if self.salud <= 0:
            print(f"{self.nombre} no puede descansar porque está sin salud.")
            return

        salud_recuperada = self.salud_maxima * 0.15
        energia_recuperada = self.energia_maxima * 0.15

        self.salud += salud_recuperada
        self.energia += energia_recuperada

        if self.salud > self.salud_maxima:
            self.salud = self.salud_maxima

        if self.energia > self.energia_maxima:
            self.energia = self.energia_maxima

        print(f"{self.nombre} ha descansado y recuperado un 15% de su salud y energía.")

class Personaje(Entidad):
    def __init__(self, nombre, salud, energia, ataque_basico, probabilidad_critico, habilidades=[], dinero=0, nivel = 1, experiencia = 0):
        super().__init__(nombre, salud, energia, ataque_basico, probabilidad_critico)
        self.habilidades = habilidades
        self.inventario = []
        self.dinero = dinero
        self.nivel = nivel
        self.experiencia = experiencia

    def aprender_habilidad(self, habilidad):
        if len(self.habilidades) < 3:
            self.habilidades.append(habilidad)
            print(f"{self.nombre} aprendio la habilidad {habilidad.nombre}")
        else:
            print(f"{self.nombre} ya cuenta con 3 habilidades y no puede aprender más.")

    def olvidar_habilidad(self, habilidad_a_olvidar):
        if habilidad_a_olvidar in self.habilidades:
            self.habilidades.remove(habilidad_a_olvidar)
            print(f"{self.nombre} ha olvidado la habilidad {habilidad_a_olvidar.nombre}")
        else:
            print(f"{self.nombre} no posee la habilidad {habilidad_a_olvidar.nombre} para olvidarla.")

    def recibir_experiencia(self, cantidad):
        self.experiencia += cantidad
        print(f"{self.nombre} ha ganado {cantidad} puntos de experiencia.")

        if self.experiencia >= 100 * self.nivel:
            self.subir_nivel()
            self.aumentar_atributos()

    def subir_nivel(self):
        self.nivel += 1
        self.experiencia = 0
        print(f"{self.nombre} ha subido al nivel {self.nivel}!")

    def aumentar_atributos(self):
        self.salud_maxima += 10
        self.energia_maxima += 5
        self.ataque_basico += 2
        print(f"{self.nombre} ha aumentado sus atributos al subir de nivel.")

    def agregar_objeto(self, objeto):
        if len(self.inventario) < 10:
            self.inventario.append(objeto)
            print(f"{self.nombre} ha recogido {objeto.nombre}.")
        else:
            print(f"{self.nombre} no puede llevar más objetos. El inventario está lleno.")

    def eliminar_objeto(self, objeto):
        if objeto in self.inventario:
            self.inventario.remove(objeto)
            print(f"{self.nombre} ha eliminado {objeto.nombre} del inventario.")
        else:
            print(f"{self.nombre} no tiene {objeto.nombre} en el inventario.")

    def listar_objetos(self):
        print(f"{self.nombre} tiene los siguientes objetos en el inventario:")
        for objeto in self.inventario:
            print(f"- {objeto.nombre}: {objeto.descripcion}")
    
    def usar_pocion(self, pocion):
        if isinstance(pocion, Pocion):
            if pocion in self.inventario:
                if pocion.tipo == "salud":
                    cantidad_curacion = pocion.nivel * 10
                    self.salud += cantidad_curacion
                    if self.salud > self.salud_maxima:
                        self.salud = self.salud_maxima
                    print(f"{self.nombre} ha usado una poción de salud y ha recuperado {cantidad_curacion} puntos de salud.")
                elif pocion.tipo == "energia":
                    cantidad_curacion = pocion.nivel * 5
                    self.energia += cantidad_curacion
                    if self.energia > self.energia_maxima:
                        self.energia = self.energia_maxima
                    print(f"{self.nombre} ha usado una poción de energía y ha recuperado {cantidad_curacion} puntos de energía.")
                else:
                    print(f"{self.nombre} no puede usar esa poción.")
            else:
                print(f"{self.nombre} no tiene {pocion.nombre} en el inventario.")
        else:
            print(f"{self.nombre} no puede usar ese objeto.")

    def derrotar_enemigo(self, enemigo):
        if len (self.inventario) < 10:
            self.inventario.append(enemigo.objeto_otorgado)
        self.experiencia += enemigo.experiencia_otorgada
        self.dinero += enemigo.dinero_otorgado
        print(f"{self.nombre} ha aniquilado a {enemigo.nombre} y ha ganado {enemigo.dinero_otorgado} monedas y {enemigo.experiencia_otorgada} de experiencia..")

class Enemigo(Entidad):
    def __init__(self, nombre, salud, energia, ataque_basico, probabilidad_critico, experiencia_otorgada, dinero_otorgado, objeto_otorgado):
        super().__init__(nombre, salud, energia, ataque_basico, probabilidad_critico)
        self.experiencia_otorgada = experiencia_otorgada
        self.dinero_otorgado = dinero_otorgado
        self.objeto_otorgado = objeto_otorgado

class Habilidad:
    def __init__(self, nombre, ataque, energia_requerida):
        self.nombre = nombre
        self.ataque = ataque
        self.energia_requerida = energia_requerida

class Objeto:
    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

class Pocion(Objeto):
    def __init__(self, nombre, descripcion, tipo, nivel, precio):
        super().__init__(nombre, descripcion, precio)
        self.tipo = tipo
        self.nivel = nivel

class Tienda:
    def __init__(self):
        self.inventario_objetos = []
        self.inventario_pociones = []

    def agregar_objeto(self, objeto):
        self.inventario_objetos.append(objeto)

    def agregar_pocion(self, pocion):
        self.inventario_pociones.append(pocion)

    def vender_objeto(self, personaje, objeto):
        if objeto in self.inventario_objetos and personaje.dinero >= objeto.precio:
            personaje.dinero -= objeto.precio
            personaje.agregar_objeto(objeto)
            self.inventario_objetos.remove(objeto)
            print(f"{personaje.nombre} ha comprado {objeto.nombre} por {objeto.precio} monedas.")
        else:
            print(f"{personaje.nombre} no posee las monedas suficiente para comprar {objeto.nombre}.")

    def vender_pocion(self, personaje, pocion):
        if pocion in self.inventario_pociones and personaje.dinero >= pocion.precio:
            personaje.dinero -= pocion.precio
            personaje.agregar_objeto(pocion)
            self.inventario_pociones.remove(pocion)
            print(f"{personaje.nombre} ha comprado {pocion.nombre} por {pocion.precio} monedas.")
        else:
            print(f"{personaje.nombre} no posee las monedas suficiente para comprar {pocion.nombre}.")