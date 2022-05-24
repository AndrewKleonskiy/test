def parse_file(path: str):

    Output = []
    with open(path, "r") as f:

        document = {}
        key = None

        for line in f.readlines():

            if line.strip().startswith("#"):
                continue

            if not line.strip():
                if not document:
                    continue
                document[key] = "\n".join(document[key])

                Output.append(document)
                document = {}
                key = None
                continue

            if line.startswith(" "):
                document[key].append(line.strip())
            else:
                new_key, data = line.split(':')
                if new_key not in document:
                    document[new_key] = []
                document[new_key].append(data.strip())
                if key and key != new_key:
                    document[key] = "\n".join(document[key])
                key = new_key

        Output.append(document)
    return Output


def load_data(path: str):
    parsed_data = parse_file(path)

    for document in parsed_data:
        print(document, '\n')


load_data('example.txt')
