
# Contrato Indefinido vs Prestación de Servicios

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://salarios-colombia.streamlit.app)

Esta aplicación web te ayuda a comparar y convertir valores entre dos modalidades de contratación en Colombia:

1. **Contrato a Término Indefinido:** Calcula la tarifa equivalente por prestación de servicios a partir de un salario base mensual.
2. **Contrato por Prestación de Servicios:** Determina el salario base equivalente en un contrato indefinido a partir de una tarifa de prestación.

## Características

- Ajusta parámetros de cálculo: porcentaje de prestaciones sociales, salud, pensión y riesgos.
- Visualiza de forma clara y gráfica la distribución de costos.
- Obtén información normativa relevante sobre las dos modalidades de contratación.

## Requisitos

- Python 3.x
- Streamlit
- Pandas

## Cómo Ejecutar

1. Clona este repositorio.
2. Instala las dependencias:  
   ```bash
   pip install -r requirements.txt
   ```
3. Ejecuta la aplicación:  
   ```bash
   streamlit run app.py
   ```
4. Abre el enlace local que aparece en la terminal en tu navegador.

## Uso

1. Selecciona el tipo de conversión desde las pestañas: 
   - **"De contrato indefinido a prestación"**: Ingresa el salario base mensual.
   - **"De prestación a indefinido"**: Ingresa la tarifa mensual por prestación.
2. Ajusta los porcentajes desde la barra lateral.
3. Obtén resultados, desglose de costos y factores asociados.

## Nota
Esta herramienta es una guía informativa. No sustituye asesoría legal o contable profesional.

## Contribuciones
¡Gracias por tu interés en contribuir a este proyecto! Aquí te mostramos cómo puedes participar:

1. **Reportar Problemas**: Si encuentras algún error o problema, por favor repórtalo creando un Issue en el repositorio.
2. **Contribuir con Código**: Siente la libertad de realizar un Fork del repositorio, desarrollar tus mejoras y enviar un Pull Request (PR).
3. **Revisar PRs**: Si deseas ayudar, puedes revisar y dar tu opinión sobre los Pull Requests abiertos del proyecto.
4. **Compartir el Proyecto**: ¡Invita a otros desarrolladores y usuarios a conocer y utilizar esta herramienta!

### Lineamientos para Contribuciones
- Sigue las **buenas prácticas de codificación**, incluyendo un código limpio y bien documentado.
- Asegúrate de que los cambios estén cubiertos con **pruebas adecuadas** antes de enviar un PR.
- Proporciona una **descripción clara y detallada** del propósito del Pull Request.
- Verifica que los cambios no rompan otras partes del proyecto.
