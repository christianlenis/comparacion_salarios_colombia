import streamlit as st
from main import calcular_tarifa_prestacion_servicios, calcular_salario_base

st.set_page_config(page_title="Calculadora Contratos Colombia", layout="wide")

# Barra lateral con ajustes
with st.sidebar:
    st.write("Aquí puedes ajustar los porcentajes utilizados en los cálculos.")
    porcentaje_prestaciones = st.slider("Porcentaje Prestaciones Sociales", 0.0, 0.5, 0.35, 0.01)
    porcentaje_salud = st.slider("Porcentaje Salud (sobre base cotización)", 0.0, 0.2, 0.125, 0.005)
    porcentaje_pension = st.slider("Porcentaje Pensión (sobre base cotización)", 0.0, 0.2, 0.16, 0.005)
    porcentaje_riesgos = st.slider("Porcentaje Riesgos Laborales (sobre base cotización)", 0.0, 0.05, 0.01, 0.001)

# Encabezado principal
st.title("Calculadora Contratos en Colombia")

st.write("""
Esta herramienta te permite calcular equivalencias entre contratos a término indefinido y contratos por prestación de servicios. 

**Tip:** Hay parámetros configurables. Si necesitas ajustar los porcentajes, abre la barra lateral (flecha en la esquina superior izquierda) para modificar los valores.
""")

# Selector de cálculo
calculo_tipo = st.radio(
    "¿Qué deseas calcular?",
    ("De contrato indefinido a prestación de servicios",
     "De prestación de servicios a contrato indefinido")
)

if calculo_tipo == "De contrato indefinido a prestación de servicios":
    salario_base = st.number_input("Introduce el salario base mensual (en COP):", min_value=0, step=100000)
    if salario_base > 0:
        total_a_pedir, costos_seguridad_social, prestaciones, salud, pension, riesgos = calcular_tarifa_prestacion_servicios(
            salario_base,
            porcentaje_prestaciones,
            porcentaje_salud,
            porcentaje_pension,
            porcentaje_riesgos
        )
        st.markdown(
            f"**Tarifa de prestación de servicios equivalente:** <span style='color:green;font-weight:bold;'>{total_a_pedir:,.0f} COP</span>",
            unsafe_allow_html=True)

        with st.expander("Ver desglose de costos"):
            st.markdown(
                f"- **Costos de seguridad social:** <span style='color:red;'>{costos_seguridad_social:,.0f} COP</span>",
                unsafe_allow_html=True)
            st.markdown(f"  - Salud: {salud:,.0f} COP")
            st.markdown(f"  - Pensión: {pension:,.0f} COP")
            st.markdown(f"  - Riesgos: {riesgos:,.0f} COP")
            st.markdown(
                f"- **Costos de prestaciones sociales:** <span style='color:orange;'>{prestaciones:,.0f} COP</span>",
                unsafe_allow_html=True)

else:
    tarifa_prestacion = st.number_input("Introduce la tarifa mensual por prestación de servicios (en COP):",
                                        min_value=0, step=100000)
    if tarifa_prestacion > 0:
        salario_base, factor_total, factor_seguridad_social, factor_prestaciones = calcular_salario_base(
            tarifa_prestacion,
            porcentaje_prestaciones,
            porcentaje_salud,
            porcentaje_pension,
            porcentaje_riesgos
        )
        st.markdown(
            f"**Salario base equivalente:** <span style='color:blue;font-weight:bold;'>{salario_base:,.0f} COP</span>",
            unsafe_allow_html=True)

        with st.expander("Ver más información"):
            st.write("**Desglose de factores**:")
            st.write(f"- Factor total utilizado: {factor_total:.2f}")
            st.write(f"- Factor de seguridad social (con base en el 40%): {factor_seguridad_social:.2f}")
            st.write(
                f"- Factor de prestaciones sociales (ej. {porcentaje_prestaciones * 100:.0f}%): {factor_prestaciones:.2f}")

            st.markdown("""
            **Interpretación:**  
            La tarifa por prestación de servicios incluye el salario base, más los costos equivalentes a seguridad social y prestaciones 
            sociales que tendrías en un contrato indefinido.  

            Al dividir la tarifa por estos factores, obtienes el salario base que se equipara a lo que recibirías en un contrato a término indefinido.
            """)

# Sección informativa sobre normativa
st.markdown("---")
st.header("Información Normativa Relevante")

st.subheader("Contrato de Trabajo a Término Indefinido")
st.write("""
Un contrato a término indefinido es aquel que no tiene una fecha de finalización establecida, ofreciendo estabilidad laboral al trabajador. Este tipo de contrato puede ser acordado de forma verbal o escrita. Es importante destacar que, si no se especifica la duración del contrato, se presume que es a término indefinido. Más información disponible en [Gerencie.com](https://www.gerencie.com/contrato-de-trabajo-a-termino-indefinido.html).
""")

st.subheader("Contrato de Prestación de Servicios")
st.write("""
El contrato de prestación de servicios se utiliza para la ejecución de actividades relacionadas con la administración o funcionamiento de una entidad. Este contrato se caracteriza por la autonomía e independencia en la ejecución de las labores, sin que exista subordinación laboral. Es fundamental que este tipo de contrato no se utilice para encubrir una relación laboral que debería estar amparada por un contrato de trabajo. Más detalles en [Asuntos Legales](https://www.asuntoslegales.com.co/consultorio/regulacion-del-contrato-de-prestacion-de-servicios-2168926).
""")

st.subheader("Consideraciones Importantes")
st.write("""
- **Subordinación:** En un contrato de trabajo existe subordinación, mientras que en un contrato de prestación de servicios, el contratista actúa con independencia.
- **Prestaciones Sociales:** Los contratos de trabajo a término indefinido incluyen prestaciones sociales como prima, cesantías y vacaciones, las cuales no aplican en contratos de prestación de servicios.
- **Seguridad Social:** En los contratos de prestación de servicios, el contratista es responsable de sus aportes a seguridad social, mientras que en los contratos laborales, el empleador asume una parte de estos aportes.

Para profundizar en estos temas, puedes consultar la [Guía para la Contratación de Prestación de Servicios](https://colombiacompra.gov.co/sites/cce_public/files/files_2020/cce-eicp-gi-21_guia_contratacion_prestacion_de_servicios_v1_03-03-2023_1.pdf) de Colombia Compra Eficiente.
""")

st.info("Recuerda que es fundamental conocer la normativa vigente para asegurar el cumplimiento de las obligaciones legales en cualquier modalidad de contratación.")
