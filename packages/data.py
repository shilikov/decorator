from packages.logger import log_to_file, log_to_console
import csv

LOG_PATH = 'log.txt'

@log_to_file(LOG_PATH)
@log_to_console
def get_raw(raw_data_path):
    with open(raw_data_path, encoding='utf-8') as file:
        rows = csv.reader(file, delimiter=",")
        result = list(rows)
    return result


@log_to_file(LOG_PATH)
@log_to_console
def save_true(data, pure_data_path):
    with open(pure_data_path, "w", encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerows(data)
    return 'csv файл отформатирован и записан'




