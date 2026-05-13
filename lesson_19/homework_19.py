"""
відберіть лише строки з вказаним ключем Key TSTFEED0300|7E3E|0400
Створіть функцію, що поверне лог-файл, де буде аналіз правильності вимог:
1. для кожного випадку де heartbeat більше 31 сек але менше 33 логувало WARNING в файл hb_test.log
2. для кожного випадку де heartbeat більше рівно 33 логувало ERROR в файл hb_test.log
3. Зверніть увагу, що нам для аналізу помилок було б добре знати час, в який помилка відбулася.
"""

from datetime import datetime
import logging

logging.basicConfig(
    filename="hb_test.log",
    level=logging.WARNING,
    format="%(levelname)s %(message)s"
)
logger = logging.getLogger(__name__)

def extract_heartbeats(filepath: str, key: str):
    heartbeats_list = []
    with open(filepath, 'r', encoding='utf-8') as file:
        for line in file:
            if key in line:
                start = line.find("Timestamp") + len("Timestamp")
                end = line.find("Key")
                timestamp = (line[start:end]).strip()
                time_obj = datetime.strptime(timestamp, "%H:%M:%S")
                heartbeats_list.append(time_obj)
    return heartbeats_list

def analyze_heartbeats(heartbeats_list):
    heartbeats_list.sort()

    for i in range(len(heartbeats_list)-1):
        current_time = heartbeats_list[i]
        next_time = heartbeats_list[i + 1]
        diff = abs((current_time - next_time).total_seconds())

        msg = (
            f"{key} heartbeat delay {diff} sec "
            f"(from {current_time:%H:%M:%S} "
            f"to {next_time:%H:%M:%S})"
        )

        if 31 < diff < 33:
            logger.warning(msg)
        elif diff >= 33:
            logger.error(msg)

if __name__ == "__main__":
    key = "TSTFEED0300|7E3E|0400"
    filepath = "hblog.txt"
    heartbeats = extract_heartbeats(filepath, key)
    analyze_heartbeats(heartbeats)


