def calculate_gacha_probability(pull_num: int) -> float:
    if pull_num <= 0:
        raise ValueError

    if pull_num >= 90:
        return 1.0

    if pull_num < 74:
        return 0.006

    return 0.006 + (pull_num - 73) * 0.06