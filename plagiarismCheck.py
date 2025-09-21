import sys
import re
from Levenshtein import ratio as levenshtein_ratio

def preprocess_text(text):
    # 只保留中文、英文和数字
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

def write_result(output_path, answer):
    try:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(f"{answer:.2f}")
        print("结果已写入")
    except Exception as e:
        print(f"写入文件时出错：{e}")
        sys.exit(1)

def levenshtein(original_text, copied_text):
    ori_word = preprocess_text(original_text)
    cp_word = preprocess_text(copied_text)
    # 如果文本过长，采样计算
    max_length = 10000
    if len(ori_word) > max_length or len(cp_word) > max_length:
        sample_size = min(max_length, len(ori_word), len(cp_word))
        ori_sample = ori_word[:sample_size] if len(ori_word) > sample_size else ori_word
        cp_sample = cp_word[:sample_size] if len(cp_word) > sample_size else cp_word
        return levenshtein_ratio(ori_sample, cp_sample)
    
    return levenshtein_ratio(ori_word, cp_word)

if __name__ == "__main__":

    if len(sys.argv) != 4:
        sys.exit(1)    #输入格式检测
    
    # 获取命令行参数
    original_file = sys.argv[1]
    copied_file = sys.argv[2]
    output_file = sys.argv[3]

    original_content = read_file(original_file)
    copied_content = read_file(copied_file)

    answer = levenshtein(original_content, copied_content)

    write_result(output_file, answer)
    