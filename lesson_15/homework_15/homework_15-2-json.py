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


def validate_json_file(json_file: Path) -> tuple[bool, str]:
    try:
        with open(json_file, "r", encoding="utf-8") as j_file:
            data = json.load(j_file)
        return True, type(data).__name__
    except json.JSONDecodeError as e:
        logging.error(f"{json_file.name} - JSONDecodeError: {e}")
        return False, "json.JSONDecodeError"


if __name__ == "__main__":
    json_dir = Path(__file__).parent.parent / "ideas_for_test" / "work_with_json"
    json_files = list(json_dir.glob("*.json"))

    print("Перевірка JSON файлів:\n")

    for json_file in json_files:
        is_valid, dtype = validate_json_file(json_file)

        status = "✅ OK" if is_valid else "❌ invalid"
        print(f"{json_file.name:<25} {status:<10} type: {dtype}")