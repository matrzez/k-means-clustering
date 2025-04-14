import random
import time
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# Funkcja do generowania losowych, unikalnych punktów
def generator_punktow(ilosc_pkt):
    punkty = set()
    while len(punkty) < ilosc_pkt:
        punkt = (random.uniform(1, 100), random.uniform(1, 100))
        punkty.add(punkt)
    return list(punkty)

# Zabezpieczamy nasz kod przed wprowadzeniem błędnych danych, które mogłyby skutkować niepoprawnym działaniem kodu
while True:
    try:
        # Wybór trybu generowania punktów
        wybor = input("Wybierz tryb generowania punktów ('l' - losowe, 'r' - ręczne): ")
        if wybor != 'l' and wybor != 'r':
            raise ValueError("Nieprawidłowy wybór trybu!")

        # Wczytanie liczby punktów i liczby klastrów od użytkownika, obydwie wartości są typu integer
        ilosc_pkt = int(input("Podaj ilość punktów: "))
        if ilosc_pkt <= 0:
            raise ValueError("Liczba punktów musi być dodatnia!")

        ilosc_klas = int(input("Podaj ilość klas: "))
        if (ilosc_klas >= ilosc_pkt) or (ilosc_klas <= 0):
            raise ValueError("Liczba klastrów musi być dodania oraz mniejsza niż liczba punktów!")

        break
    except ValueError as e:
        print(e)
        print("Wprowadź poprawne dane.\n")

# Generowanie punktów na podstawie wybranego trybu
if wybor == 'l':
    punkty = generator_punktow(ilosc_pkt)
elif wybor == 'r':
    punkty = []
    for i in range(ilosc_pkt):
        while True:
            try:
                x = int(input("Podaj współrzędną x: "))
                y = int(input("Podaj współrzędną y: "))
                punkty.append([x, y])
                break
            except ValueError:
                print("Wprowadź poprawne dane dla współrzędnych x i y.\n")

print("Wylosowane punkty:")
for punkt in punkty:
    print(punkt)

# Utworzenie obiektu klasy KMeans i dopasowanie do punktów
start_time = time.time()
kmeans = KMeans(n_clusters=ilosc_klas, n_init = 10)
kmeans.fit(punkty)
centroidy = kmeans.cluster_centers_
przypisane_klasy = kmeans.predict(punkty)
end_time = time.time()

# Wypisujemy pozyskane współrzędne centroidów
print("\nWspółrzędne centroidów:")
for centroid in centroidy:
    print(centroid)

# Wyświetlanie czasu działania algorytmu
czas_wykonania = end_time - start_time
print(f"\nCzas wykonania algorytmu klasteryzacji: {czas_wykonania} sekund")

# Wizualizacja

# Lista kolorów dla klastrów, w wypadku podania przez użytkownika większej ilości klas niż 8, konieczne będzie dodanie dodatkowych kolorów
colors = ['red', 'blue', 'green', 'orange', 'purple', 'brown', 'pink', 'gray']

# Wyświetlanie punktów na wykresie, z odpowiednimi kolorami dla klastrów
for i, punkt in enumerate(punkty):
    klasa = przypisane_klasy[i]
    plt.scatter(punkt[0], punkt[1], color=colors[klasa])

# Wyświetlanie centroidów na wykresie
for i, centroid in enumerate(centroidy):
    plt.scatter(centroid[0], centroid[1], color='black', marker='x', s=100)
    plt.annotate(f'Centroid {i+1}', (centroid[0]+1, centroid[1]-1))  

# Konfiguracja tytułu i osi
plt.title('Klasteryzacja wylosowanych punktów za pomocą metody k-średnich')
plt.xlabel('Wymiar X')
plt.ylabel('Wymiar Y')

# Wyświetlanie wykresu
plt.show()