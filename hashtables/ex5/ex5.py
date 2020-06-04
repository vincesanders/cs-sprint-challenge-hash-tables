# Your code here
def finder(files, queries):
    """
    YOUR CODE HERE
    """
    # Your code here
    result = []
    # iterate over each path
    # file is key, rest of path is value
    paths = {}
    for path in files:
        # iterate backward through path
        index = len(path) - 1
        char = path[index]
        key = ''
        # add file names to paths
        while char != '/':
            key = char + key
            index -= 1
            char = path[index]
        index = index + 1
        if key in paths:
            paths[key].append(path[:index])
        else:
            paths[key] = [path[:index]]
    for q in queries:
        if q in paths:
            for i in range(len(paths[q])):
                result.append(f'{paths[q][i]}{q}')
    return result


if __name__ == "__main__":
    files = [
        '/bin/foo',
        '/bin/bar',
        '/usr/bin/baz'
    ]
    queries = [
        "foo",
        "qux",
        "baz"
    ]
    print(finder(files, queries))
