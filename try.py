import re

def parse_question(question):
    # 判断 question 中是否包含问号
    if "?" in question:
        # 匹配含问号的格式，如 "14 ? 11"
        match = re.match(r"(\d{1,2})\s*\?\s*(\d{1,2})", question)
    else:
        # 匹配没有问号的格式，如 "1411" 或 "14 11"
        match = re.match(r"(\d{1,2})\s*(\d{1,2})", question)

    # 检查是否匹配成功
    if match:
        num1, num2 = match.groups()
        print(f"解析出的数字: {num1}, {num2}")
        return num1, num2
    else:
        print("无法解析数学题")
        return None

# 示例
question_with_question_mark = "14 ? 11"
question_without_question_mark = "14 11"

parse_question(question_with_question_mark)
parse_question(question_without_question_mark)
