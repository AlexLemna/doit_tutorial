from doit.tools import run_once


def task_hello_world():
    return {"actions": ['echo "hello world!" > hello.txt'], "targets": ["hello.txt"]}


def task_download_data():
    return {
        "actions": [
            "curl -OL https://s3.amazonaws.com/pydoit-intermediate/Melee_data.csv.gz"
        ],
        "targets": ["Melee_data.csv.gz"],
        "uptodate": [run_once],
    }


def task_gunzip_data():
    return {
        "actions": ["gunzip -c %(dependencies)s > %(targets)s"],
        "targets": ["Melee_data.csv"],
        "file_dep": ["Melee_data.csv.gz"],
    }
