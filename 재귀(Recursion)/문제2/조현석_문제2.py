from enum import Enum


class Position:
    def __init__(self, x, y):
        self.x = int(x)
        self.y = int(y)

    def __eq__(self, other):
        return (self.x, self.y) == (other.x, other.y)


class Maze:
    def __init__(self, maze_size: int, walls: list, exit: Position):
        self.exit = exit
        self.maze_size = maze_size
        self.walls = walls


class Person:
    def __init__(self, position, direction):
        self.position = position
        self.direction = direction
        self.ways = ["forward", "right", "backward"]

    def move(self, way):
        if way == "forward":
            self.direction = self.direction
        elif way == "right":
            self.direction = self.Direction((self.direction.value + 1) % 4)
        elif way == "backward":
            self.direction = self.Direction((self.direction.value + 2) % 4)
        dx = [0, 1, 0, -1]
        dy = [-1, 0, 1, 0]
        self.position.x += dx[self.direction.value]
        self.position.y += dy[self.direction.value]

    class Direction(Enum):
        NORTH = 0
        EAST = 1
        SOUTH = 2
        WEST = 3


class Case:
    def __init__(self, maze):
        self.__maze = maze
        self.__aeguk = Person(Position(0, 0), Person.Direction.EAST)
        self.__visited = [[[0, 0, 0, 0] for i in range(maze.maze_size)] for i in range(maze.maze_size)]

    def escape(self):
        current_direction, current_position = self.__get_current_state()
        if current_position == self.__maze.exit:
            return True
        else:
            self.__set_visited()
            for way in self.__aeguk.ways:
                self.__aeguk.move(way)
                if not self.__is_wall(self.__aeguk.position) and not self.__is_visited():
                    if self.escape() is True:
                        return True
                self.__restore_state(current_position, current_direction)
            return False

    def __is_wall(self, position):
        if (
                position.x < 0 or
                position.x >= self.__maze.maze_size or
                position.y < 0 or
                position.y >= self.__maze.maze_size or
                Position(position.x, position.y) in self.__maze.walls
        ):
            return True

    def __is_visited(self):
        return self.__visited[self.__aeguk.position.x][self.__aeguk.position.y][self.__aeguk.direction.value]

    def __set_visited(self):
        self.__visited[self.__aeguk.position.x][self.__aeguk.position.y][self.__aeguk.direction.value] = 1

    def __get_current_state(self):
        current_position = Position(self.__aeguk.position.x, self.__aeguk.position.y)
        current_direction = Person.Direction(self.__aeguk.direction.value)
        return current_direction, current_position

    def __restore_state(self, current_position, current_direction):
        self.__aeguk.position = current_position
        self.__aeguk.direction = current_direction


class FileInput:
    def __init__(self, file_name):
        self.__file_name = file_name
        self.__cases = []
        self.__deserialize()

    def __deserialize(self):
        with open(self.__file_name, "r") as f:
            lines = f.readlines()

        i = 1
        while i < len(lines):
            maze_size = int(lines[i])
            wall = []
            for j in range(i + 1, i + 1 + maze_size):
                for k in range(maze_size):
                    if lines[j][k * 2] == '1':
                        wall.append(Position(k, j - i - 1))
            exit = Position(*lines[i + maze_size + 1].split())
            maze = Maze(maze_size, wall, exit)
            i += maze_size + 2
            self.__cases.append(Case(maze))

    def get_cases(self):
        return self.__cases


cases = FileInput("./input.txt").get_cases()
for case in cases:
    print(case.escape())
