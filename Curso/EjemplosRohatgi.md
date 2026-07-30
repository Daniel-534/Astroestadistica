\section{Ejemplo 3: Medida de Probabilidad en un Espacio Continuo}

Sea $\Omega = (0, \infty)$ y $\mathcal{S} = \mathcal{B}$, la $\sigma$-álgebra de Borel en $\Omega$. Se define la función de conjunto $P$ de la siguiente manera: para cada intervalo $I \subseteq \Omega$,
$$P_I = \int_I e^{-x} dx$$

\subsection{Solución}

Para demostrar que $P$ es una medida de probabilidad válida en el espacio de probabilidad $(\Omega, \mathcal{S})$, verificamos que cumple con los axiomas de Kolmogorov establecidos en el texto:

\begin{enumerate}
    \item \textbf{No negatividad:} Dado que la función exponencial $e^{-x}$ es estrictamente positiva para todo $x \in (0, \infty)$, la integral sobre cualquier intervalo $I$ será no negativa. Por lo tanto, se cumple claramente que $P_I \ge 0$.
    \item \textbf{Normalización:} La probabilidad del espacio muestral completo $\Omega$ se calcula como:
    $$P_\Omega = \int_0^\infty e^{-x} dx = \left[ -e^{-x} \right]_0^\infty = 0 - (-1) = 1$$
    \item \textbf{Aditividad numerable:} Por las propiedades fundamentales del cálculo integral, la integral sobre una unión numerable de intervalos disjuntos es igual a la suma de las integrales sobre cada intervalo individual. Por lo tanto, $P$ es numerablemente aditiva.
\end{enumerate}

En conclusión, $P$ satisface todos los axiomas de probabilidad y define correctamente una medida de probabilidad en el espacio $(\Omega, \mathcal{S})$.



\section{El Problema del Cumpleaños}

Considere una clase de $r$ estudiantes. Las fechas de nacimiento de estos $r$ estudiantes forman una muestra de tamaño $r$ de los 365 días del año. Se desea encontrar la probabilidad de que todos los cumpleaños sean distintos y determinar la probabilidad de que el procedimiento de identificación termine en el $k$-ésimo estudiante.

\subsection{Solución}

La probabilidad de que los $r$ cumpleaños sean todos diferentes está dada por la fórmula de permutaciones:

$$q_r = \frac{_{365}P_r}{(365)^r}$$

Se puede demostrar que esta probabilidad es menor a $1/2$ si $r = 23$. La siguiente tabla proporciona los valores de $q_r$ para algunos valores seleccionados de $r$:

\begin{center}
\begin{tabular}{|c|c|c|c|c|c|c|}
\hline
$r$ & 20 & 23 & 25 & 30 & 35 & 60 \\
\hline
$q_r$ & 0.589 & 0.493 & 0.431 & 0.294 & 0.186 & 0.006 \\
\hline
\end{tabular}
\end{center}

A continuación, suponga que a cada uno de los $r$ estudiantes se le pregunta su fecha de nacimiento en orden, con la instrucción de que tan pronto como un estudiante escuche su fecha de nacimiento, debe levantar la mano. 

Sea $p_k$ la probabilidad de que el procedimiento termine (es decir, se levante una mano por primera vez) cuando al $k$-ésimo ($k = 1, 2, \dots, r$) estudiante se le pregunta su fecha de nacimiento. Entonces:

$$p_1 = 1 - \left(\frac{364}{365}\right)^{r-1}$$

y para $k = 2, 3, \dots, r$:

$$p_k = \frac{_{365}P_{k-1}}{(365)^{k-1}} \left(1 - \frac{k-1}{365}\right)^{r-k+1} \left[1 - \left(\frac{365-k}{365-k+1}\right)^{r-k}\right]$$
