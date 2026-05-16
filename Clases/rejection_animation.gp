# Configuración del terminal para salida GIF animada
set terminal gif size 800,500 animate delay 30 optimize
set output "rejection_animation.gif"

# Ejes, etiquetas y malla de referencia
set title "Proceso de Aceptación y Rechazo" font ",14"
set xlabel "x" font ",12"
set ylabel "y" font ",12"
set xrange [0:1]
set yrange [0:2.6]
set grid
set key top right

# Definición analítica de la densidad objetivo y la envolvente
target_density(x) = 30.0 * x * (1.0 - x)**4
envelope_function(x) = 2.5

# Estilos de línea y punto consistentes con el esquema visual previo
set style line 1 lc rgb '#00ff9d' lw 2
set style line 2 lc rgb '#8b8680' lw 1.5 dt 2
set style line 3 pt 7 ps 0.8 lc rgb '#00ff9d'
set style line 4 pt 7 ps 0.5 lc rgb '#4a4a4a'

# Parámetros de control de la animación
total_candidates = 5000
candidates_per_frame = 100
frame_count = total_candidates / candidates_per_frame

# Bucle de renderizado progresivo
do for [frame = 1:frame_count] {
    upper_index = frame * candidates_per_frame - 1
    plot target_density(x) with lines ls 1 title 'p(x)', \
         envelope_function(x) with lines ls 2 title 'f(x)', \
         'rejection_data.dat' every ::0::upper_index using ($3==1 ? $1 : 1/0):($3==1 ? $2 : 1/0) with points ls 3 title 'Aceptados', \
         'rejection_data.dat' every ::0::upper_index using ($3==0 ? $1 : 1/0):($3==0 ? $2 : 1/0) with points ls 4 title 'Rechazados'
}
