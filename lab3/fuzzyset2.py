import pandas as pd
import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

czasWolny = pd.DataFrame(np.array(
    [["poniedziałek", 0.6], ["wtorek", 0.6], ["środa", 0.5], ["czwartek", 0.5], ["piątek", 0.7], ["sobota", 0.8],
     ["niedziela", 0.9]]), columns=['dzien', 'wartosc'])
kosztyAktywn = pd.DataFrame(np.array(
    [["kino", 0.6], ["teatr", 0.7], ["restauracja", 0.9], ["sport na powietrzu", 0.2], ["sport w klubie", 0.6],
     ["basen", 0.3], ["czytanie", 0.1], ["film w domu", 0.1]]), columns=['aktywnosc', 'wartosc'])
poziomAktywn = pd.DataFrame(np.array(
    [["styczeń", 0.2], ["luty", 0.1], ["marzec", 0.5], ["kwiecień", 0.5], ["maj", 0.7], ["czerwiec", 0.8],
     ["lipiec", 0.9], ["sierpień", 0.9], ["wrzesień", 0.8], ["październik", 0.5], ["listopad", 0.3],
     ["grudzień", 0.2]]), columns=['miesiac', 'wartosc'])

print(czasWolny, kosztyAktywn, poziomAktywn)

# Generate universe variables
#   * Quality and service on subjective ranges [0, 1]
#   * life has a range of [0, 1] in units of percentage points
x_czasWolny = np.arange(0, 1.01, 0.01)
x_kosztAktywn = np.arange(0, 1.01, 0.01)
x_poziomAktywn = np.arange(0, 1.01, 0.01)
x_jakjest = np.arange(0, 1.01, 0.01)
# Generate fuzzy membership functions
czasWolny_lo = fuzz.trimf(x_czasWolny, [0, 0, 0.5])
czasWolny_md = fuzz.trimf(x_czasWolny, [0, 0.5, 1])
czasWolny_hi = fuzz.trimf(x_czasWolny, [0.5, 1, 1])
kosztAktywn_lo = fuzz.trimf(x_kosztAktywn, [0, 0, 0.5])
kosztAktywn_md = fuzz.trimf(x_kosztAktywn, [0, 0.5, 1])
kosztAktywn_hi = fuzz.trimf(x_kosztAktywn, [0.5, 1, 1])
poziomAktywn_lo = fuzz.trimf(x_kosztAktywn, [0, 0, 0.5])
poziomAktywn_md = fuzz.trimf(x_kosztAktywn, [0, 0.5, 1])
poziomAktywn_hi = fuzz.trimf(x_kosztAktywn, [0.5, 1, 1])
jakjest_lo = fuzz.trimf(x_jakjest, [0, 0, 0.5])
jakjest_md = fuzz.trimf(x_jakjest, [0, 0.5, 1])
jakjest_hi = fuzz.trimf(x_jakjest, [0.5, 1, 1])

# Visualize these universes and membership functions
fig, (ax0, ax1, ax2, ax3) = plt.subplots(nrows=4, figsize=(10, 10))

ax0.plot(x_czasWolny, czasWolny_lo, 'b', linewidth=1.5, label='Mało')
ax0.plot(x_czasWolny, czasWolny_md, 'g', linewidth=1.5, label='Średnio')
ax0.plot(x_czasWolny, czasWolny_hi, 'r', linewidth=1.5, label='Dużo')
ax0.set_title('czas wolny')
ax0.legend()

ax1.plot(x_kosztAktywn, kosztAktywn_lo, 'b', linewidth=1.5, label='Mało')
ax1.plot(x_kosztAktywn, kosztAktywn_md, 'g', linewidth=1.5, label='Średnio')
ax1.plot(x_kosztAktywn, kosztAktywn_hi, 'r', linewidth=1.5, label='Dużo')
ax1.set_title('koszt aktywnosci')
ax1.legend()

ax2.plot(x_poziomAktywn, poziomAktywn_lo, 'b', linewidth=1.5, label='Mało')
ax2.plot(x_poziomAktywn, poziomAktywn_md, 'g', linewidth=1.5, label='Średnio')
ax2.plot(x_poziomAktywn, poziomAktywn_hi, 'r', linewidth=1.5, label='Dużo')
ax2.set_title('poziom aktywnosci')
ax2.legend()

ax3.plot(x_jakjest, jakjest_hi, 'r', linewidth=1.5, label='Prosta dużo')
ax3.plot(x_jakjest, jakjest_md, 'g', linewidth=1.5, label='Prosta dużo')
ax3.plot(x_jakjest, jakjest_lo, 'b', linewidth=1.5, label='Prosta mało')
ax3.set_title('life standard')
ax3.legend()

# Turn off top/right axes
for ax in (ax0, ax1, ax2, ax3):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()

