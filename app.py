import matplotlib.pyplot as plt

# -----------------------------
# Datos (en porcentajes)
# -----------------------------
# Riesgos absolutos
suture_est     = 1.644
suture_lower   = 0.215
suture_upper   = 3.0745

adhesive_est   = 1.9737
adhesive_lower = 0.4101
adhesive_upper = 3.5373

# Diferencia de riesgos (Adhesive - Suture)
diff_est   = 0.33
diff_lower = -1.79
diff_upper =  2.45

# Margen de no inferioridad
delta = 3.0  # 3%

# -----------------------------
# Creación de figura y subplots
# -----------------------------
fig, axes = plt.subplots(nrows=1, ncols=2, figsize=(7, 3), facecolor='white')
ax1, ax2 = axes

# ============ Subplot 1: Riesgos absolutos ============
# Coordinadas Y muy cercanas
y_suture   = 0.02
y_adhesive = -0.02

# Sutura
ax1.errorbar(
    x=suture_est,
    y=y_suture,
    xerr=[[suture_est - suture_lower], [suture_upper - suture_est]],
    fmt='o',
    color='black',
    ecolor='black',
    elinewidth=2,
    capsize=5,
    label='Suture (95% CI)'
)

# Adhesivo
ax1.errorbar(
    x=adhesive_est,
    y=y_adhesive,
    xerr=[[adhesive_est - adhesive_lower], [adhesive_upper - adhesive_est]],
    fmt='o',
    color='black',
    ecolor='black',
    elinewidth=2,
    capsize=5,
    label='Adhesive (95% CI)'
)

# Etiquetas y formato del subplot izquierdo
ax1.set_title('Absolute Risk (%)', fontsize=11, color='black')
ax1.set_xlabel('Incidence (%)', fontsize=10, color='black')

# Ajustamos las marcas y etiquetas en Y
ax1.set_yticks([y_adhesive, y_suture])
ax1.set_yticklabels(['Adhesive', 'Suture'], color='black')

# Ajustamos los límites en X para que quepan los IC
xmin_abs = min(suture_lower, adhesive_lower) - 1.0
xmax_abs = max(suture_upper, adhesive_upper) + 1.0
ax1.set_xlim(xmin_abs, xmax_abs)

# Quitamos las líneas superior y derecha
ax1.spines['top'].set_visible(False)
ax1.spines['right'].set_visible(False)

ax1.legend(loc='best', frameon=False, fontsize=9)

# ============ Subplot 2: Diferencia de riesgos ============
y_diff = 0  # Se representa en Y=0

ax2.errorbar(
    x=diff_est,
    y=y_diff,
    xerr=[[diff_est - diff_lower], [diff_upper - diff_est]],
    fmt='o',
    color='black',
    ecolor='black',
    elinewidth=2,
    capsize=5,
    label='Risk difference (95% CI)'
)

# Línea vertical para el margen de no inferioridad
ax2.axvline(
    x=delta,
    color='black',
    linestyle='--',
    linewidth=1.5,
    label=f'Non-inferiority margin = {delta}%'
)

# Línea vertical para 0%
ax2.axvline(
    x=0,
    color='gray',
    linestyle=':',
    linewidth=1.0,
    label='No difference (0%)'
)

# Etiquetas y formato del subplot derecho
ax2.set_title('Absolute Risk Difference', fontsize=11, color='black')
ax2.set_xlabel('(Adhesive − Suture) [%]', fontsize=10, color='black')

# Ocultamos las marcas del eje Y en el segundo subplot
ax2.set_yticks([y_diff])
ax2.set_yticklabels([''])

# Ajustamos límites en X
xmin_diff = min(diff_lower - 1.0, 0)
xmax_diff = max(diff_upper + 1.0, delta + 1.0)
ax2.set_xlim(xmin_diff, xmax_diff)

# Quitamos las líneas superior, derecha y opcionalmente la izquierda
ax2.spines['top'].set_visible(False)
ax2.spines['right'].set_visible(False)
ax2.spines['left'].set_visible(False)

ax2.legend(loc='best', frameon=False, fontsize=9)

# -----------------------------
# Ajustes finales y mostrar
# -----------------------------
plt.tight_layout()
plt.show()
