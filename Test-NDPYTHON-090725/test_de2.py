tests = {
    # Câu 1a: Nhập 2 số thực, in tổng và hiệu
    "Cau1a": [
        {"input": "", "expected": ["['apple', 'banana']"]}
    ],

    # Câu 1b: 
    "Cau1b": [
        {"input": "", "expected": ["11"]}  # "apple" (5) + "banana" (6) = 11
    ],

    # Câu 2a: 
    "Cau2a": [
        {"input": "123456\n", "expected": ["246"]},    # vị trí 2,4,6
        {"input": "98765\n", "expected": ["86"]}       # vị trí 2,4
    ],

    # Câu 2b: 
    "Cau2b":[
        {"input": "12321\n", "expected": ["True"]},
        {"input": "123456\n", "expected": ["False"]}
    ],
    # Câu 3:
    "Cau3a":[
        {"input": "", "expected": ["(12, 18, 21, 9)"]}
    ], 
    "Cau3b":  [
        {"input": "", "expected": ["2"]}  # 5, 7, 19 là số nguyên tố
    ]
}
