import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation
from matplotlib.animation import PillowWriter

# Données orbitales
orbites = {
    "Vénus": {"a": 0.72, "e": 0.0068, "color": "orange", "periode": 224.7},
    "Terre": {"a": 1.0, "e": 0.0167, "color": "blue", "periode": 365.25},
    "Mars": {"a": 1.52, "e": 0.0934, "color": "red", "periode": 687.0}
}

theta = np.linspace(0, 2 * np.pi, 500)
jours = np.linspace(0, 7300, 300)  # 20 ans ≈ 7300 jours

# Figure
fig, ax = plt.subplots(figsize=(8, 8))
points = {}
for planete, data in orbites.items():
    a, e, color = data["a"], data["e"], data["color"]
    r = a * (1 - e**2) / (1 + e * np.cos(theta))
    x = r * np.cos(theta) - a * e
    y = r * np.sin(theta)
    ax.plot(x, y, linestyle='--', color=color, alpha=0.4)
    points[planete], = ax.plot([], [], 'o', color=color, label=planete)

ax.plot(0, 0, 'yo', label='Soleil')
ax.set_xlim(-1.8, 1.8)
ax.set_ylim(-1.8, 1.8)
ax.set_aspect('equal')
ax.grid(True)
ax.set_title("Orbites de 2005 à 2025")
ax.set_xlabel("UA")
ax.set_ylabel("UA")
ax.legend()

def update(frame):
    jour = jours[frame]
    for planete, data in orbites.items():
        a, e, T = data["a"], data["e"], data["periode"]
        theta_pos = 2 * np.pi * jour / T
        r = a * (1 - e**2) / (1 + e * np.cos(theta_pos))
        x = r * np.cos(theta_pos) - a * e
        y = r * np.sin(theta_pos)
        points[planete].set_data([x], [y])  # <- correction ici
    return points.values()

ani = animation.FuncAnimation(fig, update, frames=len(jours), blit=True, interval=50)
ani.save("orbites_2005_2025.gif", writer=PillowWriter(fps=20))