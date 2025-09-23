
import os
import numpy as np
import matplotlib.pyplot as plt
from astropy.constants import h, c, k_B
from astropy import units as u
from scipy.constants import golden

plt.style.use('pres_sty.mplstyle')
path_to_save = '../figures/'

width = 6.50127 / 1.6
height = width / golden / 1.2

print('Planck constant: ', h)
print('Speed of light: ', c)
print('Boltzman constant: ', k_B)

nu = np.linspace(1e11, 1e14, 1000) * u.Hz
# nu = np.linspace(400, 800, 1000) * u.MHz

T = 150 * u.K

rayleigh_jeans = 2 * k_B * T * nu ** 2 / c ** 2
wien = 2 * h * nu ** 3 / c ** 2 * np.exp(-h * nu / (k_B * T))
planck = 2 * h * nu ** 3 / c ** 2 / (np.exp(h * nu / (k_B * T)) - 1)

# Wien's law
b = 2898 * u.um * u.K
nu_max = (c / (b / T))
S_max = 2 * h * nu_max ** 3 / c ** 2 / (np.exp(h * nu_max / (k_B * T)) - 1)

fig, ax = plt.subplots(figsize=(width, height))
fig.subplots_adjust(left=.16, bottom=.19, right=.99, top=.99)

ax.plot(
    nu.to_value(u.THz),
    wien.to_value(u.J * u.s ** 3 * u.Hz ** 3 / u.m ** 2),
    label='Wien',
    lw=.5, ls=":", c="k"
    )
ax.plot(
    nu.to_value(u.THz),
    rayleigh_jeans.to_value(u.J * u.s ** 3 * u.Hz ** 3 / u.m ** 2),
    label='Rayleigh-Jeans',
    lw=.5, ls='--', c="k"
    )
ax.plot(
    nu.to_value(u.THz),
    planck.to_value(u.J * u.s ** 3 * u.Hz ** 3 / u.m ** 2),
    label='Planck',
    lw=1, c="k"
    )

ax.text(
    x=nu_max.to_value(u.THz) * 1.2,
    y=S_max.to_value(u.J * u.s ** 3 * u.Hz ** 3 / u.m ** 2),
    s=" ".join((f"$T={T.to_value(u.K)}$", "\\si{\\kelvin}")),
    fontsize=7
    )

ax.set_xlabel('Frequency \\si{\\tera\\hertz}')
ax.set_ylabel('Spectral flux density \\si{\\joule\\s^3\\hertz^3\\per\\m\\squared}')

ax.set_xscale('log')
ax.set_yscale('log')

ax.legend(loc='upper left')
fig.savefig(os.path.join(path_to_save, 'planck.pdf'))
# plt.show()
