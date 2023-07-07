def read_file(filename: str) -> list | None:
    try:
        with open(filename, 'r') as file:
            commands = file.readlines()
            return commands
    except IOError:
        print(f'Could not read the file {filename}')
        return
