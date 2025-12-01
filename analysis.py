# analysis.py
# Author contact: 24f1000043@ds.study.iitm.ac.in
# Marimo notebook demonstrating interactive data analysis with reactive cells.
# Save as analysis.py and open with `uvx marimo edit analysis.py`

# %% 
# Cell 1 — Libraries & small helper functions (no direct dependencies on widget)
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Helper: create a synthetic dataset with controllable noise & size
def make_dataset(n=200, noise=1.0, random_state=0):
    """Return a DataFrame with two related variables x and y.
    y is approximately linear in x with added Gaussian noise.
    """
    rng = np.random.default_rng(random_state)
    x = rng.uniform(0, 10, size=n)
    y = 2.5 * x + rng.normal(0, noise, size=n)  # linear relation with slope 2.5
    return pd.DataFrame({"x": x, "y": y})

# Note: this cell defines functions used by downstream cells (data flow comment).

# %%
# Cell 2 — Interactive controls (slider widget)
import marimo as mo

# Slider controlling the dataset size (n) and noise level
n_slider = mo.ui.slider(50, 2000, value=200, step=10, label="Sample size (n)")
noise_slider = mo.ui.slider(0.1, 5.0, value=1.0, step=0.1, label="Noise (std dev)")

# Document the connection: changes to n_slider or noise_slider will cause dependent cells to re-run.

# %% 
# Cell 3 — Create dataset (depends on sliders)
# Data flow: this cell *depends on* n_slider and noise_slider. When either changes,
# this cell re-executes and downstream analysis (correlation, plots) updates automatically.
n = int(n_slider.value)
noise = float(noise_slider.value)

df = make_dataset(n=n, noise=noise, random_state=42)  # reactive dataset

# Show a quick preview (Marimo will render the dataframe)
df.head()

# %% 
# Cell 4 — Analysis & Dynamic Markdown (depends on df)
# Compute descriptive statistics and correlation which depend on the dataset created above.
mean_x = df["x"].mean()
mean_y = df["y"].mean()
corr = df["x"].corr(df["y"])

# Display a dynamic summary using Marimo's markdown helper. The content updates with sliders.
mo.md(f"""
# Interactive Analysis Summary

- **Sample size (n):** {n}  
- **Noise (std dev):** {noise:.2f}  
- **Mean x:** {mean_x:.3f}  
- **Mean y:** {mean_y:.3f}  
- **Pearson correlation (x, y):** **{corr:.3f}**

_Interpretation:_ Correlation should be high and close to 1 when noise is small, and decrease as noise increases.
""")

# %% 
# Cell 5 — Scatter plot (depends on df)
# Plot the relationship — this visual updates when the sliders change.
fig, ax = plt.subplots(figsize=(6, 4))
ax.scatter(df["x"], df["y"], alpha=0.6)
ax.set_title(f"Scatter plot (n={n}, noise={noise:.2f})")
ax.set_xlabel("x")
ax.set_ylabel("y")

# Draw the true underlying line for reference
x_line = np.linspace(df["x"].min(), df["x"].max(), 200)
ax.plot(x_line, 2.5 * x_line, linestyle="--", label="true line (slope=2.5)")
ax.legend()

# If Marimo auto-renders matplotlib figures, this will appear inline and update reactively.
plt.show()

# %% 
# Cell 6 — Optional: filter effect demo (depends on df)
# Demonstrates adding another dependent value derived from df (e.g., high-x subset)
threshold = mo.ui.slider(2.0, 8.0, value=5.0, step=0.1, label="x threshold for subset")
subset = df[df["x"] >= threshold.value]  # dependent on threshold and df

mo.md(f"""
## Subset analysis (x ≥ {threshold.value:.2f})

- Subset size: {len(subset)}
- Subset correlation: {subset['x'].corr(subset['y']):.3f}
""")

# End of notebook
