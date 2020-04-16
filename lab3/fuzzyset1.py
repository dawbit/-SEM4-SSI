import pandas as pd
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

naslonecznienie = [("Warszawa", 0.6), ("Kraków", 1.0), ("Gdańsk", 0.9), ("Wrocław", 0.8), ("Katowice", 0.3),
                   ("Poznań", 0.7), ("Gliwice", 0.3)]
zanieczyszczenie = [("Warszawa", 0.3), ("Kraków", 0.1), ("Gdańsk", 0.9), ("Wrocław", 0.7), ("Katowice", 0.1),
                    ("Poznań", 0.6), ("Gliwice", 0.1)]
df = pd.read_csv('DaneMiast.csv', sep=";")

# Generate universe variables
#   * Insolation and toxicity on subjective ranges [0, 10]
#   * lif has a range of [0, 1] in units of percentage points
x_tox = np.arange(0, 1.01, 0.01)
x_sun = np.arange(0, 1.01, 0.01)
x_lif = np.arange(0, 1.01, 0.01)
# Generate fuzzy membership functions
qual_lo = fuzz.trimf(x_tox, [0, 0, 0.5])
qual_md = fuzz.trimf(x_tox, [0, 0.5, 1])
qual_hi = fuzz.trimf(x_tox, [0.5, 1, 1])
sun_lo = fuzz.trimf(x_sun, [0, 0, 0.5])
sun_md = fuzz.trimf(x_sun, [0, 0.5, 1])
sun_hi = fuzz.trimf(x_sun, [0.5, 1, 1])
lif_lo = fuzz.trimf(x_lif, [0, 0, 0.5])
lif_md = fuzz.trimf(x_lif, [0, 0.5, 1])
lif_hi = fuzz.trimf(x_lif, [0.5, 1, 1])

# Visualize these universes and membership functions
fig, (ax0, ax1, ax2) = plt.subplots(nrows=3, figsize=(10, 10))

ax0.plot(x_tox, qual_lo, 'b', linewidth=1.5, label='Mało')
ax0.plot(x_tox, qual_md, 'g', linewidth=1.5, label='Średnio')
ax0.plot(x_tox, qual_hi, 'r', linewidth=1.5, label='Dużo')
ax0.set_title('Air toxicity')
ax0.legend()

ax1.plot(x_sun, sun_lo, 'b', linewidth=1.5, label='Mało')
ax1.plot(x_sun, sun_md, 'g', linewidth=1.5, label='Średnio')
ax1.plot(x_sun, sun_hi, 'r', linewidth=1.5, label='Dużo')
ax1.set_title('Sun quantity')
ax1.legend()

ax2.plot(x_lif, lif_lo, 'b', linewidth=1.5, label='Low')
ax2.plot(x_lif, lif_md, 'g', linewidth=1.5, label='Medium')
ax2.plot(x_lif, lif_hi, 'r', linewidth=1.5, label='High')
ax2.set_title('Life standard')
ax2.legend()

# Turn off top/right axes
for ax in (ax0, ax1, ax2):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()

# We need the activation of our fuzzy membership functions at these values.
# The exact values  do not exist on our universes...
# This is what fuzz.interp_membership exists for!
tox_level_lo = fuzz.interp_membership(x_tox, qual_lo, 0.1)
tox_level_md = fuzz.interp_membership(x_tox, qual_md, 0.1)
tox_level_hi = fuzz.interp_membership(x_tox, qual_hi, 0.1)

sun_level_lo = fuzz.interp_membership(x_sun, sun_lo, 0.3)
sun_level_md = fuzz.interp_membership(x_sun, sun_md, 0.3)
sun_level_hi = fuzz.interp_membership(x_sun, sun_hi, 0.3)

# Now we take our rules and apply them. Rule 1 concerns low toxicity OR high insolation.
# The OR operator means we take the maximum of these two.
active_rule1 = sun_level_hi * tox_level_lo

