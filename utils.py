def validate_parameters(action):
    """This decorator validate all input parameters from input.txt file"""

    def inner(*args, **kwargs):
        try:
            action(*args, *kwargs)
        except IndexError:
            raise ValueError('Missing input parameters')
        return action(*args, *kwargs)
    return inner


def read_file(filename: str) -> list | None:
    try:
        with open(filename, 'r') as file:
            commands = file.readlines()
            return commands
    except IOError:
        print(f'Could not read the file {filename}')
        return
