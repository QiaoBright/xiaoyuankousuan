# 注意事项：

使用前请点个免费的star

版本较粗糙，可能出问题，欢迎大佬来优化

作者对使用造成的任何后果不负责任

只能识别两个数的判断和部分100以内加减法的运算（绘画效果很好，但是小猿口算识别不出来...）


## 相关下载
保持在cmd输入
```shell
pip install pyautogui pillow pytesseract
```

## 下载tesseract

```
https://github.com/tesseract-ocr/tesseract/releases
```
## 也可以通过第三方下载
```
https://digi.bib.uni-mannheim.de/tesseract/
```
## 下载安装tesseract教程链接如下
```
https://blog.csdn.net/SzyPy/article/details/140773600?ops_request_misc=%257B%2522request%255Fid%2522%253A%2522138260D1-C1BF-4DF5-AA74-C5A32457BFE7%2522%252C%2522scm%2522%253A%252220140713.130102334.pc%255Fall.%2522%257D&request_id=138260D1-C1BF-4DF5-AA74-C5A32457BFE7&biz_id=0&utm_medium=distribute.pc_search_result.none-task-blog-2~all~first_rank_ecpm_v1~rank_v31_ecpm-2-140773600-null-null.142^v100^pc_search_result_base7&utm_term=%E5%A6%82%E4%BD%95%E5%9C%A8%20Windows%20%E4%B8%8A%E5%AE%89%E8%A3%85%20Tesseract%20%E5%B9%B6%E6%B7%BB%E5%8A%A0%E4%B8%AD%E6%96%87%E8%AF%AD%E8%A8%80%E6%94%AF%E6%8C%81&spm=1018.2226.3001.4187
```


## 下载脚本
拉取整个仓库，存放于一个文件夹

## 修改脚本

main.py中的地址改成本地地址
```python
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'\
```

## 寻找坐标并修改坐标

将手机投屏至电脑，保证不要移动投屏窗口的位置和大小，保证鼠标可以正常操作手机（就像触屏一样）
如果笔记本电脑十六寸，如图片所示，投屏位置定位一样，后续可以不看
![example](https://github.com/user-attachments/assets/a34c6ecc-86ae-4042-bb8a-91008f385f94)


powershell中进入仓库文件夹，运行find_x_y.py
```shell
cd 输入你的文件夹
python find_x_y.py
```

根据指示移动至 题目识别区域 和 画大小号区域

修改main.py的主函数
```python
def main():
    x_start = 400  # 根据实际情况调整
    y_start = 350  # 根据实际情况调整
    width = 500    # 根据实际情况调整
    height = 100   # 根据实际情况调整

    screenshot_path = "screenshot.png"

    capture_screen_region(x_start, y_start, width, height, screenshot_path)

    math_question = recognize_math_question(screenshot_path)
    print(f"识别到的数学题：{math_question}")

    result = compare_math_question(math_question)

    if result:
        print(f"判断结果：{result}")
        draw_x = 450  # 根据实际情况调整
        draw_y = 800  # 根据实际情况调整
        draw_result(result, draw_x, draw_y)
    else:
        print("无法解析数学题")

```


## 运行
```shell
python main.py
```
