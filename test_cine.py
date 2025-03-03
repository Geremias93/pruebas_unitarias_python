import pytest
from cine import Pelicula

def test_compra_exitosa():
    pelicula = Pelicula("Prueba", 10, 10)
    resultado = pelicula.vender_entradas(5)
    assert resultado == "Has comprado 5 entradas para Prueba. Total: $50"

def test_asientos_insuficientes():
    pelicula = Pelicula("Prueba", 3, 10)
    resultado = pelicula.vender_entradas(5)
    assert resultado == "No hay suficientes asientos disponibles. Solo quedan 3 asientos."

def test_compra_cero_entradas():
    pelicula = Pelicula("Prueba", 10, 10)
    resultado = pelicula.vender_entradas(0)
    assert resultado == "Has comprado 0 entradas para Prueba. Total: $0"
