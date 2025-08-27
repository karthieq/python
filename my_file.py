with open('my_file', 'r') as rf:
    with open('my_file2', 'w') as wf:
        for line in rf:
            wf.write(line)
