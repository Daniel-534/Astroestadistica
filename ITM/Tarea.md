Descripción de la actividad

Diseñe un aplicativo en Excel que permita evaluar y comparar proyectos de inversión mediante la organización de sus flujos de caja, el cálculo de indicadores financieros y la interpretación de los resultados.

El aplicativo deberá funcionar con diferentes datos de entrada y actualizar automáticamente sus resultados. Su diseño debe permitir que cualquier usuario comprenda qué información ingresar, cómo utilizar la herramienta y cómo interpretar sus salidas.

La herramienta tendrá un alcance general dentro de las condiciones expresamente definidas en su manual. No deberá quedar limitada a resolver un único ejercicio ni depender de modificaciones manuales de las fórmulas cada vez que cambien los datos.

Objetivo general

Desarrollar un aplicativo que integre los conceptos de matemáticas financieras para evaluar alternativas de inversión y sustentar decisiones mediante indicadores, análisis de sensibilidad y criterios de interpretación.

Objetivos específicos

Organizar la inversión inicial y los flujos de caja de proyectos con diferentes horizontes de evaluación.
Aplicar correctamente la equivalencia financiera y la correspondencia entre tasas y periodos.
Calcular e interpretar indicadores de conveniencia financiera.
Comparar alternativas e identificar cómo cambian sus resultados ante variaciones en los supuestos.
Validar los cálculos y documentar el funcionamiento, las condiciones de uso y las limitaciones del aplicativo.
1. Alcance y requisitos del aplicativo

La herramienta deberá permitir evaluar un proyecto de manera individual y comparar, como mínimo, dos alternativas de inversión. Debe admitir flujos periódicos de cuantía variable, sin exigir que los ingresos o egresos sean iguales en todos los periodos.

El número de periodos deberá ser configurable dentro de una capacidad definida por los autores. Al modificarlo, los cálculos deberán considerar únicamente los periodos activos y evitar incluir valores residuales de ejercicios anteriores.

La versión mínima trabajará con periodos regulares. Si se incorporan flujos con fechas irregulares, deberá identificarse esta modalidad y utilizar procedimientos compatibles con dichas fechas.

2. Datos de entrada

Incluya campos claramente identificados para ingresar:

Nombre y descripción breve de cada proyecto.
Moneda y unidad de presentación de los valores.
Inversión inicial, ubicada en el momento cero.
Número de periodos y periodicidad del análisis.
Ingresos y egresos de cada periodo.
Valor residual y recuperación del capital de trabajo, cuando correspondan.
Tasa de descuento, indicando su modalidad y periodicidad.
Supuestos utilizados para construir los flujos de caja.
El aplicativo deberá calcular el flujo neto de cada periodo y establecer una convención de signos comprensible. Evite contabilizar dos veces conceptos como la inversión inicial o el valor residual.

Si permite ingresar tasas con una periodicidad diferente a la de los flujos, deberá realizar la conversión correspondiente. Si solo acepta una modalidad de tasa, deberá indicarlo claramente y orientar al usuario sobre el dato requerido.

3. Indicadores financieros obligatorios

Valor Presente Neto —VPN—. Calcule el valor presente de los flujos futuros y considere por separado el flujo del momento cero. Explique qué implica obtener un VPN positivo, negativo o igual a cero para la tasa de descuento utilizada.

Tasa Interna de Retorno —TIR—. Calcule la tasa que hace que el VPN sea igual a cero y compárela con una tasa de descuento expresada en la misma periodicidad. Cuando no pueda obtenerse una TIR válida o existan condiciones que puedan producir múltiples tasas, la herramienta deberá advertirlo y evitar una recomendación automática basada únicamente en este indicador.

Relación beneficio-costo —B/C—. Calcule la relación entre el valor presente de los beneficios y el valor presente de los costos, incluida la inversión inicial según la clasificación adoptada. Explique qué conceptos integra en cada componente. Para este indicador se requiere conservar la separación entre beneficios y costos; no basta con utilizar únicamente los flujos netos.

Periodo de recuperación simple y descontado. Determine cuándo se recupera la inversión mediante los flujos acumulados, sin descuento y con descuento, respectivamente. Si no se recupera dentro del horizonte analizado, deberá indicarlo. Si utiliza fracciones de periodo, explique el supuesto empleado para estimarlas.

En todos los casos, presente el resultado acompañado de una interpretación comprensible.

4. Comparación y recomendación

Incluya una sección que reúna los indicadores de las alternativas y facilite su comparación.

