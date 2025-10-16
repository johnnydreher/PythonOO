"""
Enunciado:
Crie um sistema para cálculo de áreas de figuras geométricas.

Deve conter:
- Classe base Figura com método abstrato area().
- Classes derivadas:
  - Circulo (atributo: raio)
  - Retangulo (atributos: base e altura)
- Cada classe deve implementar o cálculo da área conforme sua fórmula.

O que será avaliado:
- Uso de herança e métodos abstratos.
- Aplicação correta das fórmulas matemáticas.
"""
# TODO: implementar classes Figura, Circulo e Retangulo
import math
class Figura:
    def area(self):
        raise NotImplementedError("Subclasses devem implementar este método")
class Circulo(Figura):
    def __init__(self, raio):
        self.raio = raio
    def area(self):
        return math.pi * (self.raio ** 2)
class Retangulo(Figura):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura