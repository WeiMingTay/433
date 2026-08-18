Als Fachinformatiker für Systemintegration

möchte ich die Stabilität einer Netzwerkverbindung bewerten, indem ich nicht nur die durchschnittliche Latenz, sondern auch deren Schwankung (Jitter) messe und quantifiziere.

# Celebration Criteria (Lernziele) 

- Wir können die Spannweite eines Datensatzes berechnen.
- Wir können die Varianz berechnen.
- Wir können die Standardabweichung berechnen und interpretieren.
- Wir verstehen die Standardabweichung als Maß für die Konsistenz oder Zuverlässigkeit eines Systems.

# Wissens-Briefing 

Streuungsmaße beschreiben, wie stark die Datenwerte um ein Lagemaß (meist den Mittelwert) verteilt sind. Sie sind ein Maß für die Konsistenz oder Zuverlässigkeit eines Prozesses.

- **Spannweite:** Die Differenz zwischen dem größten (Maximum) und dem kleinsten Wert (Minimum) in einem Datensatz. Sie ist einfach zu berechnen, aber sehr anfällig für Ausreißer.  
- **Varianz ():** Die durchschnittliche quadratische Abweichung der einzelnen Datenwerte vom arithmetischen Mittel. Eine große Varianz bedeutet eine starke Streuung. Formel für eine Stichprobe:  $s^2=\\frac{1}{n−1}\\displaystyle\\sum_{​i=1}^n​(x_i​−\\overline{x})^2$
- **Standardabweichung ():** Die Quadratwurzel aus der Varianz. Sie hat dieselbe Einheit wie die ursprünglichen Daten und ist daher leichter zu interpretieren. Eine geringe Standardabweichung bei der Netzwerklatenz bedeutet eine stabile, "glatte" Verbindung, während eine hohe Standardabweichung auf eine unzuverlässige, "ruckelnde" Verbindung hindeutet, selbst wenn der Mittelwert identisch ist.

 

# Aufgaben 

1. Berechnet die Spannweite, Varianz und Standardabweichung für den Datensatz: 10, 12, 15, 11, 13.
2. Zwei Programmierer schreiben Code. Die Anzahl der pro Tag geschriebenen Codezeilen über 5 Tage wird erfasst:
  - Programmierer A: 100, 150, 120, 400, 80
  - Programmierer B: 150, 160, 155, 145, 165 Berechnet für beide den Mittelwert und die Standardabweichung. Wer arbeitet produktiver? Wer arbeitet konsistenter?
3. **Lego-Aufgabe:** Lasst eurer Lego-Auto 5-mal eine definierte Strecke fahren und stoppt die Zeit. Berechnet den Mittelwert und die Standardabweichung der Fahrzeiten. Was sagt die Standardabweichung über das Anschieben mit der Hand aus?
4. **Tool-Aufgabe:** Gebt die Daten aus der Abschlussaufgabe von Epic M4.3 in eine Tabellenkalkulation (Excel, LibreOffice Calc) ein und berechnet die Kennzahlen mit den eingebauten Funktionen `MITTELWERT()`, `MEDIAN()`, `VAR.S()` und `STABW.S()`.

# Referenzen & Vertiefung 

- **Primärquelle:** Kersken, S. (2025). _IT-Handbuch für Fachinformatiker_ (12. Aufl.). Rheinwerk Computing. (Kapitel 2.4.2, S. 106-108)
- **Sekundärquellen:**
  - YouTube:()
  - Novustat: [Anleitung für statistische Kennzahlen](https://novustat.com/statistik-blog/statistik-fuer-dummies-statistik-auswertung-mit-spss.html)