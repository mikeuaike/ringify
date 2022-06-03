import matplotlib.pyplot as plt
import unsio.input as uns_in
import numpy as np
from sys import argv

snapshotIn = argv[1]

s = uns_in.CUNS_IN(snapshotIn, 'all')
s.nextFrame()

_, pos = s.getData('disk', 'pos')
_, id = s.getData('disk', 'id')
_, mass = s.getData('disk', 'mass')
x = pos[0::3]
y = pos[1::3]

# Number of Bodies
n_body = np.argmax(id)

# Find Center:
x_center = np.sum(x[0:9999]) / n_body
y_center = np.sum(y[0:9999]) / n_body

# Number of Rings
n = 25

R = np.sqrt(x**2 + y**2)
step = np.sqrt((x[np.argmax(x)]) ** 2 + (y[np.argmax(y)]) ** 2) / n

# Initial Boundaries
R1 = np.sqrt(x_center**2 + y_center**2)
R2 = R1 + step

print('Step: ', step, ' kparsec')
density_array = []


print('Center: ', 'x = ', x_center, 'y = ', y_center)
# Iteration
i = 0
for i in range(0, n):
    cond = np.argwhere((R >= R1) & (R < R2)).flatten()
    sum_mass = np.sum(mass[cond])
    density = sum_mass / (np.pi*(R2 ** 2 - R1 ** 2)) * 10000000000
    density_array.append(density)
    print('ring ', i, ':', density, 'sun_mass e^10 kpa^-2')
    i = i + 1
# move boundaries
    R1 = R2
    R2 = R2 + step


# plot!
x_axis = np.arange(n) * step
y_axis = np.array(density_array)

fig, ax = plt.subplots()
ax.plot(x_axis, y_axis)

plt.title("Density along concentric rings of the Galactic Disk")
plt.xlabel("Ring Radius [kpa]")
plt.ylabel("Density [Msun e^10 kpa^(-2)]")
plt.grid()
plt.xscale("log")
plt.yscale("log")
plt.show()
