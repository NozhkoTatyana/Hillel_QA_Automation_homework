from pathlib import Path
import json
import logging

"""
Провалідуйте, чи усі файли у папці ideas_for_test/work_with_json є валідними json.
результат для невалідного
файлу виведіть через логер на рівні еррор у файл json__<your_second_name>.log
"""

result_dir = Path(__file__).parent / "result"
result_dir.mkdir(exist_ok=True)

log_file = result_dir / "json_nozhko.log"

logging.basicConfig(
    filename=log_file,
    filemode="a",
    level=logging.ERROR,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

json_dir = Path(__file__).parent.parent / "ideas_for_test" / "work_with_json"
json_files = list(json_dir.glob("*.json"))

print("Перевірка JSON файлів:\n")
for json_file in json_files:
    try:
        with open(json_file, "r", encoding="utf-8") as j_file:
            data = json.load(j_file)
            status = "✅ OK"
            dtype = type(data).__name__
            print(f"{json_file.name:<25} {status:<10} type: {dtype}")
    except json.JSONDecodeError as e:
        status = "❌ invalid"
        dtype = "json.JSONDecodeError"
        logging.error(f"{json_file.name} - JSONDecodeError: {e}")
        print(f"{json_file.name:<25} {status:<10} type: {dtype}")
