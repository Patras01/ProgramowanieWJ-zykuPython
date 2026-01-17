class Board:
    def __init__(self, n=8):
        self.n = n
        self.queens = []

    def place(self, row, col):
        """Dodaje królową na podaną pozycję."""
        self.queens.append((row, col))

    def remove(self, row, col):
        """Usuwa królową z podanej pozycji (backtracking)."""
        self.queens.remove((row, col))

    def is_safe(self, row, col):
        """Sprawdza, czy żadna inna królowa nie atakuje pola (row, col)."""
        # Sprawdzanie wiersza, kolumny i przekątnych
        for r, c in self.queens:
            if r == row or c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def solve(self, col=0):
        """Rekurencyjnie szuka rozwiązań, ustawiając królowe kolumna po kolumnie."""
        # Jeśli ustawiono n królowych — mamy rozwiązanie
        if col == self.n:
            return 1

        count = 0
        # Rekurencyjnie próbujemy ustawiać królowe rząd po rzędzie
        for row in range(self.n):
            if self.is_safe(row, col):
                self.place(row, col)
                count += self.solve(col + 1)  # Przejdź do następnej kolumny
                self.remove(row, col)  # Powrót (odrzucamy ruch)
        return count

    # Metody magiczne wymagane w zadaniu
    def __len__(self):
        return len(self.queens)

    def __iter__(self):
        yield from self.queens

    def __contains__(self, pos):
        return pos in self.queens

    def __str__(self):
        """Wizualizacja szachownicy w tekście."""
        res = ""
        for r in range(self.n):
            row_str = ""
            for c in range(self.n):
                row_str += " Q " if (r, c) in self.queens else " . "
            res += row_str + "\n"
        return res


# Funkcja startowa zgodna z API zadania
def solve(n=8):
    return Board(n).solve()


# --- TESTOWANIE WYNIKÓW ---
if __name__ == "__main__":
    print(f"solve(1) -> {solve(1)} rozwiązanie")
    print(f"solve(4) -> {solve(4)} rozwiązania")
    print(f"solve(8) -> {solve(8)} rozwiązań")