Para alternativas mutuamente excluyentes, con igual horizonte y condiciones comparables, la recomendación deberá considerar el VPN y explicar las posibles diferencias frente a la TIR. No seleccione automáticamente un proyecto solo por presentar la TIR más alta o el menor tiempo de recuperación.

Cuando los proyectos tengan horizontes distintos, el aplicativo deberá advertir que la comparación requiere un tratamiento adicional. Puede incorporar un procedimiento de comparación, siempre que explique sus supuestos y condiciones de aplicación.

La recomendación también deberá reconocer factores como el riesgo, la disponibilidad de recursos y la confiabilidad de las proyecciones.

5. Análisis de sensibilidad

Permita modificar, como mínimo:

La tasa de descuento.
Una variable operativa relevante, como los ingresos o los costos.
Presente un escenario base, uno favorable y uno desfavorable. Los cambios deben trasladarse automáticamente a los flujos o a los cálculos correspondientes.

Explique cómo estas variaciones afectan el VPN y si modifican la recomendación. Los escenarios deberán construirse mediante supuestos explícitos y coherentes.

6. Funcionalidad y controles

El aplicativo deberá:

Diferenciar visualmente las celdas de entrada, las fórmulas y los resultados.
Actualizar los cálculos al cambiar los datos.
Validar datos incompletos, valores no numéricos y periodos fuera de la capacidad admitida.
Advertir inconsistencias entre tasas y periodicidades.
Presentar mensajes claros cuando un indicador no pueda calcularse.
Evitar que un error se oculte como cero o se interprete como un resultado válido.
Incluir tablas o gráficos que ayuden a interpretar los flujos y los resultados.
Facilitar la navegación y proteger las fórmulas frente a modificaciones accidentales, sin impedir su revisión académica.
No es obligatorio utilizar macros. Se valorará el funcionamiento y la claridad de la solución, independientemente de las herramientas de Excel empleadas.

7. Validación de resultados

Incluya una hoja denominada Pruebas, con al menos seis casos que permitan comprobar:

Un proyecto con VPN positivo.
Un proyecto con VPN negativo.
Un proyecto que no recupere la inversión dentro del horizonte.
Un cambio en el número de periodos y en los flujos.
Una situación en la que la TIR no pueda interpretarse de manera convencional.
Una entrada incompleta o inválida que active un mensaje de control.
Para cada caso, registre los datos utilizados, el resultado esperado, el resultado del aplicativo y la conclusión de la prueba. Verifique cada indicador obligatorio al menos una vez.

Los resultados de referencia deberán obtenerse mediante un procedimiento independiente del cálculo que se está comprobando. Duplicar la misma fórmula en dos columnas no constituye una validación suficiente.

8. Manual de uso

Incluya una hoja denominada Manual, con:

Propósito y alcance de la herramienta.
Requisitos de uso y versión de Excel utilizada.
Explicación de cada dato de entrada.
Instrucciones para evaluar y comparar proyectos.
Convenciones de signos, tasas y periodos.
Interpretación de los indicadores.
Descripción de los escenarios.
Mensajes de validación y forma de corregir las entradas.
Capacidad máxima y limitaciones.
Fuentes consultadas y referencias en normas APA 7.
9. Caso demostrativo

Presente un caso de elaboración propia que compare dos alternativas reales o hipotéticas. El sector, la organización y el tipo de inversión serán de libre elección.

El caso deberá incluir los datos, los supuestos, los resultados, el análisis de sensibilidad y una recomendación sustentada. Si utiliza información hipotética, identifíquela expresamente.

Este caso demostrará el funcionamiento del aplicativo; la herramienta deberá seguir siendo utilizable con otros datos sin modificar sus fórmulas.

10. Entregable y presentación

Entregue un archivo de Excel que contenga:

Portada e identificación de los autores.
Manual de uso.
Datos de entrada y flujos de caja.
Cálculos e indicadores.
Comparación de alternativas.
Análisis de sensibilidad.
Pruebas de validación.
Caso demostrativo, conclusiones y referencias.
Puede organizar las secciones en las hojas que considere necesarias, siempre que sean fáciles de localizar.

Nombre del archivo: Trabajo_Final_Evaluacion_Inversiones_Apellido1_Apellido2.xlsx. Si utiliza macros, entregue el archivo en formato .xlsm.

Antes de enviarlo, compruebe que abre correctamente, que conserva las fórmulas y que no depende de vínculos externos inaccesibles. La entrega se realizará exclusivamente mediante el aula virtual.
