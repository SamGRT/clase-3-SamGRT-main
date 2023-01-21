# El volumen actual de un depósito de agua (en metros cúbicos)
volumen_reservorio = 4.445e8
# La cantidad de lluvia de una tormenta (en metros cúbicos)
lluvia = 5e6

# Escribe tu respuesta aqui ✍️

porcentaje = lluvia * 0.1
lluvia -= porcentaje
volumen_reservorio += lluvia
porcentaje = volumen_reservorio * 0.05
volumen_reservorio += porcentaje
porcentaje = volumen_reservorio * 0.02
volumen_reservorio -= porcentaje
volumen_reservorio -= 2.5e5
print(volumen_reservorio)
