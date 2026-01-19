wzrost = input("Podaj swój wzrost w cm: ")
masa = input("Podaj swoja mase w kg: ")
wzrost = float(wzrost)
masa = float(masa)
bmi = masa/pow((wzrost/100),2)
print(f"Twoje bmi wynosi {bmi:.2f}")
if bmi < 16.0:
    print("Wygłodzenie")
elif bmi < 16.9:
    print("Wychudzenie")
elif bmi < 18.5:
    print("Wiedowaga")
elif bmi < 24.9:
    print("Waga prawidłowa")
elif bmi < 29.9:
    print("Wadwaga")
elif bmi < 34.9:
    print("Otylość pierwszego stopnia")
elif bmi < 39.9:
    print("Otylość drugiego stopnia")
elif bmi > 40:
    print("Otylość trzeciego stopnia")