# core.py：核心功能模块
# ------------ 功能1：添加学生 ------------
def add_student(students_list, student_info):
    """
    给学生列表添加新学生
    参数：
        students_list：存放所有学生的列表（必须是列表类型）
        student_info：要添加的学生信息（必须是字典类型）
    返回值：
        True：添加成功
        False：添加失败（因为学号重复）
    """
    # 检查学号是否重复：遍历学生列表，看有没有学号和要添加的学生相同的
    for student in students_list:
        if student["学号"] == student_info["学号"]:
            return False  # 学号重复，添加失败
    # 学号不重复，把新学生添加到列表
    students_list.append(student_info)
    return True  # 添加成功

# ------------ 功能2：删除学生 ------------
def delete_student(students_list, delete_id):
    """
    从学生列表中删除指定学号的学生
    参数：
        students_list：学生列表
        delete_id：要删除的学生学号
    返回值：
        True：删除成功
        False：删除失败（找不到该学号的学生）
    """
    # 遍历学生列表，用enumerate获取索引和学生信息（索引用于删除）
    for index, student in enumerate(students_list):
        if student["学号"] == delete_id:
            del students_list[index]  # 删除该索引的学生
            return True  # 删除成功
    return False  # 找不到该学号的学生，删除失败

# ------------ 功能3：查询学生 ------------
def query_student(students_list, keyword):
    """
    查询学生列表中符合关键词的学生
    参数：
        students_list：学生列表
        keyword：查询关键词（学号或姓名的一部分）
    返回值：
        result_list：符合条件的学生列表（空列表表示没有找到）
    """
    result_list = []
    # 遍历学生列表，检查学号或姓名是否包含关键词
    for student in students_list:
        # 把学号和姓名转成小写，方便模糊查询（比如输入“张”能找到“张三”“张四”，输入“zh”也能找到）
        if keyword.lower() in student["学号"].lower() or keyword.lower() in student["姓名"].lower():
            result_list.append(student)
    return result_list

# ------------ 功能4：修改学生成绩 ------------
def modify_student_score(students_list, student_id, subject, new_score):
    """
    修改学生的指定科目成绩
    参数：
        students_list：学生列表
        student_id：要修改的学生学号
        subject：要修改的科目（必须是“数学成绩”或“语文成绩”）
        new_score：新的成绩
    返回值：
        True：修改成功
        False：修改失败（找不到该学号的学生）
    """
    for student in students_list:
        if student["学号"] == student_id:
            student[subject] = new_score  # 修改该学生的指定科目成绩
            return True  # 修改成功
    return False  # 修改失败




# # 测试Core模块
# test_students = []
# # 测试添加学生
# test_student = {"学号": "2024052001", "姓名": "张三", "班级": "一年级一班", "数学成绩": 95, "语文成绩": 90}
# add_result = add_student(test_students, test_student)
# print(f"添加学生结果：{add_result}")  # 应该输出True
# # 测试重复添加
# add_result2 = add_student(test_students, test_student)
# print(f"重复添加学生结果：{add_result2}")  # 应该输出False
# # 测试查询
# query_result = query_student(test_students, "张")
# print(f"查询结果：{query_result}")  # 应该输出[{'学号': '2024052001', ...}]