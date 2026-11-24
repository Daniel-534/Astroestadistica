"""Problema 2: relacion periodo-luminosidad de Cefeidas (regresion bayesiana lineal)."""
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

rng = np.random.default_rng(2026)
sigma, tau2, N = 0.3, 10**2, 10_000

# Datos: M_V = V + 5 log10(plx) - 10
d = pd.read_csv("mw_cepheids_1_.csv", skiprows=[1, 2], skipinitialspace=True)
d = d.dropna(subset=["Per", "plx", "Vmag"])
d = d[(d.Per > 0) & (d.plx > 0)]
x = np.log10(d.Per.to_numpy())
y = (d.Vmag + 5 * np.log10(d.plx) - 10).to_numpy()
X = np.column_stack((np.ones_like(x), x))
print("m =", len(x))

# a) dispersion
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(x, y)
ax.invert_yaxis()
ax.set(xlabel=r"$\log_{10}P$", ylabel="$M_V$", title="a) Datos")
fig.tight_layout()

# b-e) posterior normal bivariada (MAP = media)
Sigma = np.linalg.inv(X.T @ X / sigma**2 + np.eye(2) / tau2)
mu = Sigma @ X.T @ y / sigma**2
print("d,e) MAP/media (a,b) =", mu.round(4))
print("e) Sigma =\n", Sigma.round(6))

# f) muestras posteriores
s = rng.multivariate_normal(mu, Sigma, N)

# g) intervalos 95%
q = np.quantile(s, [0.025, 0.975], axis=0)
print("g) a:", q[:, 0].round(4), " b:", q[:, 1].round(4))

# h) P = 12 d
x12 = np.array([1, np.log10(12)])
m12 = s @ x12
pred = m12 + rng.normal(0, sigma, N)
print(f"h) media={m12.mean():.4f}  IC media={np.quantile(m12, [.025, .975]).round(4)}")
print(f"   predictiva IC 95%={np.quantile(pred, [.025, .975]).round(4)}")

# i) recta MAP + banda 95%
xg = np.linspace(x.min(), x.max(), 200)
curves = s[:, [0]] + s[:, [1]] * xg
lo, hi = np.quantile(curves, [0.025, 0.975], axis=0)
fig, ax = plt.subplots(figsize=(7, 5))
ax.scatter(x, y, label="Datos")
ax.plot(xg, mu[0] + mu[1] * xg, "r", label="Recta MAP")
ax.fill_between(xg, lo, hi, alpha=0.3, label="Banda 95%")
ax.invert_yaxis()
ax.set(xlabel=r"$\log_{10}P$", ylabel="$M_V$", title="i) Relación P-L")
ax.legend()
fig.tight_layout()

# j) OLS
ols = np.linalg.lstsq(X, y, rcond=None)[0]
cov_ols = sigma**2 * np.linalg.inv(X.T @ X)   # sigma conocida
se = np.sqrt(np.diag(cov_ols))
print("j) OLS (a,b) =", ols.round(4), " IC95% OLS a:",
      (ols[0] + 1.96 * se[0] * np.array([-1, 1])).round(4),
      " b:", (ols[1] + 1.96 * se[1] * np.array([-1, 1])).round(4))
plt.show()
