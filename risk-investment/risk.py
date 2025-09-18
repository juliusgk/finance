
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# Analyst-Ratings Daten für Alphabet (GOOGL) basierend auf aktuellen Quellen
analyst_data = {
    'Quelle': ['MarketBeat', 'StockAnalysis', 'Benzinga', 'Zacks', 'TipRanks_Avg', 'TradingView'],
    'Price_Target': [224.51, 226.85, 225.62, 218.75, 225.00, 236.15],
    'Anzahl_Analysten': [40, 40, 35, 48, 45, 42],
    'Rating': ['Buy', 'Buy', 'Buy', 'Buy', 'Buy', 'Buy'],
    'Min_Target': [186, 186, 186, 184, 186, 190],
    'Max_Target': [300, 300, 300, 240, 250, 300]
}

# Zusätzliche Marktdaten
current_price = 249.52  # Aktueller Kurs (Sept 2025)
beta = 0.99  # Beta-Wert
risk_free_rate = 0.045  # 10-Jahr Treasury (ca. 4.5%)
market_return = 0.10  # Erwartete Marktrendite (10%)

df = pd.DataFrame(analyst_data)

print("=== ALPHABET (GOOGL) INVESTMENT ANALYSE = ==\n")
print("Aktueller Kurs:", f"${current_price:.2f}")
print("Beta:", beta)
print()

# 1. STANDARDABWEICHUNG DER ANALYST-RATINGS
print("1. STANDARDABWEICHUNG DER ANALYST PRICE TARGETS")
print("=" * 50)

price_targets = df['Price_Target'].values
mean_target = np.mean(price_targets)
std_dev = np.std(price_targets, ddof=1)  # Sample standard deviation
cv = std_dev / mean_target  # Coefficient of Variation

print(f"Durchschnittliches Price Target: ${mean_target:.2f}")
print(f"Standardabweichung: ${std_dev:.2f}")
print(f"Variationskoeffizient: {cv:.3f} ({cv*100:.1f}%)")
print(f"Min Price Target: ${df['Min_Target'].min()}")
print(f"Max Price Target: ${df['Max_Target'].max()}")
print()

# 2. EXPECTED RETURN (WEIGHTED AVERAGE)
print("2. EXPECTED RETURN (GEWICHTETER DURCHSCHNITT)")
print("=" * 50)

# Gewichtung nach Anzahl der Analysten
weights = df['Anzahl_Analysten'] / df['Anzahl_Analysten'].sum()
weighted_avg_target = np.sum(df['Price_Target'] * weights)
expected_return = (weighted_avg_target - current_price) / current_price

print("Gewichtung nach Anzahl Analysten:")
for i, row in df.iterrows():
    print(f"  {row['Quelle']}: {weights[i]:.3f} ({weights[i]*100:.1f}%) - {row['Anzahl_Analysten']} Analysten")

print(f"\nGewichtetes durchschnittliches Price Target: ${weighted_avg_target:.2f}")
print(f"Erwartete Rendite: {expected_return:.3f} ({expected_return*100:.1f}%)")
print()

# 3. RISIKO-ÜBERSICHT MIT BETA
print("3. RISIKO-ANALYSE INKLUSIVE BETA")
print("=" * 50)

# CAPM Expected Return
capm_return = risk_free_rate + beta * (market_return - risk_free_rate)
excess_return = expected_return - capm_return

print(f"Risikofreier Zinssatz: {risk_free_rate*100:.1f}%")
print(f"Erwartete Marktrendite: {market_return*100:.1f}%")
print(f"Alphabet Beta: {beta}")
print(f"CAPM erwartete Rendite: {capm_return*100:.1f}%")
print(f"Analyst erwartete Rendite: {expected_return*100:.1f}%")
print(f"Alpha (Excess Return): {excess_return*100:.1f}%")
print()

# Risiko-Kategorisierung
print("RISIKO-BEWERTUNG:")
print("-" * 20)

if beta < 0.8:
    beta_risk = "NIEDRIG (Defensiv)"
elif beta <= 1.2:
    beta_risk = "MITTEL (Marktkonform)"
else:
    beta_risk = "HOCH (Aggressiv)"

if cv < 0.1:
    analyst_consensus = "STARK (Niedrige Streuung)"
elif cv <= 0.15:
    analyst_consensus = "MODERAT (Mittlere Streuung)"
else:
    analyst_consensus = "SCHWACH (Hohe Streuung)"

