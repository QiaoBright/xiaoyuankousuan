import pyautogui
from PIL import Image, ImageEnhance, ImageOps
import pytesseract
import re
import time
import os

# 设置 Tesseract 可执行文件的路径
pytesseract.pytesseract.tesseract_cmd = os.getenv('TESSERACT_CMD', r'D:\ruanjian\Tesseract\tesseract.exe')

# 定义图像预处理函数

def preprocess_image(image_path):
    img = Image.open(image_path)
    
    # 将图片转换为灰度图像
    img = img.convert('L')
    
    # 自动调整图片对比度
    img = ImageOps.autocontrast(img)
    
    # 二值化图片
    img = img.point(lambda p: p > 128 and 255)
    
    # 保存处理后的图像供检查
    processed_image_path = "screenshot.png"
    img.save(processed_image_path)
    
    return processed_image_path


# 定义捕捉屏幕区域函数

def capture_screen_region(x_start, y_start, width, height, save_path="screenshot.png"):
    region = (x_start, y_start, width, height)
    screenshot = pyautogui.screenshot(region=region)
    screenshot.save(save_path)
    save_path = preprocess_image(save_path)
    return save_path

# 使用 OCR 识别数学题

def recognize_math_question(image_path):
    custom_config = r'--psm 6 -c tessedit_char_whitelist=0123456789?+-='
    result = pytesseract.image_to_string(Image.open(image_path), config=custom_config).strip()
    
    return result

def compare_math_question(question,answer):
    if answer == 'add_and_subtract':
        match = re.match(r'(\d+)\s*([+\-*/])\s*(\d+)', question)
        print('1',match)
    else:
        if "?" in question:
            match = re.match(r"(\d+)\s*\?\s*(\d+)", question)
        else:
            match = re.match(r"(\d+)\s*(\d+)", question)

    
    # 如果匹配到两个数字，继续处理
    if match and answer =='judge':
        num1 = int(match.group(1))  # 获取第一个数字
        num2 = int(match.group(2))  # 获取第二个数字

        # 根据数字大小返回比较结果
        if num1 > num2:
            return '>'
        elif num1 < num2:
            return '<'
        else:
            return '='
    elif match and answer == 'add_and_subtract':
        num1 = int(match.group(1))  # 第一个数字
        operator = match.group(2)  # 运算符
        num2 = int(match.group(3))  # 第二个数字
        # print(num1,operator,num2)
        if operator == '+':
            return  num1 + num2
        else:
            return num1 - num2
    return None

def draw_result(result, x, y):
    pyautogui.FAILSAFE = False  # 可选：关闭鼠标移动到左上角自动停止
    if result == '>':
        # 绘制大于号 ">"
        pyautogui.moveTo(x, y)
        pyautogui.mouseDown(button='left')

    # 右下角移动 (50, 50)
        pyautogui.moveRel(50, 50, duration=0.01)

    # 接着左下角移动 (-50, 50)
        pyautogui.moveRel(-50, 50, duration=0.01)

    # 松开鼠标左键
        pyautogui.mouseUp(button='left')

    elif result == '<':
        # 绘制小于号 "<"
        pyautogui.moveTo(x, y)  # 移动到起始位置
        pyautogui.mouseDown(button='left')

    # 右下角移动 (50, 50)
        pyautogui.moveRel(-50, 50, duration=0.01)

    # 接着左下角移动 (-50, 50)
        pyautogui.moveRel(50, 50, duration=0.01)

    # 松开鼠标左键
        pyautogui.mouseUp(button='left')

    elif result == '=':
        # 绘制等于号 "="
        pyautogui.moveTo(x, y)  # 移动到起始位置
        pyautogui.dragRel(50, 0, duration=0.2)    # 绘制第一条水平线
        pyautogui.moveTo(x, y + 20)  # 移动到下方
        pyautogui.dragRel(50, 0, duration=0.2)    # 绘制第二条水平线

def draw_number(result, x, y):
    """模拟鼠标绘制数字"""
    pyautogui.FAILSAFE = False  # 可选：关闭鼠标移动到左上角自动停止
    pyautogui.moveTo(x, y)  # 移动到指定位置
    a = x
    # 将结果转换为字符串，以便逐个字符绘制
    for char in str(result):
        print(char)
        a += 100  # 将 x 增加 100，准备绘制下一个数字
        pyautogui.mouseDown(button='left')  # 按下鼠标左键
        if char == '0':
            draw_zero()
        elif char == '1':
            draw_one()
        elif char == '2':
            draw_two()
        elif char == '3':
            draw_three()
        elif char == '4':
            draw_four()
        elif char == '5':
            draw_five()
        elif char == '6':
            draw_six()
        elif char == '7':
            draw_seven()
        elif char == '8':
            draw_eight()
        elif char == '9':
            draw_nine()

        # 调整位置为下一个数字

        pyautogui.moveTo(a, y)  # 移动到新的位置
        pyautogui.mouseUp(button='left')  # 松开鼠标左键

    pyautogui.mouseUp(button='left')  # 松开鼠标左键


