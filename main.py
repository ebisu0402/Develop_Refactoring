import numpy as np
from check_and_repeat import check_string


# ランダムな数を生成して関数を呼び出す
def main():
    # ランダムな数を生成
    repeat_horizontal = np.random.randint(1, 11)  # 1から10までのランダムな整数
    repeat_vertical = np.random.randint(1, 11)

    # 関数を呼び出し
    try:
        result = check_string("Hello", repeat_horizontal, repeat_vertical)
        print(result)
    except ValueError as e:
        print(f"エラー: {e}")


# 実行
if __name__ == "__main__":
    main()

# TODO:
