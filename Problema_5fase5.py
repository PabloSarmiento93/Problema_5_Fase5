# Pablo Daniel Sarmiento Cruz
# 213022_127
# Ingeniería de sistemas
# Fundamento de Programación
# Código Fuente: autoría propia

recursos = [
    ["Pablo Sarmiento", 8, 8, 8, 8, 8],
    ["Andrés Rodriguez", 9, 9, 8, 9, 8],
    ["Jonathan Giot", 7, 8, 8, 7, 8],
    ["Mayra Ochoa", 10, 9, 9, 8, 9]
]


def calcular_horas(horas):
    total = sum(horas)

    if total > 40:
        clasificacion = "Sobretiempo"
    else:
        clasificacion = "Horario Estándar"

    return total, clasificacion

print()
print("=" * 40)
print("REPORTE DE HORAS SEMANALES")
print("=" * 40)
print()

for recurso in recursos:
    nombre = recurso[0]
    horas = recurso[1:]

    total, clasificacion = calcular_horas(horas)

    print("----------------------------")
    print("Nombre:", nombre)
    print("Total de horas:", total)
    print("Clasificación:", clasificacion)


