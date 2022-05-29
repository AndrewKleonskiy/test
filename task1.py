import pandas as pd
import numpy as np
import hashlib


def hash_md5(string: str):
    return hashlib.md5(string.encode('utf-8')).hexdigest()


def isNaN(num):
    return num != num


def in1(path: str):
    Output = []
    data = pd.read_csv(path, sep=';')
    for x, y in data.iterrows():

        document = {'email_hash': '', 'domain': '', 'tags':[]}
        tags = ('password', 'name', 'phone', 'address')

        document['email_hash'] = hash_md5(y.login.strip())
        document['domain'] = y.login.split('@')[1]

        d1 = {k: y.to_dict()[k] for k in tags}
        for key, value in d1.items():
            if not isNaN(value):
                document['tags'].append(value)


        Output.append(document)

    save_out(Output, 'output_1.txt')


def in2(path: str):
    Output = []

    with open('input_2.txt', 'r') as f:
        file_lines = f.readlines()
        file_lines = [line.rstrip('\n') for line in file_lines]

    data = pd.DataFrame([string.split(';') for string in file_lines])
    for x, y in data.iterrows():
        document = {'email_hash': '', 'domain': '', 'tags': []}

        document['email_hash'] = hash_md5(y[0].strip())
        document['domain'] = y[0].split('@')[1]
        d1 = y.to_dict()

        for key, value in list(d1.items())[1:]:
            if not value is None:
                document['tags'].append(value)

        Output.append(document)

    save_out(Output, 'output_2.txt')


def save_out(input_file: list, output_filename):
    with open(output_filename, 'w') as file:
        for el in input_file:
            for key, value in el.items():
                file.write(f'{key} : {value}\n')
            file.write('\n')


in1('input_1.txt')
in2('input_2.txt')
