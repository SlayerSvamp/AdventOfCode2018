from decorators import timer


class Node():
    def __init__(self, data):
        self.next = self
        self.prev = self
        self.data = data

    def insert_after(self, node):
        self.next = node.next
        self.prev = node
        self.prev.next = self
        self.next.prev = self
        return self

    def remove(self):
        self.next.prev = self.prev
        self.prev.next = self.next
        return self

    def loop(self):
        yield self
        cur = self.next
        while cur != self:
            yield cur
            cur = cur.next


@timer
def play(n_players, last_marble):
    current = Node(0)
    player = Node(0)
    for _ in range(n_players-1):
        player = Node(0).insert_after(player)

    for marble in range(1, last_marble + 1):
        player = player.next
        if marble % 23:
            current = Node(marble).insert_after(current.next)
        else:
            for _ in range(6):
                current = current.prev
            player.data += marble + current.prev.remove().data

    return max(player.loop(), key=lambda x: x.data).data


data = '405 players; last marble is worth 71700 points'
n_players, last_marble = tuple(int(x) for x in data.split() if x.isdigit())

print('Part One:', play(n_players, last_marble))
print('Part Two:', play(n_players, last_marble * 100))
