import streamlit as st
import pandas as pd
from main import calcular_tarifa_prestacion_servicios, calcular_salario_base

# Set page title and layout
st.set_page_config(
    page_title="Calculadora Contratos Colombia",
    layout="wide"
)

# Sidebar configuration
st.sidebar.subheader("Ajustes de Cálculo")
with st.sidebar:
    st.write("Ajusta los porcentajes utilizados en los cálculos:")
    st.help("Estos porcentajes afectan el resultado final. Ajusta con cuidado.")
    porcentaje_prestaciones = st.slider(
        "Porcentaje Prestaciones Sociales", 0.0, 0.5, 0.35, 0.01,
        help="Incluye prima, cesantías y vacaciones. Generalmente alrededor del 35%."
    )
    porcentaje_salud = st.slider(
        "Porcentaje Salud (sobre base cotización)", 0.0, 0.2, 0.125, 0.005,
        help="Porcentaje del 40% de la tarifa destinado a salud."
    )
    porcentaje_pension = st.slider(
        "Porcentaje Pensión (sobre base cotización)", 0.0, 0.2, 0.16, 0.005,
        help="Porcentaje del 40% de la tarifa destinado a pensión."
    )
    porcentaje_riesgos = st.slider(
        "Porcentaje Riesgos Laborales (sobre base cotización)", 0.0, 0.05, 0.01, 0.001,
        help="Costo de riesgos laborales aplicado sobre la base del 40%."
    )

# Main title and introduction
st.title("📑 Calculadora de Contratos en Colombia")
st.write("""
Esta herramienta te ayuda a calcular equivalencias entre contratos a término indefinido y contratos por prestación de servicios. 

- Ajusta los parámetros en la barra lateral.
- Selecciona el tipo de cálculo.
- Ingresa los valores.
""")

# Tabs for the two calculation types
tabs = st.tabs(["De contrato indefinido a prestación", "De prestación a indefinido"])

with tabs[0]:
    # "De contrato indefinido a prestación de servicios"
    st.subheader("De Contrato Indefinido a Prestación de Servicios")
    st.info(
        "Calcula cuánto debes cobrar por prestación de servicios para recibir el equivalente de un salario indefinido.")

    # Example Button
    if st.button("Cargar Ejemplo", key="ejemplo_indefinido"):
        salario_base_example = 2500000
    else:
        salario_base_example = 0

    salario_base = st.number_input(
        "Introduce el salario base mensual (en COP):",
        min_value=0, step=100000, value=salario_base_example,
        help="Este es el salario base mensual en un contrato a término indefinido."
    )

    if salario_base > 0:
        total_a_pedir, costos_seguridad_social, prestaciones, salud, pension, riesgos = calcular_tarifa_prestacion_servicios(
            salario_base,
            porcentaje_prestaciones,
            porcentaje_salud,
            porcentaje_pension,
            porcentaje_riesgos
        )

        # Layout with two columns: results on the right
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("### Resultado")
            st.markdown(
                f"**Tarifa de prestación de servicios equivalente:** :green_heart: **{total_a_pedir:,.0f} COP**"
            )

            with st.expander("Ver desglose de costos"):
                st.write("Costos de seguridad social:")
                st.metric("Salud", f"{salud:,.0f} COP")
                st.metric("Pensión", f"{pension:,.0f} COP")
                st.metric("Riesgos", f"{riesgos:,.0f} COP")

                st.write("Prestaciones sociales:")
                st.metric("Prestaciones Sociales", f"{prestaciones:,.0f} COP")

        # On the right column, show a small bar chart for breakdown
        with col2:
            st.markdown("#### Distribución de Costos")
            df = pd.DataFrame({
                'Concepto': ['Salud', 'Pensión', 'Riesgos', 'Prestaciones'],
                'Valor': [salud, pension, riesgos, prestaciones]
            })
            st.bar_chart(df.set_index('Concepto'))

with tabs[1]:
    # "De prestación de servicios a contrato indefinido"
    st.subheader("De Prestación de Servicios a Contrato Indefinido")
    st.info("Calcula el salario base equivalente en un contrato indefinido a partir de una tarifa por prestación.")

    # Example Button
    if st.button("Cargar Ejemplo", key="ejemplo_prestacion"):
        tarifa_example = 3500000
    else:
        tarifa_example = 0

    tarifa_prestacion = st.number_input(
        "Introduce la tarifa mensual por prestación de servicios (en COP):",
        min_value=0, step=100000, value=tarifa_example,
        help="La tarifa mensual que facturarías por prestación de servicios."
    )

    if tarifa_prestacion > 0:
        salario_base_calc, factor_total, factor_seguridad_social, factor_prestaciones = calcular_salario_base(
            tarifa_prestacion,
            porcentaje_prestaciones,
            porcentaje_salud,
            porcentaje_pension,
            porcentaje_riesgos
        )

        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("### Resultado")
            st.markdown(
                f"**Salario base equivalente:** :blue_heart: **{salario_base_calc:,.0f} COP**"
            )

            with st.expander("Ver más información"):
                st.write("**Desglose de Factores**:")
                st.write(f"- Factor total: {factor_total:.2f}")
                st.write(f"- Factor de seguridad social (40% base): {factor_seguridad_social:.2f}")
                st.write(
                    f"- Factor de prestaciones sociales ({porcentaje_prestaciones * 100:.0f}%): {factor_prestaciones:.2f}")

                st.markdown("""
                **Interpretación:**  
                La tarifa por prestación de servicios incluye el salario base, más los costos equivalentes a seguridad social y prestaciones 
                sociales que tendrías en un contrato indefinido.  

                Al dividir la tarifa por estos factores, obtienes el salario base equivalente.
                """)

        # On the right column, a brief numeric summary
        with col2:
            st.markdown("#### Resumen Numérico")
            st.metric("Factor Total", f"{factor_total:.2f}")
            st.metric("Factor Seguridad Social", f"{factor_seguridad_social:.2f}")
            st.metric("Factor Prestaciones", f"{factor_prestaciones:.2f}")

# Additional Information Section
st.markdown("---")
st.header("Información Normativa Relevante")

st.subheader("Contrato de Trabajo a Término Indefinido")
st.write("""
Un contrato a término indefinido es aquel que no tiene una fecha de finalización establecida, ofreciendo estabilidad laboral al trabajador. 
Si no se específica la duración, se presume que es indefinido. 
[Más información](https://www.gerencie.com/contrato-de-trabajo-a-termino-indefinido.html).
""")

st.subheader("Contrato de Prestación de Servicios")
st.write("""
El contrato de prestación de servicios se basa en la autonomía e independencia del contratista, sin subordinación. 
No incluye prestaciones sociales. 
[Más información](https://www.asuntoslegales.com.co/consultorio/regulacion-del-contrato-de-prestacion-de-servicios-2168926).
""")

st.subheader("Consideraciones Importantes")
st.write("""
- **Subordinación:** Presente en contratos laborales, no en prestación de servicios.
- **Prestaciones Sociales:** Incluidas en contratos laborales, no en prestación de servicios.
- **Seguridad Social:** En prestación de servicios, el contratista asume sus aportes.

[Guía de Colombia Compra Eficiente](https://colombiacompra.gov.co/sites/cce_public/files/files_2020/cce-eicp-gi-21_guia_contratacion_prestacion_de_servicios_v1_03-03-2023_1.pdf)
""")

st.info(
    "Conocer la normativa vigente es crucial para cumplir con las obligaciones legales en cualquier modalidad de contratación.")
