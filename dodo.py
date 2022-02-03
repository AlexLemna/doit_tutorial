def task_hello_world():
    return {'actions': ['echo "hello world!" > hello.txt'],
            'targets': ['hello.txt']}
