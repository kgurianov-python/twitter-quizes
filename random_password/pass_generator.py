
import random
import string
from enum import Enum
from typing import Collection, Hashable

DEFAULT_REQUIREMENTS = [string.ascii_uppercase, string.ascii_lowercase, string.punctuation]


class Strength(Enum):
    WEAK = 5
    STRONG = 8
    VERY_STRONG = 12


def generate_password(required: Collection[Hashable] = None) -> str:
    strength = get_user_input()
    limits = {}
    if not required:
        required = DEFAULT_REQUIREMENTS.copy()

    # randomize the spread between required character sets, make sure each appears at least once
    while len(required) > 1:
        limits[required.pop()] = random.randint(1, strength.value - len(required) - sum(limits.values()))
    limits[required.pop()] = strength.value - sum(limits.values())

    # candidates = [random.choices(key, k=value) for key, value in limits.items()]
    password_array = [char for required_sample in [random.choices(key, k=value) for key, value in limits.items()] for
                      char in required_sample]
    random.shuffle(password_array)
    return "".join(password_array)


def get_user_input():
    while True:
        try:
            options = ", ".join(([f"{idx + 1}: {value.name}" for idx, value in enumerate(Strength)]))
            strength = int(input(f"Please select the password strength ({options})"))
            return list(Strength)[strength - 1]
        except (ValueError, IndexError):
            print("Invalid input, please choose valid value")


if __name__ == '__main__':

    print(f"{generate_password() = }")

    required_chars = ['ABC-XYZ', '1', '&']
    print(f"{generate_password(required_chars.copy()) = }")
