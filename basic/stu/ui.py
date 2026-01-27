# ui.py：用户界面模块
# ------------ 功能1：打印菜单 ------------
# def print_menu():
#     """
#     打印学生管理系统的主菜单
#     为什么用函数？：因为菜单要重复打印，用函数可以避免重复写代码
#     为什么加注释？：让别人（包括未来的自己）知道这个函数是做什么的
#     """
#     # 用分割线美化菜单（零基础可选，只是让菜单好看）
#     print("=" * 40)  # 打印40个=，形成分割线
#     print("       学生管理系统 V1.0")  # 系统标题
#     print("1.  添加学生信息")  # 菜单选项1
#     print("2.  删除学生信息")  # 菜单选项2
#     print("3.  查询学生信息")  # 菜单选项3
#     print("4.  修改学生成绩")  # 菜单选项4
#     print("5.  手动保存数据")  # 菜单选项5
#     print("6.  退出系统")       # 菜单选项6
#     print("=" * 40)  # 结束分割线

# 在ui.py顶部导入colorama库
from colorama import Fore, Style, init
# 初始化colorama（解决Windows的颜色显示问题）
init(autoreset=True)

# 美化后的print_menu()函数
def print_menu():
    print("=" * 40)
    print(Fore.GREEN + "       学生管理系统 V1.0" + Style.RESET_ALL)  # 绿色标题
    print(Fore.CYAN + "1.  添加学生信息" + Style.RESET_ALL)  # 青色选项
    print(Fore.CYAN + "2.  删除学生信息" + Style.RESET_ALL)
    print(Fore.CYAN + "3.  查询学生信息" + Style.RESET_ALL)
    print(Fore.CYAN + "4.  修改学生成绩" + Style.RESET_ALL)
    print(Fore.CYAN + "5.  手动保存数据" + Style.RESET_ALL)
    print(Fore.RED + "6.  退出系统" + Style.RESET_ALL)  # 红色退出选项
    # 在ui.py的print_menu()里添加第7个选项
    print("7.  导出数据为CSV文件")
    print("=" * 40)


# ------------ 功能2：获取用户的有效选择 ------------
def get_user_choice():
    """
    获取用户输入的1-6之间的数字选择
    为什么要做“有效选择”？：防止用户输入非数字（比如abc）或不在1-6的数字（比如7）
    """
    while True:  # 循环，直到用户输入有效选择为止
        try:
            # 获取用户输入的内容，并转成整数（因为input()默认返回字符串）
            choice = int(input("请输入您的选择（1-6）："))
            # 检查输入的数字是否在1-6之间
            if 1 <= choice <= 7:
                return choice  # 返回有效的选择
            else:
                print("输入错误！请输入1-6之间的数字！")  # 提示用户输入错误
        except ValueError:
            # 当用户输入非数字（比如abc）时，会触发ValueError异常
            print("输入错误！请输入数字！")  # 提示用户输入错误

# ------------ 功能3：获取学生的基本信息（用于添加学生） ------------
def get_student_info():
    """
    获取用户输入的学生信息：学号、姓名、班级、数学成绩、语文成绩
    为什么要单独写这个函数？：因为添加学生时需要多次获取用户输入，用函数可以简化代码
    """
    # 1. 获取学号：学号必须是字符串（防止前面的0丢失，比如“2024052001”如果是整数会变成2024052001，但实际是字符串）
    student_id = input("请输入学号：")
    # 2. 获取姓名：直接字符串
    name = input("请输入姓名：")
    # 3. 获取班级：直接字符串
    class_name = input("请输入班级：")
    # 4. 获取数学成绩：必须是整数或浮点数，用try-except处理
    while True:
        try:
            math_score = float(input("请输入数学成绩："))
            break  # 输入有效，跳出循环
        except ValueError:
            print("数学成绩必须是数字！请重新输入！")
    # 5. 获取语文成绩：同样必须是数字
    while True:
        try:
            chinese_score = float(input("请输入语文成绩："))
            break
        except ValueError:
            print("语文成绩必须是数字！请重新输入！")
    # 返回一个字典，包含所有学生信息
    return {
        "学号": student_id,
        "姓名": name,
        "班级": class_name,
        "数学成绩": math_score,
        "语文成绩": chinese_score
    }

# ------------ 功能4：获取要删除的学号 ------------
def get_delete_id():
    """获取用户要删除的学生学号"""
    return input("请输入要删除的学生学号：")

# ------------ 功能5：获取要查询的关键词（学号或姓名） ------------
def get_query_keyword():
    """获取用户要查询的学号或姓名关键词"""
    return input("请输入要查询的学号或姓名关键词：")

# ------------ 功能6：获取要修改的学号和成绩 ------------
def get_modify_info():
    """获取要修改的学生学号和新成绩"""
    student_id = input("请输入要修改的学生学号：")
    # 选择要修改的科目
    while True:
        print("1. 修改数学成绩")
        print("2. 修改语文成绩")
        try:
            subject_choice = int(input("请输入要修改的科目："))
            if subject_choice == 1:
                subject = "数学成绩"
                break
            elif subject_choice == 2:
                subject = "语文成绩"
                break
            else:
                print("输入错误！请输入1或2！")
        except ValueError:
            print("输入错误！请输入数字！")
    # 获取新成绩
    while True:
        try:
            new_score = float(input(f"请输入新的{subject}："))
            break
        except ValueError:
            print(f"{subject}必须是数字！请重新输入！")
    # 返回要修改的学号、科目、新成绩
    return student_id, subject, new_score

# 在ui.py里添加获取导出确认的函数
def get_export_confirm():
    """获取用户是否确认导出的选择"""
    while True:
        confirm = input("确定要导出为CSV文件吗？(y/n)：")
        if confirm.lower() in ["y", "yes"]:
            return True
        elif confirm.lower() in ["n", "no"]:
            return False
        else:
            print("输入错误！请输入y或n！")