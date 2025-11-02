from pathlib import Path

MOVES = {'^': (0, 1),
         'v': (0, -1),
         '>': (1, 0),
         '<': (-1, 0)
         }

class DeliveryPerson:
    def __init__(self, name: str):
        self.name = name
        self.x = 0
        self.y = 0

    def move(self, direction: str):
        dx, dy = MOVES[direction]
        self.x += dx
        self.y += dy
        return (self.x, self.y)


class PizzaDelivery:
    def __init__(self, instructions: str):
        self.instructions = instructions
        self.visited = {(0, 0)}

    def deliver_single(self):
        maria = DeliveryPerson("Maria")
        for move in self.instructions:
            self.visited.add(maria.move(move))
        return len(self.visited)

    def deliver_with_clovis(self):
        maria = DeliveryPerson("Maria")
        clovis = DeliveryPerson("Clovis")
        for i, move in enumerate(self.instructions):
            person = maria if i % 2 == 0 else clovis
            self.visited.add(person.move(move))
        return len(self.visited)


def main(path="input.txt"):
    instructions = Path(path).read_text().strip()
    game = PizzaDelivery(instructions)

    print("Part 1:", game.deliver_single(), "houses received at least one pizza.")
    print("Part 2:", game.deliver_with_clovis(), "houses received at least one pizza.")


if __name__ == "__main__":
    main()
