import statistics

# Zwei Programmierer schreiben Code. Die Anzahl der pro Tag geschriebenen Codezeilen über 5 Tage wird erfasst:
# Programmierer A: 100, 150, 120, 400, 80
# Programmierer B: 150, 160, 155, 145, 165 
# Berechnet für beide den Mittelwert und die Standardabweichung. Wer arbeitet produktiver? Wer arbeitet konsistenter?

coder_A = [100, 150, 120, 400, 80]
coder_B = [150, 160, 155, 145, 165]

# Mittelwert berechnen

def mittelwert_berechnen(list):
    return sum(list) / len(list)
       
mittel_A= mittelwert_berechnen(coder_A)
mittel_B = mittelwert_berechnen(coder_B)
differenz = mittel_A - mittel_B

print(f"Programmierer A: {mittel_A} Codezeilen")
print(f"Programmierer B: {mittel_B} Codezeilen")
    
if differenz < 0:
    differenz *= -1
    
print(f"Differenz: {differenz} Codezeilen")

# Standardabweichung

def std_abw(list):
    return statistics.stdev(list)

print(f"Standardabweichung Coder A: {std_abw(coder_A):.2f}")
print(f"Standardabweichung Coder B: {std_abw(coder_B):.2f}")