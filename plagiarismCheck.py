import sys
import re

def preprocess_text(text):
    # 移除非中文、英文和数字的字符
    text = re.sub(r'[^\u4e00-\u9fa5a-zA-Z0-9]', ' ', text)
    # 将多个空格替换为单个空格
    text = re.sub(r'\s+', ' ', text)
    return text.strip()

def read_file(file_path):
    # 文件读取
    try:
        with open(file_path, mode='r', encoding='utf-8') as file:
            file_content = file.read()
            return file_content
    except FileNotFoundError:
        print("文件不存在")
        sys.exit(1)
    except Exception as e:
        print(f"读取文件时出错：{e}")
        sys.exit(1)

def write_result(output_path, similarity):
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"{similarity:.2f}")
        print("结果已写入")
    except Exception as e:
        print(f"写入文件时出错：{e}")
        sys.exit(1)

if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit(1)    #输入格式检测
    
    # 获取命令行参数
    original_file = sys.argv[1]
    copied_file = sys.argv[2]
    output_file = sys.argv[3]

    original_content = read_file(original_file)
    copied_content = read_file(copied_file)
    