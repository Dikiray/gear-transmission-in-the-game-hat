"""
Fedorenko Dmitriy
"""
NUM_PLAYERS = 3  # must be not less than 2
NUM_ROUNDS = 5   # must be positive
class HatGame:
    def __init__(self, num_players, num_rounds):
        self.num_players = num_players
        self.num_rounds = num_rounds
        self.gap = 0
        self.round_index = 0
        self.player_index = 0

    def __next__(self):
        if self.round_index == self.num_rounds:
            raise StopIteration()
        return self.next_round()

    def __iter__(self):
        return self

    def next_round(self):
        if self.player_index == 0:
            self.gap += 1
        if self.gap == self.num_players - 1 and self.player_index == self.num_players - 1:
            self.round_index += 1
            self.gap = 0
            some = self.player_index
            self.player_index = 0
            return(some, some - 1, self.round_index - 1)
        some = self.player_index
        self.player_index = (self.player_index + 1) % self.num_players
        return(some, (some + self.gap) % self.num_players, self.round_index)


hat_game = HatGame(
    num_players=NUM_PLAYERS,
    num_rounds=NUM_ROUNDS,
)

for explains_index, guesses_index, round_index in hat_game:
    print("{} -> {}, round {}".format(
        explains_index,
        guesses_index,
        round_index))

# 0->1, 1->2, 2->3, 3->4, 4->0
# 0->2, 1->3, 2->4, 3->0, 4->1
# ...
# ... 4->3
