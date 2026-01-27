# db.py：数据存储模块
import json  # 导入Python自带的json模块，用于数据格式化
# 在db.py里导入csv模块
import csv

# 数据文件的路径：把数据保存到项目根目录的student_data.json文件
DATA_FILE_PATH = "student_data.json"

# ------------ 功能1：从json文件读取学生数据 ------------
def load_data():
    """
    从json文件读取学生数据
    返回值：
        students_list：学生列表（如果文件不存在或读取失败，返回空列表）
    """
    try:
        # 打开json文件：r表示只读，encoding="utf-8"防止中文乱码
        with open(DATA_FILE_PATH, "r", encoding="utf-8") as f:
            # 把json字符串转成Python的列表
            students_list = json.load(f)
        return students_list
    except FileNotFoundError:
        # 文件不存在时（第一次运行系统时），返回空列表
        return []
    except json.JSONDecodeError:
        # 文件内容格式错误时，返回空列表
        return []
    except Exception as e:
        # 其他未知错误时，打印错误信息并返回空列表
        print(f"读取数据失败：{e}")
        return []

# ------------ 功能2：把学生数据保存到json文件 ------------
def save_data(students_list):
    """
    把学生列表保存到json文件
    参数：
        students_list：要保存的学生列表
    返回值：
        True：保存成功
        False：保存失败
    """
    try:
        # 打开json文件：w表示写入（覆盖原有内容），encoding="utf-8"防止中文乱码
        # indent=4：保存的json文件格式美化（每个层级缩进4个空格），方便人阅读
        with open(DATA_FILE_PATH, "w", encoding="utf-8") as f:
            json.dump(students_list, f, ensure_ascii=False, indent=4)
        return True  # 保存成功
    except Exception as e:
        # 保存失败时，打印错误信息
        print(f"保存数据失败：{e}")
        return False  # 保存失败

# ------------ 功能3：导出学生数据为CSV文件 ------------
def export_csv(students_list):
    """
    把学生数据导出为CSV文件
    参数：
        students_list：要导出的学生列表
    返回值：
        True：导出成功
        False：导出失败
    """
    csv_file_path = "student_data.csv"
    # 确定CSV的表头（和学生字典的键一致）
    headers = ["学号", "姓名", "班级", "数学成绩", "语文成绩"]
    try:
        # 打开CSV文件：w表示写入，newline=""防止空行，encoding="utf-8-sig"防止Excel打开中文乱码
        with open(csv_file_path, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.DictWriter(f, fieldnames=headers)  # 创建DictWriter对象
            writer.writeheader()  # 写入表头
            writer.writerows(students_list)  # 写入所有学生数据
        return True
    except Exception as e:
        print(f"导出CSV失败：{e}")
        return False

# # 测试DB模块
# test_students = [
#     {"学号": "2024052001", "姓名": "张三", "班级": "一年级一班", "数学成绩": 95, "语文成绩": 90},
#     {"学号": "2024052002", "姓名": "李四", "班级": "一年级二班", "数学成绩": 85, "语文成绩": 80}
# ]
# # 测试保存数据
# save_result = save_data(test_students)
# print(f"保存数据结果：{save_result}")  # 应该输出True
# # 测试读取数据
# load_result = load_data()
# print(f"读取数据结果：{load_result}")  # 应该输出测试的学生列表