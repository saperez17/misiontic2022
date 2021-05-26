def calcular_herencia(ganado_heredado):
    """Cantidad de ganado heredado por cada uno de los hermanos
    Parámetros:
    -----------
    ganado_heredado (int):
    Número de cabezas de ganado que heredan los 3 hermanos.
    Debe ser múltiplo de 6.
    Retorna:
    --------
    str: Cadena de caracteres de la forma “Total: {ganado_heredado}
    Hijo mayor: {ganado_heredado_hermano_mayor}
    Hijo del medio: {ganado_heredado_hermano_medio}
    Hijo menor: {ganado_heredado_hermano_menor}.”
    con la información de la cantidad de ganado heredado
    por cada hermano.
    """
    if (ganado_heredado%6!=0):
        return f"Valor de entrada no multipe de 6"
    fraction = ganado_heredado/6
    brothers_share = [fraction*i for i in [1,2,3]]
    return f"Total: {ganado_heredado}\nHijo mayor: {brothers_share[2]:.0f}\nHijo del medio: {brothers_share[1]:.0f}\nHijo menor: {brothers_share[0]:.0f}"

if __name__ == "__main__":
    for i in [180]:
        print(calcular_herencia(i))