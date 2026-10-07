import subprocess
import os
import sys
import ast

# Đảm bảo đường dẫn luôn đúng dù chạy từ đâu
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)
os.chdir(BASE_DIR)

# Fix encoding cho Windows console
if sys.stdout.encoding != 'utf-8':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
    except Exception:
        pass

from test_de2 import tests

def normalize(s):
    return s.lower().replace(" ", "").replace(":", "").replace("=", "").strip()

def run_code(file, input_data):
    try:
        env = os.environ.copy()
        env["PYTHONIOENCODING"] = "utf-8"
        result = subprocess.run(
            [sys.executable, file],
            input=input_data.encode('utf-8'),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            env=env,
            timeout=3
        )
        output = result.stdout.decode('utf-8', errors='replace').strip().splitlines()
        return [line.strip() for line in output if line.strip()]
    except subprocess.TimeoutExpired:
        return ["loiquathoigian"]
    except Exception as e:
        return [f"loi_chay: {e}"]

def check_match(output, expected):
    # 1. Thử so sánh dạng đối tượng Python (set, dict, tuple, list) bằng ast.literal_eval
    parsed_expected = None
    if isinstance(expected, (dict, list, set, tuple)):
        parsed_expected = expected
    elif isinstance(expected, str):
        try:
            parsed_expected = ast.literal_eval(expected.strip())
        except:
            parsed_expected = None

    if parsed_expected is not None:
        for line in output:
            try:
                parsed_out = ast.literal_eval(line.strip())
                if type(parsed_out) == type(parsed_expected) and parsed_out == parsed_expected:
                    return True
            except:
                continue

    # 2. So sánh dạng chuỗi thông thường (sau khi normalize)
    expected_norm = normalize(str(expected))
    return any(expected_norm in normalize(out) for out in output)

def grade(student_id="unknown", base_dir=None):
    if base_dir is None:
        base_dir = os.path.join(BASE_DIR, "submissions_de2")
    elif not os.path.isabs(base_dir):
        base_dir = os.path.join(BASE_DIR, base_dir)

    total_score = 0
    max_score = 0
    print(f"📋 Bắt đầu chấm điểm cho {student_id}")
    print(f"📂 Thư mục bài làm: {base_dir}\n")

    for bai, testcases in tests.items():
        file_path = os.path.join(base_dir, f"{bai}.py")
        if not os.path.exists(file_path):
            print(f"❌ Không tìm thấy file: {file_path}")
            continue

        print(f"🔹 {bai.upper()}")
        case_list = testcases if isinstance(testcases, list) else [testcases]
        case_right = 0
        for idx, test in enumerate(case_list, 1):
            output = run_code(file_path, test["input"])
            this_ok = False

            expected_raw = test.get("expected", [])
            expected_candidates = expected_raw if isinstance(expected_raw, list) else [expected_raw]

            for expected in expected_candidates:
                if check_match(output, expected):
                    this_ok = True
                    break

            if this_ok:
                print(f"  ✅ Test {idx}: Input {repr(test['input'].strip())} → Đúng")
                case_right += 1
            else:
                print(f"  ❌ Test {idx}: Input {repr(test['input'].strip())} → Sai (Kết quả: {output})")
        bai_score = round(case_right / len(case_list), 2)  # tỉ lệ đúng của bài này
        total_score += bai_score
        max_score += 1
        print(f"    Kết quả: {case_right}/{len(case_list)} test đúng → {bai_score} điểm\n")

    # Quy đổi về thang điểm 10 nếu có bài
    scaled_score = round((total_score / max_score) * 10, 2) if max_score > 0 else 0

    print(f"""
    ╔══════════════════════════════════════════════╗
    ║ 🎯 Điểm số   : {scaled_score:>5.2f}/10 ({total_score}/{max_score} bài)             ║
    ║ 👤 Sinh viên : {student_id:<30}║
    ║ 📄 Mã đề     : Đề số 02 (Nâng cao)          ║
    ╚══════════════════════════════════════════════╝
    """)


if __name__ == "__main__":
    sv_id = sys.argv[1] if len(sys.argv) > 1 else "sv001"
    sub_path = sys.argv[2] if len(sys.argv) > 2 else os.path.join(BASE_DIR, "submissions_de2")
    grade(sv_id, sub_path)

