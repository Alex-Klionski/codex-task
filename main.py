from canvas import Canvas
from utils import read_file, validate_parameters
from typing import List


class CanvasCommandProcessor:
    def __init__(self):
        self.canvas = None
        self.commands_mapper = {
            'C': self.create_canvas,
            'L': self.add_line,
            'R': self.add_rectangle,
            'B': self.bucket_fill
        }

    def process_commands(self, commands: List[str]) -> None:
        with open('output_new.txt', 'w') as file:
            for command in commands:
                operation, *params = command.split()

                if operation not in self.commands_mapper:
                    print(f'Invalid command {operation}')
                    continue

                self.commands_mapper[operation](params)

                if self.canvas is not None:
                    file.write(f'{self.canvas}\n')

    @validate_parameters
    def create_canvas(self, params: List[str]) -> None:
        self.canvas = Canvas(int(params[0]), int(params[1]))

    @validate_parameters
    def add_line(self, params: List[str]) -> None:
        self._validate_canvas()
        self.canvas.add_line(int(params[0]), int(params[1]), int(params[2]), int(params[3]))

    @validate_parameters
    def add_rectangle(self, params: List[str]) -> None:
        self._validate_canvas()
        self.canvas.add_rectangle(int(params[0]), int(params[1]), int(params[2]), int(params[3]))

    @validate_parameters
    def bucket_fill(self, params: List[str]) -> None:
        self._validate_canvas()
        self.canvas.bucket_fill(int(params[0]), int(params[1]), params[2])

    def _validate_canvas(self) -> None:
        if not self.canvas:
            raise ValueError('Canvas does not exist')


def process_file(filename: str) -> None:
    if not filename:
        print("Filename does not exist")
        return

    commands = read_file(filename)
    CanvasCommandProcessor().process_commands(commands=commands)


if __name__ == '__main__':
    process_file('input.txt')
