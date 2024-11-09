import random


def print_random():
    # 0から1億の範囲のランダムな数の100万個のリスト
    large_set = set(random.randint(0, 100000000) for _ in range(1000000))

    # 0から1億の範囲のランダムな数の100個のリスト
    small_list = [random.randint(0, 100000000) for _ in range(100)]

    # small_list の各要素が large_set に含まれていれば表示
    for num in small_list:
        if num in large_set:
            print(f"Found: {num}")


if __name__ == "__main__":
    print_random()