def draw_zero():
    """绘制数字0的路径"""
    pyautogui.moveRel(50, 0, duration=0.1)  # 向右
    pyautogui.moveRel(0, 80, duration=0.1)  # 向下
    pyautogui.moveRel(-50, 0, duration=0.1)  # 向左
    pyautogui.moveRel(0, -80, duration=0.1)  # 向上


def draw_one():
    """绘制数字1的路径"""
    pyautogui.moveRel(0, 90, duration=0.1)  # 向下


def draw_two():
    """绘制数字2的路径"""
    pyautogui.moveRel(50, 0, duration=0.1)  # 向右
    pyautogui.moveRel(0, 50, duration=0.1)  # 向下
    pyautogui.moveRel(-50, 0, duration=0.1)  # 向左下
    pyautogui.moveRel(0, 50, duration=0.1)  # 向右
    pyautogui.moveRel(50, 0, duration=0.1)  # 向下


def draw_three():
    """绘制数字3的路径"""
    pyautogui.moveRel(50, 0, duration=0.1)  # 向右
    pyautogui.moveRel(0, 50, duration=0.1)  # 向下
    pyautogui.moveRel(-50, 0, duration=0.1)  # 向左
    pyautogui.moveRel(50, 0, duration=0.1)  # 向右
    pyautogui.moveRel(0, 50, duration=0.1)  # 向下
    pyautogui.moveRel(-50, 0, duration=0.1)  # 向左


def draw_four():
    """绘制数字4的路径"""
    pyautogui.moveRel(0, 50, duration=0.1)  # 向下
    pyautogui.moveRel(50, 0, duration=0.1)  # 向右
    pyautogui.moveRel(0, -50, duration=0.1)  # 向上
    pyautogui.moveRel(0, 100, duration=0.1)  # 向上



def draw_five():
    """绘制数字5的路径"""
    pyautogui.moveRel(-50, 0, duration=0.1)  # 向左
    pyautogui.moveRel(0, 50, duration=0.1)  # 向下
    pyautogui.moveRel(50, 0, duration=0.1)  # 向右
    pyautogui.moveRel(0, 50, duration=0.1)  # 向下
    pyautogui.moveRel(-50, 0, duration=0.1)  # 向左



def draw_six():
    """绘制数字6的路径"""
    pyautogui.moveRel(-50, 0, duration=0.1)  # 向左
    pyautogui.moveRel(0, 100, duration=0.1)  # 向下
    pyautogui.moveRel(50, 0, duration=0.1)  # 向右
    pyautogui.moveRel(0, -50, duration=0.1)  # 向上
    pyautogui.moveRel(-50, 0, duration=0.1)  # 向左


def draw_seven():
    """绘制数字7的路径"""
    pyautogui.moveRel(50, 0, duration=0.1)
    pyautogui.moveRel(0, 100, duration=0.1)  # 向下


def draw_eight():
    pyautogui.moveRel(-50, 0, duration=0.1)  # 向左
    pyautogui.moveRel(0, -50, duration=0.1)  # 向上
    pyautogui.moveRel(50, 0, duration=0.1)  # 向右
    pyautogui.moveRel(0, 100, duration=0.1)  # 向下
    pyautogui.moveRel(-50, 0, duration=0.1)  # 向左
    pyautogui.moveRel(0, -50, duration=0.1)  # 向上


def draw_nine():
    """绘制数字9的路径"""
    pyautogui.moveRel(-50, 0, duration=0.1)  # 向左
    pyautogui.moveRel(0, -50, duration=0.1)  # 向上
    pyautogui.moveRel(50, 0, duration=0.1)  # 向右
    pyautogui.moveRel(0, 100, duration=0.1)  # 向下
    pyautogui.moveRel(-50, 0, duration=0.1)  # 向左




# 主程序流程
def main():
    answer = 'judge'
    if answer == 'judge':
        x_start = 1550
    else:
        x_start = 1500
    y_start = 375
    width = 250
    height = 100

    screenshot_path = "screenshot.png"

    capture_screen_region(x_start, y_start, width, height, screenshot_path)

    math_question = recognize_math_question(screenshot_path)
    print(f"识别到的数学题：{math_question}")

    result = compare_math_question(math_question,answer)
    
    if result:
        print(f"判断结果：{result}")
        draw_x = 1689
        draw_y = 753
        if answer == 'judge':
            draw_result(result, draw_x, draw_y)
        else:
            draw_number(result,draw_x,draw_y)

    else:
        print("无法解析数学题")

if __name__ == "__main__":
    start_time = time.time()  # 记录程序开始运行的时间
    try:
        while True:
            main()  # 执行主函数
            time.sleep(0.3)  # 每次循环后等待 0.5 秒
            
            elapsed_time = time.time() - start_time
            if elapsed_time > 10:  # 如果超过 25 秒，则停止程序
                print("程序已自动运行 25 秒，停止运行")
                break  # 跳出循环，终止程序

    except KeyboardInterrupt:
        print("程序已手动终止")
    except Exception as e:
        print(f"发生错误：{e}")
