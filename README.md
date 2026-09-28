# n-th Roots of Unity Visualizer

A Python tool to calculate, plot, and geometrically visualize the **$n$-th roots of unity** ($z^n = 1$) on the complex plane.

---

## 📌 Mathematical Background

According to Euler's formula, the $n$-th roots of unity are given by:

$$z_k = e^{i \frac{2\pi k}{n}} = \cos\left(\frac{2\pi k}{n}\right) + i \sin\left(\frac{2\pi k}{n}\right), \quad k = 0, 1, \dots, n-1$$

### Key Properties
* **Unit Circle:** All roots lie on the circle $\vert{}z\vert{} = 1$.
* **Regular Polygon:** Connecting adjacent roots forms a regular $n$-sided polygon ($n$-gon).
* **Equally Spaced:** The angular distance between consecutive roots is $\Delta\theta = \frac{2\pi}{n}$.
## 📊 Visual Outputs

| 3rd Root of Unity ($n=3$) | 4th Root of Unity ($n=4$) |
| :---: | :---: |
| **Cube Roots**<br>![3rd Root]<img width="700" height="700" alt="3rd root of unity" src="https://github.com/user-attachments/assets/5da443f2-8ae9-4dcf-b815-874ce270787f" />
| **Fourth Roots**<br>![4th Root]<img width="700" height="700" alt="4th root of unity" src="https://github.com/user-attachments/assets/a72b5a08-25e0-4f5e-bce4-dae510bd52ee" />
 |

| 5th Root of Unity ($n=5$) | 8th Root of Unity ($n=8$) |
| :---: | :---: |
| **Pentagon Roots**<img width="700" height="700" alt="5th root of unity" src="https://github.com/user-attachments/assets/f393ab98-6538-4c92-885f-edb0b8ee7b7b" />
 | **Octagon Roots**<br>![8th Root]<img width="700" height="700" alt="8th root of unity" src="https://github.com/user-attachments/assets/d0dede4f-af6a-42cf-baa2-1e33f653f812" />
 |
---

## 💻 Source Code

```python
import numpy as np
import matplotlib.pyplot as h

def plot_roots_of_unity(n):
    # Compute arguments and complex roots
    k = np.arange(n)
    angles = 2 * np.pi * k / n
    roots = np.exp(1j * angles)

    x = roots.real
    y = roots.imag

    # Close the polygon loop by repeating the first root
    x_polygon = np.append(x, x[0])
    y_polygon = np.append(y, y[0])

    h.figure(figsize=(7, 7))

    # Plot Unit Circle
    circle_angles = np.linspace(0, 2 * np.pi, 200)
    h.plot(np.cos(circle_angles), np.sin(circle_angles), 'k--', label='Unit Circle')

    # Plot Polygon and Root Points
    h.plot(x_polygon, y_polygon, 'b--', label=f'{n}-gon')
    h.scatter(x, y, color='red', s=50, zorder=5, label='Roots')

    # Add radial lines and TeX labels
    for i, (rx, ry, angle) in enumerate(zip(x, y, angles)):
        h.plot([0, rx], [0, ry], 'g:', alpha=0.5)

        offset_x = 0.18 * np.cos(angle)
        offset_y = 0.18 * np.sin(angle)

        if i == 0:
            label_text = "1"
        else:
            label_text = f"$e^{{i \\frac{{2\\pi({i})}}{{{n}}}}}$"

        h.text(rx + offset_x, ry + offset_y, label_text, 
               fontsize=10, ha='center', va='center', color='darkblue')

    # Formatting
    h.axhline(0, color='gray', linewidth=0.8)
    h.axvline(0, color='gray', linewidth=0.8)

    h.gca().set_aspect('equal')
    h.xlim(-1.5, 1.5)
    h.ylim(-1.5, 1.5)
    h.title(f"{n}-th Roots Of Unity ($z^{{{n}}} = 1$)")
    h.xlabel("Re(z)")
    h.ylabel("Im(z)")
    h.grid(True, linestyle=':', alpha=0.6)
    h.legend(loc='upper right')
    h.tight_layout()
    h.show()


# Example usage
plot_roots_of_unity(8)