# We need the activation of our fuzzy membership functions at these values.
# The exact values  do not exist on our universes...
# This is what fuzz.interp_membership exists for!

a = pd.to_numeric(czasWolny.loc[0, "wartosc"])
b = pd.to_numeric(kosztyAktywn.loc[3, "wartosc"])
c = pd.to_numeric(poziomAktywn.loc[4, "wartosc"])
czasWolny_level_lo = fuzz.interp_membership(x_czasWolny, czasWolny_lo, a)
czasWolny_level_md = fuzz.interp_membership(x_czasWolny, czasWolny_md, a)
czasWolny_level_hi = fuzz.interp_membership(x_czasWolny, czasWolny_hi, a)

kosztAktywn_level_lo = fuzz.interp_membership(x_kosztAktywn, kosztAktywn_lo, b)
kosztAktywn_level_md = fuzz.interp_membership(x_kosztAktywn, kosztAktywn_md, b)
kosztAktywn_level_hi = fuzz.interp_membership(x_kosztAktywn, kosztAktywn_hi, b)

poziomAktywn_level_lo = fuzz.interp_membership(x_poziomAktywn, poziomAktywn_lo, c)
poziomAktywn_level_md = fuzz.interp_membership(x_poziomAktywn, poziomAktywn_md, c)
poziomAktywn_level_hi = fuzz.interp_membership(x_poziomAktywn, poziomAktywn_hi, c)

# Rule 1 Cost is low and a high amount of free time or high activity month
active_rule1 = kosztAktywn_level_lo * np.fmax(czasWolny_level_hi, poziomAktywn_level_hi)

# Now we apply this by clipping the top off the corresponding output
# membership function with `np.fmin`
jakjest_activation_hi = np.fmin(active_rule1, jakjest_hi)  # removed entirely to 0
lif0 = np.zeros_like(x_jakjest)

# Rule2 is Negativity of Rule 1
active_rule2 = kosztAktywn_hi * np.fmax(czasWolny_lo, poziomAktywn_lo)
jakjest_activation_lo = np.fmin(active_rule2, jakjest_lo)

# Rest of the rules need to be defined, otherwise we will get errors.

# Rule for catching values from medium range
active_rule3 = kosztAktywn_md * np.fmax(czasWolny_md, poziomAktywn_md)
jakjest_activation_md = np.fmin(active_rule2, jakjest_md)

# Rules for catching  extreme values ([low,low,low],[high,high,high])
active_rule4 = kosztAktywn_lo * czasWolny_lo * poziomAktywn_lo
jakjest_activation_of = np.fmin(active_rule4, jakjest_lo)

active_rule5 = kosztAktywn_hi * czasWolny_hi * poziomAktywn_hi  # If everything is expensive and we have lots of free time, usually it means we don't have too much money :)
jakjest_activation_of1 = np.fmin(active_rule5, jakjest_md)

# Visualize this
fig, ax0 = plt.subplots(figsize=(8, 3))
ax0.fill_between(x_jakjest, lif0, jakjest_activation_hi, facecolor='r', alpha=0.7)
ax0.plot(x_jakjest, jakjest_hi, 'g', linewidth=0.5, linestyle='--', )
ax0.set_title('Output membership activity')
ax0.fill_between(x_jakjest, lif0, jakjest_activation_lo, facecolor='b', alpha=0.7)
ax0.plot(x_jakjest, jakjest_lo, 'b', linewidth=0.5, linestyle='--')
ax0.fill_between(x_jakjest, lif0, jakjest_activation_md, facecolor='g', alpha=0.7)
ax0.plot(x_jakjest, jakjest_md, 'b', linewidth=0.5, linestyle='--')

ax0.fill_between(x_jakjest, lif0, jakjest_activation_of, facecolor='y', alpha=0.7)
ax0.plot(x_jakjest, jakjest_lo, 'b', linewidth=0.5, linestyle='--')
ax0.fill_between(x_jakjest, lif0, jakjest_activation_of1, facecolor='y', alpha=0.7)
ax0.plot(x_jakjest, jakjest_lo, 'b', linewidth=0.5, linestyle='--')
# Turn off top/right axes
for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
print(jakjest_activation_hi)

# Aggregate all three output membership functions together
aggregated = np.fmax(jakjest_activation_hi, jakjest_activation_lo, jakjest_activation_md)

# Calculate defuzzified result
jakjest = fuzz.defuzz(x_jakjest, aggregated, 'mom')
jakjest_activation = fuzz.interp_membership(x_jakjest, aggregated, jakjest)  # for plot

# Visualize this
fig, ax0 = plt.subplots(figsize=(8, 3))

