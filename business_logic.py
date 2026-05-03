def calculate_gacha_probability(pull_num: int) -> float:
    if pull_num <= 0:
        raise ValueError("Invalid pull number")

    # 超过90重置
    if pull_num > 90:
        return 0.006

    # 硬保底
    if pull_num == 90:
        return 1.0

    # 基础概率
    if pull_num <= 73:
        return 0.006

    # 软保底起点
    if pull_num == 74:
        return 0.066

    # 软保底递增
    return 0.066 + (pull_num - 74) * 0.06