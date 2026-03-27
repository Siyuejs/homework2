
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

    # ==========================================
    # 功能2：随机点名
    # ==========================================
    def random_call_students(self):
        """
        随机抽取不重复的学生名单，处理非数字输入异常，限制人数范围
        """
        # 先判断是否已加载学生数据
        if not self.students_dict:
            print("⚠️  提示：请先加载学生数据")
            return

        # 获取学生总人数
        total_count = len(self.students_dict)
        # 循环直到用户输入合法内容
        while True:
            # 获取用户输入
            user_input = input(f"请输入需要点名的人数（总人数：{total_count}）：")
            try:
                # 尝试把用户输入转为整数，非数字会触发ValueError
                call_count = int(user_input)
                # 判断人数是否在合法范围
                if 1 <= call_count <= total_count:
                    # 用random.sample实现不重复的随机抽取
                    selected_students = random.sample(list(self.students_dict.values()), call_count)
                    # 打印点名结果
                    print("\n===== 随机点名名单 =====")
                    for index, student in enumerate(selected_students, 1):
                        print(f"{index}. 姓名：{student.name} | 学号：{student.student_id}")
                    # 输入合法，跳出循环
                    break
                else:
                    # 人数超出范围，给出提示
                    print(f"❌ 输入错误：人数必须在 1 到 {total_count} 之间")

            # 作业要求：捕获非数字输入的ValueError异常
            except ValueError:
                print("❌ 输入错误：请输入有效的整数，不要输入字母、符号等非数字内容")

    # ==========================================
    # 功能3：生成考场安排表
    # ==========================================
    def generate_exam_arrangement(self):
        """
        随机打乱学生顺序，生成考场安排表.txt，符合作业格式要求
        """
        # 先判断是否已加载学生数据
        if not self.students_dict:
            print("⚠️  提示：请先加载学生数据")
            return

        # 1. 把学生列表随机打乱
        student_list = list(self.students_dict.values())
        random.shuffle(student_list)
        # 把打乱后的顺序保存到实例变量，供后续生成准考证使用
        self.exam_seat_list = student_list

        # 2. 写入考场安排表.txt文件
        file_name = "考场安排表.txt"
        try:
            with open(file_name, "w", encoding="utf-8") as f:
                # 作业要求：第一行必须是生成时间
                f.write(f"生成时间：{ExamSystem.get_format_time()}\n")
                # 写入表头
                f.write("考场座位号,姓名,学号\n")
                # 遍历写入每个学生的信息，座位号从1开始递增
                for seat_num, student in enumerate(student_list, 1):
                    f.write(f"{seat_num},{student.name},{student.student_id}\n")

            print(f"✅ 成功：已生成 {file_name}，保存在项目根目录")

        # 捕获文件写入的IO异常
        except IOError as e:
            print(f"❌ 错误：文件写入失败，失败原因：{e}")

    # ==========================================
    # 功能4：生成准考证目录与文件
    # ==========================================
    def generate_admission_tickets(self):
        """
        创建准考证文件夹，为每个学生生成独立的准考证txt文件
        """
        # 检查是否已生成考场安排（必须先有座位号才能生成准考证）
        if not self.exam_seat_list:
            print("⚠️  提示：请先生成考场安排表（先执行功能3）")
            return

        # 文件夹名称
        dir_name = "准考证"
        try:
            # 作业要求：在根目录创建名为「准考证」的文件夹，exist_ok=True避免已存在时报错
            os.makedirs(dir_name, exist_ok=True)

            # 遍历考场顺序，为每个学生生成独立的准考证文件
            for seat_num, student in enumerate(self.exam_seat_list, 1):
                # 作业要求：生成01.txt、02.txt格式的文件名，zfill(2)实现两位数补零
                file_name = f"{str(seat_num).zfill(2)}.txt"
                # 拼接完整的文件路径
                file_path = os.path.join(dir_name, file_name)

                # 写入准考证内容
                with open(file_path, "w", encoding="utf-8") as f:
                    f.write(f"考场座位号：{seat_num}\n")
                    f.write(f"姓名：{student.name}\n")
                    f.write(f"学号：{student.student_id}\n")

            print(f"✅ 成功：已在「{dir_name}」文件夹中生成所有准考证文件")

        # 捕获文件夹创建、文件写入的异常
        except Exception as e:
            print(f"❌ 错误：生成准考证失败，失败原因：{e}")


# ==========================================
# 主程序入口
# ==========================================
def main():
    # 1. 实例化考试系统
    exam_system = ExamSystem()
    # 作业要求：程序启动时读取文本文件
    student_file = "人工智能编程语言学生名单.txt"
    print("===== 学生信息与考场管理系统 =====")
    print("正在初始化系统，加载学生数据...")
    exam_system.load_student_data(student_file)

    # 2. 主菜单循环
    while True:
        print("\n" + "=" * 40)
        print("          系统功能菜单")
        print("=" * 40)
        print("1. 按学号查询学生信息")
        print("2. 随机点名")
        print("3. 生成考场安排表")
        print("4. 生成准考证目录与文件")
        print("5. 退出系统")
        print("-" * 40)

        # 获取用户菜单选择
        choice = input("请输入功能选项（1-5）：")

        # 根据用户选择调用对应功能
        if choice == "1":
            exam_system.search_student_by_id()
        elif choice == "2":
            exam_system.random_call_students()
        elif choice == "3":
            exam_system.generate_exam_arrangement()
        elif choice == "4":
            exam_system.generate_admission_tickets()
        elif choice == "5":
            print("👋 感谢使用，再见！")
            break
        else:
            print("❌ 输入无效，请输入1-5之间的数字")


# 程序启动入口
if __name__ == "__main__":
    main()