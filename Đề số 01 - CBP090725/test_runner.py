import subprocess
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

from test_de1 import tests

def normalize(s):
    return s.lower().replace(" ", "").replace(":", "").replace("=", "").strip()

def run_code(file, input_data):
    try:
        result = subprocess.run(
            ["python", file],
            input=input_data.encode('utf-8'),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            timeout=3
        )
        output = result.stdout.decode('utf-8').strip().splitlines()
        return [line.strip() for line in output if line.strip()]
    except subprocess.TimeoutExpired:
        return ["loiquathoigian"]

def test_normal_output(output, expected):
    expected_norm = normalize(str(expected))
    return any(expected_norm in normalize(out) for out in output)

def grade(base_dir="submissions_de1"):
    total = 0
    passed = 0
    for bai, testcases in tests.items():
        file_path = os.path.join(base_dir, f"{bai}.py")
        if not os.path.exists(file_path):
            print(f"MISS {bai}")
            continue

        case_list = testcases if isinstance(testcases, list) else [testcases]
        all_ok = True
        for idx, test in enumerate(case_list, 1):
            output = run_code(file_path, test["input"])
            this_ok = False
            for expected in test["expected"]:
                if test_normal_output(output, expected):
                    this_ok = True
                    break
            if not this_ok:
                all_ok = False
                print(f"FAIL {bai} test {idx}: got {output}, expected {test['expected']}")
        
        if all_ok:
            print(f"PASS {bai}")
            passed += 1
        total += 1
    
    print(f"\nResult: {passed}/{total} passed")

if __name__ == "__main__":
    grade()
