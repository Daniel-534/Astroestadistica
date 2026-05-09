
# GUÍA DE TRABAJO DE CAMPO: ESTADÍSTICA INFERENCIAL EN EXCEL O RSTUDIO

**TÍTULO DEL PROYECTO:** ____________________________________________  
**NOMBRES DE LOS INTEGRANTES:** Mariana Soto Villada  
**ASIGNATURA:** Estadística  
**FECHA:** ___________________________________________________________

---

## Introducción

El presente trabajo de campo tiene como propósito aplicar los conocimientos de estadística
inferencial en la resolución de problemas reales mediante el uso de Excel o R-Studio. A través
del análisis de datos cuantitativos y cualitativos, los estudiantes podrán formular hipótesis,
aplicar pruebas estadísticas, construir modelos de regresión múltiple e interpretar los
resultados con sentido crítico y técnico.

Se espera que el estudiante desarrolle habilidades para la toma de decisiones informadas
basadas en evidencia estadística. Algunos ejemplos de temas son: horas de estudio y nota
final, tiempo de sueño y rendimiento académico, uso de redes sociales y concentración,
nivel de satisfacción con el entorno académico, o tiempo de transporte y productividad.

---

## Objetivos

### Objetivo General
Aplicar técnicas inferenciales y modelos de regresión múltiple para analizar datos reales
mediante Excel o R-Studio, fortaleciendo la capacidad de interpretar resultados, tomar
decisiones y comunicar hallazgos.

### Objetivos Específicos
- Formular hipótesis y seleccionar pruebas estadísticas adecuadas según el tipo de variable.
- Aplicar pruebas de normalidad, independencia y no paramétricas.
- Calcular e interpretar correlaciones y modelos de regresión lineal múltiple.
- Elaborar conclusiones sustentadas en la evidencia estadística obtenida.

---

## Competencias

- Comprende los fundamentos de la estadística inferencial y sus aplicaciones.
- Interpreta resultados obtenidos en pruebas de hipótesis y modelos predictivos.
- Utiliza Excel o R-Studio como herramienta de análisis estadístico.
- Comunica los resultados de forma escrita y oral con precisión técnica.

---

## Etapas del Trabajo

### 1. Recolección de Datos
Seleccione un tema de interés que permita la observación o medición. Recolecte **70
observaciones válidas** mediante encuesta o medición directa. Defina mínimo **6 variables**:
3 cuantitativas (2 continuas y 1 discreta) y 3 cualitativas (2 nominales y 1 ordinal).

> **Ejemplo:** Estudio sobre hábitos de sueño y rendimiento académico.

---

### 2. Análisis Descriptivo

**En Excel**, calcule medidas de tendencia central y dispersión con funciones como:
```excel
=MEDIA(rango)
=DESVEST.M(rango)
=MIN(rango)
=MAX(rango)
```

**En R-Studio**, use:
```r
mean(variable)
sd(variable)
summary(variable)
```

Interprete los resultados.

---

### 3. Pruebas de Hipótesis

- **Prueba de normalidad:** `PRUEBA.Z.N()` o en R `shapiro.test(variable)`
- **Prueba de independencia (Chi-cuadrado):** `PRUEBA.CHICUAD(fo; fe)`
- **Pruebas no paramétricas:** prueba del signo, Mann-Whitney, prueba de corridas.
- **Pruebas pareadas:** `PRUEBA.T.N(rangoX1; rangoX2; 2; 1)`
- **Diferencia de medias independientes:** `PRUEBA.T.N(rangoX1; rangoX2; 2; 2 o 3)`

> Interprete el valor p: si $p < 0.05$ se rechaza $H_0$.

---

### 4. Correlación y Regresión Lineal Múltiple

- **Correlación de Pearson en Excel:** `=COEF.DE.CORREL(rango_x; rango_y)`
- **En R:** `cor(x, y)`
- **Regresión múltiple en Excel:** Datos -> Análisis de datos -> Regresión
- **En R:**
```r
modelo <- lm(Y ~ X1 + X2)
```

Analice los coeficientes, el $R^{2}$ y los valores p.

---

### 5. Inferencia y Predicción

Evalúe la significancia de los coeficientes:

- $H_0$: $\beta = 0$
- $H_1$: $\beta \neq 0$

Realice predicciones con valores hipotéticos de $X_1$ y $X_2$. Verifique supuestos:
linealidad, independencia, normalidad de residuos y homocedasticidad.

---

### 6. Entregable Final

- Archivo Excel con hojas separadas para cada análisis (base de datos, descriptivos,
  pruebas, regresión, resumen e interpretación).
- Informe técnico con introducción, planteamiento del problema, hipótesis, resultados
  y conclusiones.
- Video de exposición (máximo 10 minutos, formato MP4) con todos los integrantes
  participando.

---

## Modelos y Ejemplos

### Ejemplo de Tabla de Datos

| Sexo | Edad | Empleo | Estrato | Promedio creditos | Promedio Asignatura | N. horas de estudio | Semestre |
|------|------|--------|---------|-------------------|---------------------|---------------------|----------|
| f    | 22   | si     | 2       | 3.9               | 3.5                 | 1                   | 3        |
| f    | 34   | no     | 4       | 3.7               | 3.0                 | 2                   | 4        |
| m    | 21   | si     | 3       | 4.1               | 3.7                 | 1                   | 3        |
| f    | 24   | si     | 3       | 4.2               | 3.2                 | 0                   | 5        |
| f    | 23   | si     | 3       | 3.9               | 3.5                 | 0                   | 6        |

### Ejemplo de Hipótesis

- $H_0$: No existe relación entre horas de estudio y promedio asignatura.
- $H_1$: Existe relación significativa entre horas de estudio y promedio asignatura.

---

## Rúbrica de Evaluación (50 puntos)

| Criterio                | Descripción                                                              | Puntaje |
|-------------------------|--------------------------------------------------------------------------|---------|
| Organización de datos   | Base de datos clara, sin errores y bien etiquetada. Fuente justificada.  | 5       |
| Análisis descriptivo    | Gráficos, medidas y resumen adecuados e interpretados.                   | 10      |
| Pruebas de hipótesis    | Aplicación correcta, interpretación coherente.                           | 12      |
| Regresión y correlación | Cálculo, interpretación e inferencia del modelo.                         | 13      |
| Presentación e informe  | Orden, ortografía, conclusiones fundamentadas.                           | 5       |
| Creatividad y rigor     | Claridad, profundidad y originalidad en el trabajo.                      | 5       |

---

## Recomendaciones Académicas

- Cita correctamente las fuentes y datos usados, siguiendo **normas APA**.
- Usa fórmulas visibles y verifica coherencia entre hipótesis y resultados.
- Revisa ortografía, coherencia en títulos y nomenclaturas estadísticas.
- En el video, presenta de manera clara la justificación, metodología, análisis y conclusiones.
- Todos los integrantes deben participar activamente en la exposición.
