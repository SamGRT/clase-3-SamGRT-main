"""
## Ejercicio 4

Considere un triángulo de lados `a`, `b` y `c`. Utilizando la formula de Herón el área de triangulo viene dada por la siguiente ecuación:

$$
A = \sqrt{s(s-a)(s-b)(s-c)}
$$

Donde el semiperímetro del triángulo es:

$$
s = \frac{a+b+c}{2}
$$

Realice un programa que reciba las distancias de los 3 lados del triángulo y determine su área utilizando la formula de Herón.
"""
import math

print("Para el cálculo del área de un triángulo, a continuación debera indicar las 3 distancias de los 3 lados del triángulo:")
a = float(input("\nIndique la distancia 'a' del triángulo --> "))
b = float(input("Indique la distancia 'b' del triángulo --> "))
c = float(input("Indique la distancia 'c' del triángulo --> "))
s = (a+b+c)/2
if a>s or b>s or c>s :
    print("Con los datos ingresados resultará un número no perteneciente a los reales")
else:
    área = math.sqrt(s*(s-a)*(s-b)*(s-c))
    print(f"El área del triángulo es de {área:.3f} cm² ")
    