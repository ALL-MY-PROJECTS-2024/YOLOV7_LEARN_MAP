import os
import shutil

def copy_json_files(source_folder, target_folder):
    # 타겟 폴더가 없으면 생성
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # 소스 폴더에서 모든 하위 폴더 탐색
    for root, _, files in os.walk(source_folder):
        for file in files:
            if file.endswith('.json'):  # JSON 파일인지 확인
                source_path = os.path.join(root, file)
                target_path = os.path.join(target_folder, file)

                # 동일 이름 파일이 존재하면 이름 변경 (중복 방지)
                if os.path.exists(target_path):
                    base, ext = os.path.splitext(file)
                    counter = 1
                    while os.path.exists(target_path):
                        target_path = os.path.join(target_folder, f"{base}_{counter}{ext}")
                        counter += 1

                # 파일 복사
                shutil.copy2(source_path, target_path)
                print(f"Copied: {source_path} -> {target_path}")

# 사용 예제
source_folder = "/test1"
target_folder = "/test2"
copy_json_files(source_folder, target_folder)
