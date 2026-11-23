"""Dad Joke Showdown entry.

Writes one original dad joke to /output/entry.txt.

Python 3.13, standard library only, no network access.
Fully deterministic: the same bytes are written on every run.
"""

import os

JOKE = "My dad started a band called The Leftovers. We only play reheated hits."

OUTPUT_PATH = "/output/entry.txt"
MAX_CHARS = 200


def main():
    joke = JOKE
    if joke != joke.strip():
        raise ValueError("joke must not start or end with whitespace")
    if not joke.isprintable():
        raise ValueError("joke must be printable text")
    if not 1 <= len(joke) <= MAX_CHARS:
        raise ValueError("joke must be 1 to 200 characters")
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as handle:
        handle.write(joke)


if __name__ == "__main__":
    main()