print(f"Beta-Risiko: {beta_risk}")
print(f"Analisten-Konsens: {analyst_consensus}")
print(f"Prognose-Unsicherheit: {std_dev:.2f} USD Standardabweichung")
print()

# 4. PORTFOLIO-IMPACT SIMULATION
print("4. PORTFOLIO-IMPACT SIMULATION")
print("=" * 50)

portfolio_weights = [0.05, 0.10, 0.15, 0.20, 0.25]
market_scenarios = [-0.20, -0.10, 0.00, 0.10, 0.20]

print("Portfolio-Gewichtung vs. Markt-Szenarien:")
print("Gewicht\\Markt", end="")
for scenario in market_scenarios:
    print(f"\t{scenario*100:+.0f}%", end="")
print()

for weight in portfolio_weights:
    print(f"{weight*100:.0f}%\t", end="")
    for market_change in market_scenarios:
        alphabet_change = beta * market_change + (expected_return - capm_return)
        portfolio_impact = weight * alphabet_change
        print(f"\t{portfolio_impact*100:+.1f}%", end="")
    print()

print()

# 5. MONTE CARLO SIMULATION
print("5. MONTE CARLO SIMULATION (1000 SZENARIEN)")
print("=" * 50)

np.random.seed(42)
n_simulations = 1000

# Simulation der zukünftigen Kurse basierend auf Analyst-Targets und Volatilität
simulated_targets = np.random.normal(weighted_avg_target, std_dev, n_simulations)
simulated_returns = (simulated_targets - current_price) / current_price

# Statistiken
mc_mean_return = np.mean(simulated_returns)
mc_std_return = np.std(simulated_returns)
var_95 = np.percentile(simulated_returns, 5)  # Value at Risk (95% Konfidenz)
var_99 = np.percentile(simulated_returns, 1)   # Value at Risk (99% Konfidenz)

print(f"Monte Carlo Durchschnittsrendite: {mc_mean_return*100:.1f}%")
print(f"Monte Carlo Volatilität: {mc_std_return*100:.1f}%")
print(f"Value at Risk (95%): {var_95*100:.1f}%")
print(f"Value at Risk (99%): {var_99*100:.1f}%")
print(f"Wahrscheinlichkeit positiver Rendite: {(simulated_returns > 0).mean()*100:.1f}%")
print()

# 6. INVESTMENT-EMPFEHLUNG
print("6. INVESTMENT-EMPFEHLUNG")
print("=" * 50)

score = 0
reasons = []

# Scoring basierend auf verschiedenen Faktoren
if expected_return > 0.05:
    score += 2
    reasons.append("+ Positive erwartete Rendite über 5%")
elif expected_return > 0:
    score += 1
    reasons.append("+ Positive erwartete Rendite")
else:
    reasons.append("- Negative erwartete Rendite")

if beta < 1.2:
    score += 1
    reasons.append("+ Moderates Beta-Risiko")
else:
    reasons.append("- Hohes Beta-Risiko")

if cv < 0.12:
    score += 1
    reasons.append("+ Guter Analysten-Konsens")
else:
    reasons.append("- Schwacher Analysten-Konsens")

if excess_return > 0.02:
    score += 2
    reasons.append("+ Signifikantes Alpha über CAPM")
elif excess_return > 0:
    score += 1
    reasons.append("+ Positives Alpha")
else:
    reasons.append("- Negatives Alpha")

# Empfehlung basierend auf Score
if score >= 5:
    recommendation = "STARKER KAUF"
elif score >= 3:
    recommendation = "KAUF"
elif score >= 1:
    recommendation = "HALTEN"
else:
    recommendation = "VERKAUF/VERMEIDEN"

print(f"Investment Score: {score}/6")
print(f"Empfehlung: {recommendation}")
print("\nBegründung:")
for reason in reasons:
    print(reason)

print("\n" + "="*60)
print("ZUSAMMENFASSUNG")
print("="*60)
print(f"• Aktueller Kurs: ${current_price}")
print(f"• Analyst-Ziel (gewichtet): ${weighted_avg_target:.2f}")
print(f"• Erwartete Rendite: {expected_return*100:.1f}%")
print(f"• Beta-Risiko: {beta} ({beta_risk})")
print(f"• Volatilität der Prognosen: {std_dev:.2f} USD")
print(f"• Value at Risk (95%): {var_95*100:.1f}%")
print(f"• Empfehlung: {recommendation}")
