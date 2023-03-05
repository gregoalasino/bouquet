class Venta:
    def __init__(self, nombre, importe):
        self.nombre = nombre
        self.importe = importe


def display(venta):
    r = f'{venta.nombre:^10}'
    r += f'{venta.importe:^10}'
