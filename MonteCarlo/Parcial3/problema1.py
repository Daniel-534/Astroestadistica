"""Problema 1: exoplanetas, modelo Beta-Binomial."""
import matplotlib.pyplot as plt
import numpy as np
from scipy.stats import beta

rng = np.random.default_rng(2026)
n, x = 100, 18
a0, b0 = 4, 16
a1, b1 = a0 + x, b0 + n - x            # posterior Beta(22, 98)
th = np.linspace(1e-4, 1 - 1e-4, 1000)

# a) verosimilitud (relativa al maximo)
ll = x * np.log(th) + (n - x) * np.log1p(-th)
lik = np.exp(ll - ll.max())

# b) prior
prior = beta.pdf(th, a0, b0)

# c) posterior
post = beta.pdf(th, a1, b1)

# d) media, varianza, moda
media = a1 / (a1 + b1)
var = a1 * b1 / ((a1 + b1) ** 2 * (a1 + b1 + 1))
moda = (a1 - 1) / (a1 + b1 - 2)
print(f"d) media={media:.4f}  var={var:.6f}  moda={moda:.4f}")

# e) Monte Carlo
s = rng.beta(a1, b1, 10_000)

# f) intervalo creible 95%
print("f) IC 95% MC      :", np.quantile(s, [0.025, 0.975]).round(4))
print("   IC 95% analitico:", beta.ppf([0.025, 0.975], a1, b1).round(4))

# g) P(theta > 0.20 | datos)
print(f"g) P(theta>0.2) MC={np.mean(s > 0.2):.4f}  exacta={beta.sf(0.2, a1, b1):.4f}")

# graficos
fig, ax = plt.subplots(1, 2, figsize=(10, 4))
ax[0].plot(th, lik)
ax[0].set(xlabel=r"$\theta$", ylabel="Verosimilitud relativa", title="a) Verosimilitud")
ax[1].plot(th, prior, label="Prior Beta(4,16)")
ax[1].plot(th, post, label="Posterior Beta(22,98)")
ax[1].hist(s, bins=60, density=True, alpha=0.3, label="MC")
ax[1].set(xlabel=r"$\theta$", ylabel="Densidad", title="Prior y posterior")
ax[1].legend()
fig.tight_layout()
plt.show()
