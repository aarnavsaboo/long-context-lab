from itertools import product


def sweep(lengths=(2048, 8192, 32768), positions=(0.05, 0.5, 0.95), repeats=3):
    for length, position, repeat in product(lengths, positions, range(repeats)):
        yield {
            "target_chars": int(length * 4),
            "position": position,
            "seed": f"{length}-{position}-{repeat}",
        }
