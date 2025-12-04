class Arithmetic:
    def add(self, first: int, second: int) -> int:
        return first + second

    def add_float(self, first: float, second: float) -> float:
        return first + second

    def divide(self, first: int, second: int) -> float | None:
        if second == 0:
            print("Går inte att dela med 0!")
            return None

        return first / second
