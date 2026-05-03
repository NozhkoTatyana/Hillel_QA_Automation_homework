from pathlib import Path
import csv

"""
Візміть два файли з теки ideas_for_test/work_with_csv порівняйте на наявність дублікатів і приберіть їх.
Результат запишіть у файл result_<your_second_name>.csv
"""

base = Path(__file__).parent.parent

files = [
    base / "ideas_for_test" / "work_with_csv" / "r-m-c.csv",
    base / "ideas_for_test" / "work_with_csv" / "rmc.csv"
]

result_file = Path(__file__).parent / "result" / "result_nozhko.csv"
result_file.parent.mkdir(exist_ok=True)


seen = set()
unique_rows = []
headers = None

delimiters = {
    "rmc.csv": ";",
    "r-m-c.csv": ","
}

for f in files:
    delimiter = delimiters.get(f.name, ",")
    with open(f, newline='', encoding='utf-8') as csvfile:
        reader = csv.reader(csvfile, delimiter=delimiter)
        file_headers = next(reader)

        if headers is None:
            headers = file_headers
            unique_rows.append(headers)

        for row in reader:
            row_tuple = tuple(row)
            if row_tuple not in seen:
                seen.add(row_tuple)
                unique_rows.append(row_tuple)


with open(result_file, "w", newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(unique_rows)

print(f"✅ Файл без дублікатів збережено у {result_file}")