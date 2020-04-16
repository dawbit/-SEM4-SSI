import random
import math
import numpy as np

class Dane:
    def __init__(self):
            self.item_list = []

    def pobierz(self, filename):
        with open(filename, "r") as f:
            items = f.read().splitlines()
        for x in range(0, len(items)):
            items[x] = [float(i) for i in items[x].split(";")]

        for x in range(0, len(items)):
            self.item_list = self.item_list + items[x]

    def tasuj(self):
        random.shuffle(self.item_list)


    def norm(self):
        print("1. Min-max\n2. Mean\n3. Standaryzacja")
        try:
            arg = float(input('Wybór: '))
        except ValueError:
            print("To nie jest liczba")

        if arg == 1:
            try:
                range_min = int(input('Min: '))
                range_max = int(input('Max: '))
                normalized = self.item_list.copy()

                for x in range(0, len(normalized)):
                    normalized[x] = float(((normalized[x] - min(normalized)) / (max(normalized) - min(normalized))) * (range_max - range_min) + range_min)

                print(normalized)
            except ValueError:
                print("Błąd")
        elif arg == 2:
            try:
                normalized = self.item_list.copy()
                average = sum(normalized) / len(normalized)
                for x in range(0, len(normalized)):
                    normalized[x] = float((normalized[x] - average) / (max(normalized) - min(normalized)))

                print(normalized)
            except ValueError:
                print("Błąd")
        elif arg == 3:
            try:
                normalized = self.item_list.copy()
                average = sum(normalized) / len(normalized)
                deviation = 0
                for x in range(0, len(normalized)):
                    deviation += pow(normalized[x] - average, 2)

                deviation = math.sqrt(deviation / len(normalized))

                for x in range(0, len(normalized)):
                    normalized[x] = float((normalized[x] - average) / (deviation))

                print(normalized)
            except ValueError:
                print("Błąd")
        else:
            print("Zły argument")

obiekt = Dane()
obiekt.pobierz("dane.txt")

print(obiekt.item_list)

obiekt.norm()