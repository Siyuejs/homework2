#邓杰鸿-24311008-第二次人工智能编程作业

## 1. 任务拆解与 AI 协作策略
我将本次大任务拆解为6个分步实现的小任务，按顺序引导AI完成开发：
步骤1：先让AI实现Student数据类，严格要求包含__init__和__str__方法，
步骤2：让AI搭建ExamSystem逻辑控制类框架，实现静态方法和文件读取功能，添加FileNotFoundError异常处理，适配提供的制表符格式学生名单
步骤3：实现学号查找功能，要求对不存在的学号给出提示
步骤4：实现随机点名功能，要求处理非数字输入的ValueError异常，限制人数范围，保证抽取不重复
步骤5：实现考场安排表生成功能，严格按照作业要求的格式，第一行添加生成时间，包含座位号、姓名、学号
步骤6：实现准考证生成功能，要求创建指定文件夹，生成01.txt格式的文件，最后添加主程序菜单，串联所有功能

## 2. 核心 Prompt 迭代记录
### 初代 Prompt：
帮我写一个Python随机点名功能，用户输入人数，返回随机学生名单
### AI 生成的问题/缺陷：
1.  没有使用面向对象编程，代码是面向过程的
2.  没有处理用户输入非数字的异常，输入字母会直接崩溃
3.  没有限制输入人数的范围，输入超过总人数的数字会报错
4.  没有保证抽取的学生不重复
### 优化后的 Prompt ：
请把这个随机点名功能封装到ExamSystem类的方法中，满足以下要求：
1.  使用面向对象编程，基于已有的Student类实现
2.  必须用try-except捕获用户输入非数字的ValueError异常，给出友好提示
3.  必须限制用户输入的人数在1到学生总人数之间，超出范围给出提示
4.  必须保证抽取的学生不重复，使用Python标准库实现，不能用第三方库
5.  打印的结果要包含学生姓名和学号

## 3. Debug 与异常处理记录
### 报错类型/漏洞现象：
FileNotFoundError，程序启动时提示找不到「人工智能编程语言学生名单.txt」文件，后续功能全部无法使用
### 解决过程：
将报错显示的内容复制粘贴到豆包询问是哪里错误了，定位到报错出现在load_student_data方法的文件打开步骤，原因是代码没有处理文件不存在的情况，当文件名称错误、路径不对时会直接崩溃。
给文件打开的代码块加上了try-except，捕获FileNotFoundError异常，同时给出友好的错误提示，告诉用户检查文件是否在项目文件夹内，修改后程序即使找不到文件也不会崩溃，会正常提示用户。
最终修改的核心代码：给load_student_data方法加上了try-except异常处理块，捕获文件不存在的异常。

## 4. 人工代码审查 (Code Review)
```python
# 随机点名核心方法，人工逐行注释
def random_call_students(self):
    # 先判断学生字典是否为空，避免未加载数据时执行功能报错
    if not self.students_dict:
        print("⚠️  提示：请先加载学生数据")
        return
    
    # 获取学生总人数，用于后续人数范围校验
    total_count = len(self.students_dict)
    # 循环接收用户输入，直到输入合法才退出
    while True:
        # 提示用户输入点名人数，同时显示总人数，给用户明确的输入范围
        user_input = input(f"请输入需要点名的人数（总人数：{total_count}）：")
        try:
            # 尝试把用户输入的字符串转为整数，非数字内容会触发ValueError异常
            call_count = int(user_input)
            # 校验输入的人数是否在1-总人数的合法范围内
            if 1 <= call_count <= total_count:
                # 用random.sample实现不重复的随机抽取，第一个参数是待抽取的列表，第二个是抽取数量
                selected_students = random.sample(list(self.students_dict.values()), call_count)
                # 打印点名结果的表头
                print("\n===== 随机点名名单 =====")
                # 遍历抽取的学生，用enumerate生成序号，从1开始
                for index, student in enumerate(selected_students, 1):
                    # 打印每个学生的姓名和学号
                    print(f"{index}. 姓名：{student.name} | 学号：{student.student_id}")
                # 输入合法且执行完成，跳出while循环
                break
            else:
                # 人数超出范围，给用户明确的错误提示
                print(f"❌ 输入错误：人数必须在 1 到 {total_count} 之间")
        
        # 捕获用户输入非数字的异常，符合作业的异常处理要求
        except ValueError:
            # 给用户友好的错误提示，告诉用户正确的输入格式
            print("❌ 输入错误：请输入有效的整数，不要输入字母、符号等非数字内容")
