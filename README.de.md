
# Analyse der Mietpreise in Berlin

Dieses Projekt führt eine **explorative Datenanalyse (EDA)** zu Mietpreisen in verschiedenen Berliner Bezirken durch.  
Es wurde mit **Python** erstellt und verwendet Bibliotheken wie `pandas`, `matplotlib` und `seaborn` für Datenanalyse und Visualisierung.

## 📂 Projektstruktur

python_project_4/
├── env/ # virtuelle Umgebung
├── data/
│ └── berlin_rent.csv # Datensatz mit simulierten Mietdaten
├── images/ # generierte Diagramme
│ ├── distribution_prices.png
│ ├── average_price.png
│ └── relationship_sqm_price.png
├── berlin_rent_analysis.py # Hauptanalyse-Skript
├── README.md # Englische Version
└── README.de.md # Deutsche Version

## ⚙️ Verwendete Technologien
- Python 3.13
- pandas
- matplotlib
- seaborn

## 📊 Durchgeführte Analysen
1. Erste Datenexploration (`head`, `info`, `describe`)
2. Berechnung des durchschnittlichen Mietpreises pro Bezirk
3. Visualisierungen:
   - Verteilung der Mietpreise
   - Durchschnittlicher Mietpreis pro Bezirk (Balkendiagramm)
   - Zusammenhang zwischen Wohnungsgröße (m²) und Mietpreis (Scatterplot)

## 📸 Beispielergebnisse

### Verteilung der Mietpreise
![Verteilung der Mietpreise](./images/distribution_prices.png)

### Durchschnittlicher Mietpreis pro Bezirk
![Durchschnittlicher Mietpreis pro Bezirk](./images/average_price.png)

### Zusammenhang zwischen m² und Mietpreis
![Zusammenhang m² vs Mietpreis](./images/relationship_sqm_price.png)

## 🚀 Projekt ausführen

1. Repository klonen
2. Virtuelle Umgebung erstellen:
   ```bash
   python3 -m venv env
   source env/bin/activate
Abhängigkeiten installieren:
pip install pandas matplotlib seaborn
Skript starten:
python3 berlin_rent_analysis.py
🙋 Autorin
Projekt entwickelt von Paula Espinoza 
Dieses Projekt ist Teil meines Portfolios für Werkstudentenpositionen