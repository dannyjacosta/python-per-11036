class Libro:

    def __init__(self, titulo, autor, isbn, editorial, paginas, edicion, extracto=''):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.editorial = editorial
        self.paginas = paginas
        self.edicion = edicion
        self.extracto = extracto

    def print(self):
        print(f'Titulo: {self.titulo}\n'
              f'Autor: {self.autor}\n'
              f'Editorial: {self.editorial}\n'
              f'ISBN: {self.isbn}\n'
              f'Extracto: {self.extracto}')


don_quijote = Libro(titulo='El Ingenioso Hidalgo Don Quijote de la Mancha',
                    autor='Miguel de Cervantes',
                    isbn='0987-7489',
                    editorial='Seix Barall',
                    paginas=934,
                    edicion=145,
                    extracto='En un lugar de la mancha, de cuyo nombre no quiero acordarme,\n no hace mucho tiempo que vivía un hidalgo de los de lanza en astillero,\n adarga antigua, rocín flaco y galgo corredor.')
print()
don_quijote.print()

diablo_guardian = Libro(titulo='El Diablo Guardian',
                        autor='Javier Velazco',
                        isbn='0987-7621',
                        editorial='Alfaguara',
                        paginas=412,
                        edicion=6,
                        extracto='')

print()
diablo_guardian.print()
