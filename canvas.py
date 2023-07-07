class Canvas:
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height
        self.matrix = [[' ' for _ in range(width)] for _ in range(height)]

    def add_line(self, x1: int, y1: int, x2: int, y2: int) -> None:
        if y1 == y2:
            for i in range(x1, x2 + 1):
                self.matrix[y1 - 1][i - 1] = 'x'
        elif x1 == x2:
            for i in range(y1, y2 + 1):
                self.matrix[i - 1][x1 - 1] = 'x'

    def add_rectangle(self, x1: int, y1: int, x2: int, y2: int) -> None:
        self.add_line(x1, y1, x2, y1)
        self.add_line(x1, y2, x2, y2)
        self.add_line(x1, y1, x1, y2)
        self.add_line(x2, y1, x2, y2)

    def bucket_fill(self, x: int, y: int, c: str):
        if self.matrix[y - 1][x - 1] == ' ':
            self._bucket_fill(x - 1, y - 1, c)

    def _bucket_fill(self, x: int, y: int, c: str):
        if 0 <= x < self.width and 0 <= y < self.height and self.matrix[y][x] == ' ':
            self.matrix[y][x] = c
            self._bucket_fill(x + 1, y, c)
            self._bucket_fill(x - 1, y, c)
            self._bucket_fill(x, y + 1, c)
            self._bucket_fill(x, y - 1, c)

    def __str__(self) -> str:
        canvas = '\n'.join([''.join(row) for row in self.matrix])
        canvas = '-' * (self.width + 2) + '\n|' + canvas.replace('\n', '|\n|') + '|\n' + '-' * (self.width + 2)
        return canvas
