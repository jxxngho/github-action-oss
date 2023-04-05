import os

num = os.environ.get("INPUT_NUM")
if num:
    try:
        num = int(num)
    except Exception:
        exit("Error")
else:
    num = 1

print(f"::set-output name=num_squared:: {num **2}")
