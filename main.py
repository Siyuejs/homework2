import os
import random
import datetime

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
    