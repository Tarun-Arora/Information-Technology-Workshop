def func_10(path_1, path_2):
    for line_1, line_2 in zip(open(path_1), open(path_2)):
        print(line_1.strip())
        print(line_2.strip())
func_10("file_1.txt", "file_2.txt")