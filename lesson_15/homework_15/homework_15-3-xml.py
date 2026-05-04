import  xmltodict
import logging
from pathlib import Path


"""
Для файла ideas_for_test/work_with_xml/groups.xml створіть функцію пошуку по group/number і повернення
значення timingExbytes/incoming результат виведіть у консоль через логер на рівні інфо
"""


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def find_incoming_by_group_number(xml_path: Path, group_number: str):
    with open(xml_path, "r", encoding="utf-8") as f:
        data = xmltodict.parse(f.read())


    groups = data.get("groups").get("group")

    for group in groups:
        if group.get("number") == group_number:
            incoming = group.get("timingExbytes").get("incoming")
            if incoming:
                logging.info(f"group {group_number}: incoming = {incoming}")
                return incoming

    logging.info(f"group {group_number}: не знайдено")
    return None



xml_file = Path(__file__).parent.parent / "ideas_for_test" / "work_with_xml" / "groups.xml"
find_incoming_by_group_number(xml_file, "5")
