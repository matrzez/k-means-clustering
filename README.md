# Projekt: Algorytm K-Średnich

## 📌 Opis projektu
Projekt dotyczy implementacji oraz analizy algorytmu k-średnich, który jest popularnym algorytmem wykorzystywanym do rozwiązywania problemów klasteryzacji w zbiorach danych. Celem projektu jest przeprowadzenie procesu klasteryzacji na losowo wygenerowanych punktach w przestrzeni 2D, a następnie wizualizacja wyników z wyświetleniem klas i centroidów. W ramach projektu, użytkownik ma możliwość wyboru metody generowania punktów (losowe lub ręczne) oraz dostosowania liczby punktów i klastrów. Projekt wykorzystuje również narzędzia do wizualizacji wyników, takie jak biblioteka `matplotlib`.

Algorytm k-średnich (KMeans) dzieli zbiór danych na określoną liczbę klastrów, minimalizując sumę odległości między punktami a centroidami (środkami) tych klastrów. Jest to jeden z najczęściej używanych algorytmów w analizie danych i uczeniu maszynowym.

## 📊 Technologie
- **Python** – do implementacji algorytmu i analizy wyników.

## 📁 Pliki w repozytorium
- **Algorytm_k_srednich.py** – plik zawierający implementację algorytmu KMeans oraz kod umożliwiający generowanie punktów, klasteryzację i wizualizację wyników.

## Opis działania

1. **Generowanie punktów** – Użytkownik ma możliwość wyboru trybu generowania punktów:
   - **l** – losowo wygenerowane punkty w przedziale [1, 100].
   - **r** – ręczne wprowadzanie współrzędnych punktów.
  
2. **Klasteryzacja** – Po wygenerowaniu punktów, algorytm KMeans jest wykorzystywany do podzielenia punktów na zadaną liczbę klastrów. Użytkownik wprowadza liczbę punktów oraz liczbę klastrów.

3. **Analiza wyników** – Po zakończeniu klasteryzacji:
   - Wypisywane są współrzędne centroidów klastrów.
   - Czas wykonania algorytmu jest mierzony i prezentowany użytkownikowi.
  
4. **Wizualizacja** – Skrypt generuje wykres, na którym punkty są przedstawione w różnych kolorach odpowiadających przypisanym klastrom. Centroidy klastrów są wyświetlane jako czarne krzyżyki.

## 👨‍💻 Autorzy
- **Mateusz Rzeźnikiewicz** oraz **Patryk Ryba**  
**Politechnika Rzeszowska, 2023**  

