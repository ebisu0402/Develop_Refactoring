def check_string(text, repeat_horizontal, repeat_vertical):
    # 1. 文字列の長さチェック
    if len(text) < 5 or len(text) > 10:
        raise ValueError("文字列は5文字以上、10文字以下でなければなりません。")

    # 2. アルファベットチェック
    if not text.isalpha():
        raise ValueError("文字列はアルファベットのみを含む必要があります。")

    # 3. 横に繰り返す
    horizontal_text = text * repeat_horizontal

    # 4. 縦に繰り返す
    result = (horizontal_text + "\n") * repeat_vertical

    return result.strip()  # 最後の余分な改行を削除して返す


# テストケース
if __name__ == "__main__":
    try:
        print(check_string("Hello", 3, 2))  # 例: 正常ケース
    except ValueError as e:
        print(e)

    try:
        print(check_string("HelloWorld", 2, 4))  # 例: 正常ケース
    except ValueError as e:
        print(e)

    try:
        print(check_string("abc12", 2, 3))  # 例: エラーケース
    except ValueError as e:
        print(e)