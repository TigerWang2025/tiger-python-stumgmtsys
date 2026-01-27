# main.py：主程序入口（必须运行这个文件，系统才会启动）
# 导入所有模块
import ui  # 导入UI模块
import core  # 导入Core模块
import db  # 导入DB模块

# ------------ 主程序的核心逻辑 ------------
def main():
    """主程序函数"""
    # 1. 初始化：从json文件读取已保存的学生数据
    students = db.load_data()
    print("数据加载完成！")

    # 2. 主循环：不断显示菜单、处理用户选择
    while True:
        # 2.1 打印菜单
        ui.print_menu()
        # 2.2 获取用户的有效选择
        choice = ui.get_user_choice()
        # 2.3 根据选择执行对应的功能
        if choice == 1:
            # 选择1：添加学生
            student_info = ui.get_student_info()  # 获取学生信息
            add_result = core.add_student(students, student_info)  # 调用Core模块添加学生
            if add_result:
                print("添加学生成功！")
            else:
                print("添加学生失败！学号已存在！")
        elif choice == 2:
            # 选择2：删除学生
            delete_id = ui.get_delete_id()  # 获取要删除的学号
            delete_result = core.delete_student(students, delete_id)  # 调用Core模块删除学生
            if delete_result:
                print("删除学生成功！")
            else:
                print("删除学生失败！未找到该学号的学生！")
        elif choice == 3:
            # 选择3：查询学生
            keyword = ui.get_query_keyword()  # 获取查询关键词
            query_result = core.query_student(students, keyword)  # 调用Core模块查询学生
            if query_result:
                # 打印查询结果（美化格式）
                print("查询结果如下：")
                print("-" * 50)
                for student in query_result:
                    print(f"学号：{student['学号']}")
                    print(f"姓名：{student['姓名']}")
                    print(f"班级：{student['班级']}")
                    print(f"数学成绩：{student['数学成绩']}")
                    print(f"语文成绩：{student['语文成绩']}")
                    print("-" * 50)
            else:
                print("未找到符合条件的学生！")
        elif choice == 4:
            # 选择4：修改成绩
            student_id, subject, new_score = ui.get_modify_info()  # 获取修改信息
            modify_result = core.modify_student_score(students, student_id, subject, new_score)  # 调用Core模块修改成绩
            if modify_result:
                print("修改成绩成功！")
            else:
                print("修改成绩失败！未找到该学号的学生！")
        elif choice == 5:
            # 选择5：手动保存数据
            save_result = db.save_data(students)  # 调用DB模块保存数据
            if save_result:
                print("手动保存数据成功！")
            else:
                print("手动保存数据失败！")
        elif choice == 6:
            # 选择6：退出系统
            print("正在退出系统...")
            # 退出前自动保存数据
            save_result = db.save_data(students)
            if save_result:
                print("数据已自动保存！")
            else:
                print("数据自动保存失败！请手动保存！")
            print("系统已退出！")
            break  # 跳出主循环，结束程序
        # 在main.py的主循环里添加第7个选择
        elif choice == 7:
            # 选择7：导出数据为CSV文件
            confirm = ui.get_export_confirm()  # 获取确认
            if confirm:
                export_result = db.export_csv(students)  # 调用DB模块导出CSV
                if export_result:
                    print("导出CSV成功！文件已保存为student_data.csv！")
                else:
                    print("导出CSV失败！")
            else:
                print("已取消导出！")

# ------------ 运行主程序 ------------
if __name__ == "__main__":
    # 只有当直接运行main.py时，才会执行main()函数
    # 这样可以防止import main时自动运行main()函数
    main()