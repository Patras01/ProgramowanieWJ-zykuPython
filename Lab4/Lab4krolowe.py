# Lab4
class Board:
    def __init__(self, n=8):
        self.n = n
        self.queens = []

    def place(self, row, col):
        self.queens.append((row, col))

    def remove(self, row, col):
        self.queens.remove((row, col))

    def is_safe(self, row, col):
        for r, c in self.queens:
            if r == row or c == col or abs(r - row) == abs(c - col):
                return False
        return True

    def solve(self, col=0):
        if col == self.n:
            return 1

        count = 0
        for row in range(self.n):
            if self.is_safe(row, col):
                self.place(row, col)
                count += self.solve(col + 1)
                self.remove(row, col)
        return count

    def __len__(self):
        return len(self.queens)

    def __iter__(self):
        yield from self.queens

    def __contains__(self, pos):
        return pos in self.queens

    def __str__(self):
        res = ""
        for r in range(self.n):
            row_str = ""
            for c in range(self.n):
                row_str += " Q " if (r, c) in self.queens else " . "
            res += row_str + "\n"
        return res


def solve(n=8):
    return Board(n).solve()


if __name__ == "__main__":
    print(f"solve(1) -> {solve(1)} rozwiązanie")
    print(f"solve(4) -> {solve(4)} rozwiązania")
    print(f"solve(8) -> {solve(8)} rozwiązań")