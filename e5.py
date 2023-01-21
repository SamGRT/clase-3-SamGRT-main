"""
## Ejercicio 5

La ley de Coulomb describe matemáticamente la fuerza eléctrica producida entre dos cargas $q_1$ y $q_2$

$$
\vec{F} = k \frac{q_1q_2}{r^2} \widehat{r}
$$

En donde $k$ es la contaste dieléctrica, $q_1$ y $q_2$ es la magnitud de ambas y $r$ es la distancia que hay entre las cargas.

Realice un programa que solicite los valores de $q_1$, $q_2$ y $r$ para calcular la magnitud de la fuerza.

**Nota** en el vacío la constante $k$ equivale a `8.85e-12`

"""
print("A continuación ingrese la fuerza eléctrica de las 2 cargas para calcular la magnitud de la fuerza:")
q_1 = float(input("Ingrese la carga q1 --> "))
q_2 = float(input("ingrese la carga q2 --> "))
r = float(input("Ingrese la distancia que hay entre las cargas q1 y q2 --> "))
k = 8.85e-12
Resultado = k*((q_1 * q_2)/r**2)
print(f"\nLa magnitud de la fuerza entre las 2 cargas es de {Resultado} N. ")