# Now we apply this by clipping the top off the corresponding output
# membership function with `np.fmin`
lif_activation_hi = np.fmin(active_rule1, lif_hi)  # removed entirely to 0
lif0 = np.zeros_like(x_lif)

# For better visualization
# If toxicity is high and insolation is low then "life" is lo
active_rule2 = tox_level_hi * sun_level_lo
lif_activation_lo = np.fmin(active_rule2, lif_lo)

# Rule 3, if toxicity medium and isolation medium then "life" is medium
active_rule3 = sun_level_md * tox_level_md
lif_activation_md = np.fmin(active_rule3, lif_md)

# Visualize this
fig, ax0 = plt.subplots(figsize=(8, 3))
ax0.fill_between(x_lif, lif0, lif_activation_hi, facecolor='b', alpha=0.7)
ax0.plot(x_lif, lif_hi, 'g', linewidth=0.5, linestyle='--', )
ax0.set_title('Output membership activity')
ax0.fill_between(x_lif, lif0, lif_activation_lo, facecolor='g', alpha=0.7)
ax0.plot(x_lif, lif_lo, 'b', linewidth=0.5, linestyle='--')
ax0.fill_between(x_lif, lif0, lif_activation_md, facecolor='r', alpha=0.7)
ax0.plot(x_lif, lif_md, 'r', linewidth=0.5, linestyle='--')

# Turn off top/right axes
for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()

# Aggregate all three output membership functions together
aggregated = np.fmax(lif_activation_hi, lif_activation_md,
                     lif_activation_lo)  # Małe oszustwo, powinna być kolejna funkcja nie 0

# Calculate defuzzified result
lif = fuzz.defuzz(x_lif, aggregated, 'centroid')
lif_activation = fuzz.interp_membership(x_lif, aggregated, lif)  # for plot

# Visualize this
fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.plot(x_lif, lif_lo, 'b', linewidth=0.5, linestyle='--', )
ax0.plot(x_lif, lif_md, 'g', linewidth=0.5, linestyle='--')
ax0.plot(x_lif, lif_hi, 'r', linewidth=0.5, linestyle='--')
ax0.fill_between(x_lif, lif0, aggregated, facecolor='Orange', alpha=0.7)
ax0.plot([lif, lif], [0, lif_activation], 'k', linewidth=1.5, alpha=0.9)
ax0.set_title('Aggregated membership and result (line)')

# Turn off top/right axes
for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
print(lif)

i, j = df.shape
for row in range(i):
    a = df.at[row, "Naslonecznienie"]
    b = df.at[row, "Zanieczyszczenie"]
    tox_level_lo = fuzz.interp_membership(x_tox, qual_lo, b)
    tox_level_md = fuzz.interp_membership(x_tox, qual_md, b)
    tox_level_hi = fuzz.interp_membership(x_tox, qual_hi, b)

    sun_level_lo = fuzz.interp_membership(x_sun, sun_lo, a)
    sun_level_md = fuzz.interp_membership(x_sun, sun_md, a)
    sun_level_hi = fuzz.interp_membership(x_sun, sun_hi, a)
    # Zasada 1, cel zadania
    active_rule1 = sun_level_hi * tox_level_lo
    lif_activation_hi = np.fmin(active_rule1, lif_hi)
    lif0 = np.zeros_like(x_lif)
    # Zasada 2, przeciwieństwo celu zadania
    active_rule2 = tox_level_hi * sun_level_lo
    lif_activation_lo = np.fmin(active_rule2, lif_lo)

    # Zasada 3,  medium and medium then low
    active_rule3 = sun_level_md * tox_level_md
    lif_activation_md = np.fmin(active_rule3, lif_lo)

    aggregated = np.fmax(lif_activation_lo,
                         np.fmax(lif_activation_md, lif_activation_hi))
    lif = fuzz.defuzz(x_lif, aggregated, 'centroid')
    df.at[row, "JakoscZycia"] = lif
    print(lif)

print(df)
