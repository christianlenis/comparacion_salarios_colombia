

def calcular_tarifa_prestacion_servicios(base_salary: float,
                                         porcentaje_prestaciones: float = 0.35,
                                         porcentaje_salud: float = 0.125,
                                         porcentaje_pension: float = 0.16,
                                         porcentaje_riesgos:float = 0.01):
    """
    Calcula la tarifa a pedir para un contrato por prestación de servicios, teniendo en cuenta los costos
    de seguridad social y las prestaciones sociales.

    Args:
        base_salary (float): Salario base acordado.
        porcentaje_prestaciones (float, opcional): Porcentaje destinado a prestaciones sociales. Por defecto es 0.35 (o 35%).
        porcentaje_salud (float, opcional): Porcentaje destinado a salud. Por defecto es 0.125 (o 12.5%).
        porcentaje_pension (float, opcional): Porcentaje destinado a pensión. Por defecto es 0.16 (o 16%).
        porcentaje_riesgos (float, opcional): Porcentaje destinado a riesgos laborales. Por defecto es 0.01 (o 1%).

    Returns:
        tuple: Una tupla con los siguientes valores:
            - total_a_pedir (float): Monto total a solicitar en el contrato.
            - costos_seguridad_social (float): Total de los costos de seguridad social (salud, pensión, riesgos).
            - prestaciones (float): Monto de las prestaciones sociales.
            - salud (float): Monto destinado a salud.
            - pension (float): Monto destinado a pensión.
            - riesgos (float): Monto destinado a riesgos laborales.
    """
    base_cotizacion = base_salary * 0.40
    salud = base_cotizacion * porcentaje_salud
    pension = base_cotizacion * porcentaje_pension
    riesgos = base_cotizacion * porcentaje_riesgos
    costos_seguridad_social = salud + pension + riesgos
    prestaciones = base_salary * porcentaje_prestaciones
    total_a_pedir = base_salary + costos_seguridad_social + prestaciones
    return total_a_pedir, costos_seguridad_social, prestaciones, salud, pension, riesgos


def calcular_salario_base(tarifa_prestacion_servicios: float,
                          porcentaje_prestaciones: float = 0.35,
                          porcentaje_salud: float = 0.125,
                          porcentaje_pension: float = 0.16,
                          porcentaje_riesgos: float = 0.01):
    """
    Calcula el salario base según la tarifa acordada en un contrato por prestación de servicios.

    Args:
        tarifa_prestacion_servicios (float): Monto total acordado en el contrato.
        porcentaje_prestaciones (float, opcional): Porcentaje destinado a prestaciones sociales. Por defecto es 0.35 (o 35%).
        porcentaje_salud (float, opcional): Porcentaje destinado a salud. Por defecto es 0.125 (o 12.5%).
        porcentaje_pension (float, opcional): Porcentaje destinado a pensión. Por defecto es 0.16 (o 16%).
        porcentaje_riesgos (float, opcional): Porcentaje destinado a riesgos laborales. Por defecto es 0.01 (o 1%).

    Returns:
        tuple: Una tupla con los siguientes valores:
            - salario_base (float): Salario base calculado.
            - factor_total (float): Factor total generado por los porcentajes de seguridad social y prestaciones.
            - factor_seguridad_social (float): Factor generado únicamente por los porcentajes de seguridad social.
            - factor_prestaciones (float): Factor generado únicamente por el porcentaje de prestaciones sociales.
    """
    factor_seguridad_social = (0.40 * porcentaje_salud +
                               0.40 * porcentaje_pension +
                               0.40 * porcentaje_riesgos)
    factor_prestaciones = porcentaje_prestaciones
    factor_total = 1 + factor_seguridad_social + factor_prestaciones
    salario_base = tarifa_prestacion_servicios / factor_total
    return salario_base, factor_total, factor_seguridad_social, factor_prestaciones
