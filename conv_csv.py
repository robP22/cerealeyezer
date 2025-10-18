import csv
import json
import os.path

from progress_bar import progress_b
from formatter import format_process_output, summary

def convert_files() -> None:
    """ Serialize a csv into a Json. """
    pt: str = './files/'  # Begin in project directory for MVP
    _files: list = os.listdir(pt)
    n: int = len(_files)
    obj_to_dump: list[dict] = []
    failures: list = []
    count: int = 1 # track the current file for naming

    print(f'\n|{format_process_output('[Process Starting]', '一')}|')
    progress_b(0, n)
    for _file in _files:
        # Iterate through each file in our list of files.
        file_path = os.path.join(pt, _file)

        progress_b(count, n)
        with open(file_path, encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            try:
                obj_to_dump = [row for row in reader]
            except UnicodeDecodeError as e:
                print(f'File {file_path} is still fucked:\n\t[{e}]')
                failures.append(file_path)

        # Write object to the json file
        with open(f'./j_dir/_{_file.replace('.csv', '')}', 'w', newline='') as jsnfile:
            json.dump(obj_to_dump, jsnfile)

        count += 1
        obj_to_dump.clear()

    print(f'\n|{format_process_output('[Process Complete]', '一')}|')

    fails: int = n - len(os.listdir('./j_dir/'))
    summary(n, fails)

convert_files()