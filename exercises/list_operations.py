"""
练习: 列表操作

描述：
实现对学生列表的添加、删除和修改操作。

请补全下面的函数，对学生列表进行各种操作。
"""

def student_list_operations(students, operation, *args):
    """
    对学生列表进行操作
    
    参数:
    - students: 学生列表
    - operation: 操作类型 ("add", "remove", "update")
    - args: 操作所需的额外参数
    
    返回:
    - 操作后的学生列表
    """
    # 请在下方编写代码
    if operation == "add":
        # args[0] 是要添加的学生
        students.append(args[0])
    elif operation == "remove":
        # args[0] 是要删除的学生
        if args[0] in students:
            students.remove(args[0])
    elif operation == "update":
        # args[0] 是要修改的原名，args[1] 是新名
        if args[0] in students:
            index = students.index(args[0])
            students[index] = args[1]
    return students