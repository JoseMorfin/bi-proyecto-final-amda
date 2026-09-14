# Proyecto final — Mercado de vehículos ligeros en México

Materia: Inteligencia de Negocio y Soluciones de Ciencia de Datos (Prof. Edgar Avalos Gauna).
Fuente: Reporte Mercado Interno Automotor Ligeros, AMDA, agosto 2026 (cifras de INEGI).

[![Abrir en Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/JoseMorfin/bi-proyecto-final-amda/blob/main/PROYECTO_FINAL_BI.ipynb)

## Qué hay en este repositorio

| archivo | qué es |
|---|---|
| `PROYECTO_FINAL_BI.ipynb` | el cuaderno del proyecto: secciones con pistas, las gráficas las hacemos nosotros |
| `datos/` | los 8 csv capturados del PDF (abajo dice de qué página sale cada uno) |
| `main.py` | la app de Streamlit; ya corre, faltan las gráficas (`# TODO (equipo)`) |
| `requirements.txt` | lo que Streamlit Cloud instala |

El cuaderno lee los csv directo de aquí con la liga *raw*, así que no hay que subir
archivos a Colab. Si cambia un csv en el repo, el cuaderno lo ve al volver a correr.

## Datos

| archivo | de qué página del PDF | filas |
|---|---|---|
| `ventas_mensuales_2008_2026.csv` | pág. 20 (tabla mes × año) | 224 |
| `segmentos_comparativo_2025_2026.csv` | págs. 2, 3 y 4 | 35 |
| `segmentos_agosto_2012_2026.csv` | pág. 29 (gráfica de líneas) | 15 |
| `marcas_origen_ene_ago_2025_2026.csv` | pág. 23 (tabla por marca) | 192 |
| `hibridos_electricos_2016_2026.csv` | pág. 33 | 11 |
| `hibridos_electricos_por_estado_2026.csv` | pág. 33 | 13 |
| `compradores_por_region_2025_2026.csv` | pág. 34 | 7 |
| `financiamiento_ene_jul_2017_2026.csv` | pág. 16 | 10 |

Todo se comprobó contra los totales del mismo PDF:

- Ventas mensuales: la suma de los 12 meses coincide con el total anual del PDF en 17 de 18 años; enero-agosto 2026 da 1,014,715, igual que el reporte.
- Segmentos: cada periodo suma exacto el total del PDF.
- Marcas: importado y nacional suman exacto lo del PDF en los dos años.
- Híbridos por estado: suman 129,359, el total del reporte.
- Financiamiento: el % calculado da igual que el del PDF.

Dos cosas a tener en cuenta (sirven para la parte de calidad de datos):

1. **Diciembre 2022.** El PDF dice que el total 2022 es 1,094,728, pero la suma de sus 12 meses da 1,094,828. Se dejó el dato como está impreso (123,382). Seguramente es un error de dedo del reporte.
2. **`segmentos_agosto_2012_2026.csv` tiene huecos.** La gráfica del PDF no etiqueta todos los puntos: `deportivos` está vacío de 2012 a 2024 y faltan compactos 2022 y 2024 y subcompactos 2023. No se inventó ningún número; en el cuaderno hay un ejercicio para calcular deportivos como resto del total.

Cuando Edgar mande más datos, van en `datos/` y se agrega una fila a esta tabla.

## Correr la app en tu compu

```
pip install -r requirements.txt
streamlit run main.py
```

## Desplegar en Streamlit Cloud

Igual que la app de pases: entrar a share.streamlit.io → Deploy → elegir este repo,
rama `main`, archivo `main.py` → Deploy. La liga que salga es la que se entrega.

## Si queremos ir más lejos

INEGI publica la base original (RAIAVL) con ventas por marca, modelo y segmento, mes a mes:
https://www.inegi.org.mx/app/tabulados/interactivos/?px=RAIAVL_8_9&bd=RAIAVL