ax0.plot(x_jakjest, jakjest_lo, 'b', linewidth=0.5, linestyle='--', )
ax0.plot(x_jakjest, jakjest_md, 'g', linewidth=0.5, linestyle='--')
ax0.plot(x_jakjest, jakjest_hi, 'r', linewidth=0.5, linestyle='--')
ax0.fill_between(x_jakjest, lif0, aggregated, facecolor='Orange', alpha=0.7)
ax0.plot([jakjest, jakjest], [0, jakjest_activation], 'k', linewidth=1.5, alpha=0.9)
ax0.set_title('Aggregated membership and result (line)')

# Turn off top/right axes
for ax in (ax0,):
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.get_xaxis().tick_bottom()
    ax.get_yaxis().tick_left()

plt.tight_layout()
print(jakjest)

i, j = kosztyAktywn.shape  # poziomy
i2, j2 = poziomAktywn.shape  # msc
i3, j3 = czasWolny.shape  # dni

for row in range(i):
    for row2 in range(i2):
        for row3 in range(i3):
            b = pd.to_numeric(poziomAktywn.at[row2, "wartosc"])
            a = pd.to_numeric(kosztyAktywn.loc[row, "wartosc"])
            c = pd.to_numeric(czasWolny.at[row3, "wartosc"])
            czasWolny_level_lo = fuzz.interp_membership(x_czasWolny, czasWolny_lo, c)
            czasWolny_level_md = fuzz.interp_membership(x_czasWolny, czasWolny_md, c)
            czasWolny_level_hi = fuzz.interp_membership(x_czasWolny, czasWolny_hi, c)

            kosztAktywn_level_lo = fuzz.interp_membership(x_kosztAktywn, kosztAktywn_lo, a)
            kosztAktywn_level_md = fuzz.interp_membership(x_kosztAktywn, kosztAktywn_md, a)
            kosztAktywn_level_hi = fuzz.interp_membership(x_kosztAktywn, kosztAktywn_hi, a)

            poziomAktywn_level_lo = fuzz.interp_membership(x_poziomAktywn, poziomAktywn_lo, b)
            poziomAktywn_level_md = fuzz.interp_membership(x_poziomAktywn, poziomAktywn_md, b)
            poziomAktywn_level_hi = fuzz.interp_membership(x_poziomAktywn, poziomAktywn_hi, b)

            # Rule 1 Cost is low and a high amount of free time or high activity month
            active_rule1 = kosztAktywn_level_lo * np.fmax(czasWolny_level_hi, poziomAktywn_level_hi)

            # Now we apply this by clipping the top off the corresponding output
            # membership function with `np.fmin`
            jakjest_activation_hi = np.fmin(active_rule1, jakjest_hi)  # removed entirely to 0
            lif0 = np.zeros_like(x_jakjest)

            # Rule2 is Negativity of Rule 1
            active_rule2 = kosztAktywn_hi * np.fmax(czasWolny_lo, poziomAktywn_lo)
            jakjest_activation_lo = np.fmin(active_rule2, jakjest_lo)

            # Rules for catching  extreme values ([low,low,low],[high,high,high])
            active_rule3 = kosztAktywn_md * np.fmax(czasWolny_md, poziomAktywn_md)
            jakjest_activation_md = np.fmin(active_rule2, jakjest_md)

            # Zasady do wyłapywania się wartości skrajnych ([low,low,low],[high,high,high])
            active_rule4 = kosztAktywn_lo * czasWolny_lo * poziomAktywn_lo
            jakjest_activation_of = np.fmin(active_rule4, jakjest_lo)

            active_rule5 = kosztAktywn_hi * czasWolny_hi * poziomAktywn_hi  # If everything is expensive and we have lots of free time, usually it means we don't have too much money :)
            jakjest_activation_of1 = np.fmin(active_rule5, jakjest_lo)

            # Aggregate all three output membership functions together
            aggregated = np.fmax(jakjest_activation_hi, jakjest_activation_lo,
                                 jakjest_activation_md)  # Małe oszustwo, powinna być kolejna funkcja nie 0

            # Calculate defuzzified result
            jakjest = fuzz.defuzz(x_jakjest, aggregated, 'mom')

            if row3 == 0 and row2 == 0 and row == 0:
                wynik = np.array([[kosztyAktywn.at[row, "aktywnosc"], poziomAktywn.at[row2, "miesiac"],
                                   czasWolny.at[row3, "dzien"], jakjest]])
            else:
                wynik = np.append(wynik, [
                    [kosztyAktywn.at[row, "aktywnosc"], poziomAktywn.at[row2, "miesiac"], czasWolny.at[row3, "dzien"],
                     jakjest]]).reshape((len(wynik) + 1), 4)

wynikDF = pd.DataFrame(wynik, columns=["aktywnosc", "miesiac", "dzien", "wynik"])
wynikDF = wynikDF.sort_values(by=["wynik"], ascending=False)
print(wynikDF)
