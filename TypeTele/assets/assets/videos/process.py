import os

def replace_with_compressed(root_dir):
    for dirpath, dirnames, filenames in os.walk(root_dir):
        for filename in filenames:
            if filename.endswith("_compressed.mp4"):
                compressed_path = os.path.join(dirpath, filename)
                original_name = filename.replace("_compressed", "")
                original_path = os.path.join(dirpath, original_name)

                # 删除原文件
                if os.path.exists(original_path):
                    print(f"Deleting original: {original_path}")
                    os.remove(original_path)

                # 重命名压缩文件
                print(f"Renaming {compressed_path} -> {original_path}")
                os.rename(compressed_path, original_path)

# 修改为你的根目录
replace_with_compressed(".")
