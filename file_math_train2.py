import os
import shutil

# 원본 이미지 경로와 대상 경로 설정
source_dir = "./dataset_val_math/images"
target_dir = "./data/math/images/val"
# target_dir = "./data/water/images/val"

# 대상 경로가 없으면 생성
os.makedirs(target_dir, exist_ok=True)

# 모든 폴더의 이미지 파일 복사
for root, dirs, files in os.walk(source_dir):
    for file in files:
        # 이미지 파일만 복사 (jpg, png, jpeg 확장자 등)
        if file.lower().endswith((".jpg", ".png", ".jpeg")):
            source_path = os.path.join(root, file)
            target_path = os.path.join(target_dir, file)

            # 동일한 이름의 파일이 이미 있다면 이름 변경
            if os.path.exists(target_path):
                base, ext = os.path.splitext(file)
                new_file_name = f"{base}_copy{ext}"
                target_path = os.path.join(target_dir, new_file_name)

            # 파일 복사 (원본 유지)
            shutil.copy(source_path, target_path)

print(f"모든 이미지를 {target_dir}로 복사 완료!")
