import numpy as np
import matplotlib.pyplot as plt

x_min, x_max = 0.1, 3.1
y_min, y_max = 0.1, 3.1

x_dense = np.linspace(x_min, x_max, 400)
y_dense = np.linspace(y_min, y_max, 400)
X_dense, Y_dense = np.meshgrid(x_dense, y_dense)
Z = np.log(X_dense * Y_dense)

levels_c = [-1, 0, 1]
levels_xy_str = {
    -1: '$xy=1/e$ (c=-1)',
    0:  '$xy=1$   (c=0)',
    1:  '$xy=e$   (c=1)'
}
linestyles = ['dotted', 'solid', 'dashed']

n_vectors = 7
x_sparse = np.linspace(x_min + 0.2, x_max - 0.2, n_vectors)
y_sparse = np.linspace(y_min + 0.2, y_max - 0.2, n_vectors)
X_sparse, Y_sparse = np.meshgrid(x_sparse, y_sparse)
U = 1 / X_sparse
V = 1 / Y_sparse

norm = np.sqrt(U**2 + V**2)
U_norm = U / norm
V_norm = V / norm

fig, ax = plt.subplots(figsize=(8, 8))

contour_set = ax.contour(X_dense, Y_dense, Z, levels=levels_c, colors='blue', linestyles=linestyles)

ax.quiver(
    X_sparse, Y_sparse, U_norm, V_norm, color='red',
    angles='xy', scale_units='xy', scale=10, width=0.004
)

ax.plot(1, 1, 'ko', markersize=7)
ax.text(1.05, 1.05, '$(1,1)$', fontsize=12, verticalalignment='bottom')

x_tangent = np.linspace(x_min, 2, 100)
y_tangent = -x_tangent + 2
valid = (y_tangent >= y_min) & (y_tangent <= y_max) & (x_tangent <= x_max)
tangent_line, = ax.plot(
    x_tangent[valid], y_tangent[valid],
    color='green', linestyle='-', linewidth=1.5, label='Tengent: $y=-x+2$'
)

ax.set_xlabel('$x$', fontsize=12)
ax.set_ylabel('$y$', fontsize=12)
ax.set_xlim(x_min, x_max)
ax.set_ylim(y_min, y_max)
ax.set_aspect('equal', adjustable='box')
ax.grid(True, linestyle=':', alpha=0.7)

contour_handles = [
    plt.Line2D([0], [0], color='blue', lw=1.5, linestyle=ls, label=levels_xy_str[lvl])
    for lvl, ls in zip(levels_c, linestyles)
]
gradient_handle = plt.Line2D([0], [0], marker='>', color='red', markersize=6, linestyle='None', label='$\\nabla f = (1/x, 1/y)$')
all_handles = contour_handles + [tangent_line, gradient_handle]

ax.legend(handles=all_handles, loc='upper left', bbox_to_anchor=(1.02, 1))
plt.tight_layout(rect=[0, 0, 0.85, 1])

plt.show()

#plt.savefig('ln_xy_plot.svg', dpi=300, bbox_inches='tight')
