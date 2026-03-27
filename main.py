
import datetime
import os
import random

class Student:
    def __init__(self, student_id, name, gender, class_name, college):
        """
        初始化方法：创建学生对象时，给对象绑定属性
        :param student_id: 学生学号
        :param name: 学生姓名
        :param gender: 学生性别
        :param class_name: 学生班级
        :param college: 学生所属学院
        """
        # 把传入的参数，赋值给当前学生对象的属性
        self.student_id = student_id
        self.name = name
        self.gender = gender
        self.class_name = class_name
        self.college = college

    def __str__(self):
        """
        字符串魔术方法：当print(学生对象)时，自动调用该方法，返回友好的可读信息
        """
        return f"学号：{self.student_id} | 姓名：{self.name} | 性别：{self.gender} | 班级：{self.class_name} | 学院：{self.college}"



    # ==========================================
    # 作业要求：ExamSystem逻辑控制类，所有功能封装为类的方法
    # ==========================================
    class ExamSystem:
        def __init__(self):
            """
            初始化系统：创建空的学生字典存储数据，创建空列表存储考场顺序
            """
            # 学生字典格式：{学号: Student对象}，方便快速按学号查找
            self.students_dict = {}
            # 考场座位顺序列表，存储打乱后的Student对象，供准考证生成使用
            self.exam_seat_list = []

        # ==========================================
        # 作业要求：静态方法，满足至少一个@staticmethod的要求
        # ==========================================
        @staticmethod
        def get_format_time():
            """
            静态方法：获取格式化的当前时间，用于考场安排表的生成时间
            无需实例化类即可调用，直接用ExamSystem.get_format_time()
            """
            return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        # ==========================================
        # 功能1-初始化：读取学生名单文件
        # ==========================================
        def load_student_data(self, file_path):
            """
            读取指定的学生名单txt文件，解析后存入students_dict
            :param file_path: 学生名单文件的路径
            :return: 读取成功返回True，失败返回False
            """
            try:
                # 用utf-8编码打开文件，避免中文乱码
                with open(file_path, "r", encoding="utf-8") as f:
                    # 读取所有行
                    all_lines = f.readlines()
                    # 跳过第一行表头（序号	姓名	性别	班级	学号	学院）
                    for line in all_lines[1:]:
                        # 去除每行首尾的空白符、换行符
                        line = line.strip()
                        # 跳过空行
                        if not line:
                            continue
                        # 按制表符\t分割（适配你提供的名单格式）
                        parts = line.split("\t")
                        # 确保分割后有6列数据（序号、姓名、性别、班级、学号、学院）
                        if len(parts) == 6:
                            # 提取对应字段，注意索引顺序
                            serial_num, name, gender, class_name, student_id, college = parts
                            # 创建Student对象，存入学生字典
                            self.students_dict[student_id] = Student(student_id, name, gender, class_name, college)

                # 读取完成，打印提示
                print(f"✅ 初始化成功，共加载 {len(self.students_dict)} 名学生信息")
                return True

            # 作业要求：捕获文件不存在的异常，给出友好提示
            except FileNotFoundError:
                print(f"❌ 错误：找不到文件 {file_path}，请确保文件在项目文件夹内")
                return False

    # ==========================================
    # 功能1-查找：按学号查询学生信息
    # ==========================================
    def search_student_by_id(self):
        """
        用户输入学号，查询并打印学生完整信息
        学号不存在时，给出友好错误提示
        """
        # 先判断是否已加载学生数据
        if not self.students_dict:
            print("⚠️  提示：请先加载学生数据")
            return

        # 获取用户输入的学号
        input_id = input("请输入要查询的学生学号：")
        # 判断学号是否在字典中
        if input_id in self.students_dict:
            # 存在则打印信息，自动调用Student类的__str__方法
            print("\n===== 学生信息查询结果 =====")
            print(self.students_dict[input_id])
        else:
            # 不存在则给出友好提示
            print(f"❌ 错误：未找到学号为 {input_id} 的学生，请检查学号是否正确")