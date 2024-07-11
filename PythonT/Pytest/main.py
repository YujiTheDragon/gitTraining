def addition(x, y):
    return x + y


def sub(x, y):
    return x - y


class TestClass:
    x = y = 0

    def test_sub(self):
        self.x = 5
        self.y = 4
        assert sub(self.x, self.y) == 1

    def test_addition(self):
        self.x = 5
        self.y = 2
        assert addition(self.x, self.y) == 7


def main():
    pass


if __name__ == "__main__":
    main()
