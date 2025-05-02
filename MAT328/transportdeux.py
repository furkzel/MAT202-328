import numpy as np
import matplotlib.pyplot as plt

t = np.linspace(0, 2, 200)

kappa_values = np.linspace(-2, 2, 15)

plt.figure(figsize=(10, 6))
for k in kappa_values:
    x = t**3 / 3 + k
    plt.plot(t, x, label=f"$\\kappa = {k:.2f}$")

plt.title("Lignes caractéristiques : $u_t + t^2 u_x = 0$")
plt.xlabel("Temps t")
plt.ylabel("Position x")
plt.grid(True)

plt.tight_layout()
plt.show()