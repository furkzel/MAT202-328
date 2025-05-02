def initial_condition(x):
    u0 = np.zeros_like(x)
    nonzero_mask = x != 0
    u0[nonzero_mask] = 1 - np.exp(-1 / x[nonzero_mask] ** 2)
    return u0

from matplotlib import cm
from matplotlib.colors import Normalize

colors = cm.viridis
norm = Normalize(vmin=0, vmax=1)

plt.style.use('seaborn-v0_8-whitegrid')
fig, ax = plt.subplots(figsize=(9, 10))

for k in k_initial:
    sol = solve_ivp(characteristic_ode, t_span, [k], t_eval=t_eval, dense_output=True)
    u_value = initial_condition(np.array([k]))[0]
    color = colors(norm(u_value))
    ax.plot(sol.t, sol.y[0], color=color, linewidth=1.5)

for k in k_horizontal:
    ax.axhline(k, color='crimson', linestyle='--', linewidth=1.2)

ax.set(
    xlim=t_span,
    ylim=(-4, 4),
    xlabel='$t$',
    ylabel='$x$',
    title=r'Lignes Caracteristique et Condition Initiale: $u(0,x) = 1 - e^{-1/x^2}$'
)

ax.axvline(0, color='black', linewidth=0.8)

sm = cm.ScalarMappable(cmap=colors, norm=norm)
cbar = fig.colorbar(sm, ax=ax, pad=0.02)
cbar.set_label(r'$u(0,x_0)$ Value', rotation=270, labelpad=15)

plt.tight_layout()

#plt.savefig('karakteristik_baslangidddc_renkli.svg', format='svg', bbox_inches='tight')