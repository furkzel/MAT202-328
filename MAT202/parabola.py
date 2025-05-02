import numpy as np
import matplotlib.pyplot as plt

y = np.linspace(-2, 2, 100)

x = -0.25 * y**2

plt.figure(figsize=(6, 6))
plt.plot(y, x, 'b-', label=r'$x = -\frac{1}{4} y^2$')
plt.scatter([0], [0], color='black', zorder=5)
plt.text(0.1, 0.1, '$(0,0)$', fontsize=10)

plt.axhline(0, color='black', linewidth=0.5)
plt.axvline(0, color='black', linewidth=0.5)
plt.xlabel('$y$')
plt.ylabel('$x$')
plt.grid(True)
plt.legend()

plt.show()

# plt.savefig('parabola.svg', format='svg')