class RandomGenerator:
    def __init__(self, seed, a=1664525, c=1013904223, m=2**32):
        self.seed = seed
        self.a = a
        self.c = c
        self.m = m

    def rand(self):
        self.seed = (self.a * self.seed + self.c) % self.m
        return self.seed

    def rand_in_range(self, min_value, max_value):
        return min_value + (self.rand() % (max_value - min_value + 1))

rng = RandomGenerator(seed=12345)
for _ in range(10):
    print(rng.rand_in_range(1, 100))