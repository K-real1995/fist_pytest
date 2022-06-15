def read_from_file(file) -> list[str]:
    with open(file) as file:
        return file.readlines()
