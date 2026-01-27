import random
import string

def generate_random_alphanumeric(length=32):
    """
    生成指定长度的随机数字和字母组合
    """
    # 定义数字和字母字符集
    characters = string.ascii_letters + string.digits
    # 随机选择字符并连接成字符串
    random_string = ''.join(random.choice(characters) for _ in range(length))
    return random_string

# 生成32位随机数
random_result = generate_random_alphanumeric(32)
print("suijis:", random_result)