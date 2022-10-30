import math
import sys
from typing import Sequence, Tuple

import numpy as np

# Save humans, destroy zombies!


def dist(_a: Tuple[int, int], _b: Tuple[int, int]):
    a, b = np.array(_a), np.array(_b)
    return np.linalg.norm(a - b)


save = -1

# game loop
while True:
    x, y = [int(i) for i in input().split()]
    human_count = int(input())
    humans = []
    for i in range(human_count):
        human_id, human_x, human_y = [int(j) for j in input().split()]
        humans.append((human_id, human_x, human_y))
    zombie_count = int(input())
    zombies = []
    for i in range(zombie_count):
        zombie_id, zombie_x, zombie_y, zombie_xnext, zombie_ynext = [
            int(j) for j in input().split()
        ]
        zombies.append((zombie_id, zombie_x, zombie_y))

    def time_for_ash_to_reach(_a: Sequence[int]):
        return dist((x, y), (_a[1], _a[2])) / 1000

    def time_for_z_to_reach(_a: Sequence[int]):
        return min([dist((_a[1], _a[2]), (z[1], z[2])) for z in zombies]) / 400

    save_l = list(filter(lambda h: h[0] == save, humans))
    if save == -1 or len(save_l) == 0:
        savable_humans = list(
            filter(lambda h: time_for_ash_to_reach(h) < time_for_z_to_reach(h), humans)
        )
        if len(savable_humans) == 0:
            savable_humans = humans[:1]
        savable_humans = sorted(savable_humans, key=lambda h: time_for_z_to_reach(h))
        id, x, y = savable_humans[0]
        save = id
    else:
        _, x, y = save_l[0]

    # Write an action using print
    # To debug: print("Debug messages...", file=sys.stderr, flush=True)

    # Your destination coordinates
    print(f"{x} {y}")
