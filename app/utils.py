def identifier_generator():
    identifier = 1
    while True:
        yield identifier
        identifier += 1

#identifiers = identifier_generator()


class Cube:
    def __init__(self, data, size: int) -> None:
        self.name = next(identifier_generator())
        self.size = size
        self.u = data[0]
        self.f = data[1]
        self.r = data[2]
        self.b = data[3]
        self.l = data[4]
        self.d = data[5]

    @property
    def info(self) -> str:
        return f"name: {self.name}, u: {self.u}, r: {self.r}, l: {self.l}, b: {self.b}"


class BucketSpace:
    def __init__(self) -> None:
        self.pointer = None

    @property
    def __get_name(self):
        return "X" if not self.pointer else self.pointer.name

    @property
    def display(self):
        return f"  {self.__get_name}  "

    def __str__(self) -> str:
        return self.display



class Bucket:
    @staticmethod
    def __generage_bucket(sx: int, sy: int):
        return [[BucketSpace() for _ in range(sx)] for _ in range(sy)]

    def __init__(self, size_x: int, size_y: int) -> None:
        self.size_x = size_x
        self.size_y = size_y
        self.memory = self.__generage_bucket(self.size_x, self.size_y)
        self.cubes = []

    def __str__(self) -> str:
        cout = ""
        for row in self.memory:
            cout += f"[{','.join([space.display for space in row])}]\n"
        cout += "\ncubes info:\n\n"
        for i, cube in enumerate(self.cubes):
            cout += f"{i+1}. {cube.info}\n"

        return cout

    def insert_cube(self, cube: Cube):
        self.cubes.append(cube)
        ...
