import pytest
from biblioteca import Libro, Biblioteca

# Pruebas para la clase Libro
def test_inicializacion_libro():
    libro = Libro("1984", "George Orwell", 1949)
    assert libro.titulo == "1984"
    assert libro.autor == "George Orwell"
    assert libro.anio == 1949
    assert libro.prestado == False

def test_estado_libro():
    libro = Libro("1984", "George Orwell", 1949)
    assert "disponible" in str(libro)
    libro.prestado = True
    assert "prestado" in str(libro)

# Pruebas para la clase Biblioteca

def test_agregar_libro():
    biblioteca = Biblioteca()
    libro = Libro("El Principito", "Antoine de Saint-Exupéry", 1943)
    biblioteca.agregar_libro(libro)
    assert len(biblioteca.libros) == 1
    assert biblioteca.libros[0].titulo == "El Principito"

def test_eliminar_libro():
    biblioteca = Biblioteca()
    libro = Libro("Moby Dick", "Herman Melville", 1851)
    biblioteca.agregar_libro(libro)
    biblioteca.eliminar_libro("Moby Dick")
    assert len(biblioteca.libros) == 0

def test_eliminar_libro_inexistente():
    biblioteca = Biblioteca()
    libro = Libro("Orgullo y Prejuicio", "Jane Austen", 1813)
    biblioteca.agregar_libro(libro)
    biblioteca.eliminar_libro("Libro que no existe")
    assert len(biblioteca.libros) == 1  # No debería eliminar el libro existente

def test_buscar_libro_existente():
    biblioteca = Biblioteca()
    libro = Libro("Drácula", "Bram Stoker", 1897)
    biblioteca.agregar_libro(libro)
    resultado = biblioteca.buscar_libro("Drácula")
    assert resultado is not None
    assert resultado.titulo == "Drácula"

def test_buscar_libro_inexistente():
    biblioteca = Biblioteca()
    resultado = biblioteca.buscar_libro("Libro Fantasma")
    assert resultado is None

def test_listar_libros():
    biblioteca = Biblioteca()
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", 1967)
    libro2 = Libro("Don Quijote de la Mancha", "Miguel de Cervantes", 1605)
    biblioteca.agregar_libro(libro1)
    biblioteca.agregar_libro(libro2)
    lista = biblioteca.listar_libros()
    assert len(lista) == 2
    assert "Cien años de soledad" in lista[0]
    assert "Don Quijote de la Mancha" in lista[1]

def test_prestar_libro_disponible():
    biblioteca = Biblioteca()
    libro = Libro("El Hobbit", "J.R.R. Tolkien", 1937)
    biblioteca.agregar_libro(libro)
    resultado = biblioteca.prestar_libro("El Hobbit")
    assert resultado == "Has pedido prestado el libro 'El Hobbit'."
    assert libro.prestado == True

def test_prestar_libro_ya_prestado():
    biblioteca = Biblioteca()
    libro = Libro("El Hobbit", "J.R.R. Tolkien", 1937)
    biblioteca.agregar_libro(libro)
    biblioteca.prestar_libro("El Hobbit")
    resultado = biblioteca.prestar_libro("El Hobbit")
    assert resultado == "El libro 'El Hobbit' ya está prestado."

def test_prestar_libro_inexistente():
    biblioteca = Biblioteca()
    resultado = biblioteca.prestar_libro("Libro que no existe")
    assert resultado == "El libro 'Libro que no existe' no se encuentra en la biblioteca."

def test_devolver_libro_prestado():
    biblioteca = Biblioteca()
    libro = Libro("Harry Potter", "J.K. Rowling", 1997)
    biblioteca.agregar_libro(libro)
    biblioteca.prestar_libro("Harry Potter")
    resultado = biblioteca.devolver_libro("Harry Potter")
    assert resultado == "Has devuelto el libro 'Harry Potter'."
    assert libro.prestado == False

def test_devolver_libro_no_prestado():
    biblioteca = Biblioteca()
    libro = Libro("Harry Potter", "J.K. Rowling", 1997)
    biblioteca.agregar_libro(libro)
    resultado = biblioteca.devolver_libro("Harry Potter")
    assert resultado == "El libro 'Harry Potter' no estaba prestado."

def test_devolver_libro_inexistente():
    biblioteca = Biblioteca()
    resultado = biblioteca.devolver_libro("Libro que no existe")
    assert resultado == "El libro 'Libro que no existe' no se encuentra en la biblioteca."
