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
nread = s.getData('ndisk')
x = pos[0::3]
y = pos[1::3]
z = pos[2::3]

mass = mass * 1e10

# Number of Bodies
n_body = nread[1]

# Find Center:
x_com = np.sum(mass*x) / np.sum(mass)
y_com = np.sum(mass*y) / np.sum(mass)
z_com = np.sum(mass*z) / np.sum(mass)

# Array Shift:
for i in range(n_body-1):
    x[i] = x[i] - x_com
    y[i] = y[i] - y_com
    z[i] = z[i] - z_com

# Number of Rings
n = 25

R = np.sqrt(x**2 + y**2)
step = np.sqrt((x[np.argmax(x)]) ** 2 + (y[np.argmax(y)]) ** 2) / n

# Initial Boundaries
R1 = np.sqrt(x_com**2 + y_com**2)
R2 = R1 + step

print('Step: ', step, ' kpc')
density_array = []
theoric_array = []

print('Center: ', 'x = ', x_com, 'y = ', y_com)
# Density Iteration
i = 0
for i in range(0, n):
    cond = np.argwhere((R > R1) & (R < R2)).flatten()
    sum_mass = np.sum(mass[cond])
    density = sum_mass / (np.pi*(R2 ** 2 - R1 ** 2))
    density_array.append(density)
    print('ring ', i, ':', density, 'sun_mass 10^10 kpc^-2')

    i = i + 1
# move boundaries
    R1 = R2
    R2 = R2 + step

# Theoretical Curve

h = 3.5
m = 5 * 1e10

x_linspace = np.linspace(0, n*step, n)
theor_density = ((m / (np.pi * (h ** 2))) * np.exp((-x_linspace) / h)) / 2

# plot!

x_axis = np.arange(n) * step
y_axis = np.array(density_array)
fig, ax = plt.subplots()

ax.scatter(x_axis, y_axis, label='Densities from Snapshot', color='magenta')
ax.plot(x_linspace, theor_density, label='Analytic Curve of Density', color='blue')

plt.title("Density along Galactic Disk Radius")
plt.xlabel("Radius [${\mathrm{kpc}}$]")
plt.ylabel("Density [$10^{10}{\mathrm{M}}_{\odot}$ ${\mathrm{kpc}}^{-2}$]")
plt.grid()
plt.xscale("log")
plt.yscale("log")
plt.legend()

aux = (argv[1], 'DiskDensityProfile')
name = "_".join(aux)
plt.savefig(name)
plt.show()
