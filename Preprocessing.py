
'''
write_txt takes a cooridinates dict as input and saves the keys and values in the following form
Frame_no, (array([class_no, ...], dtype=float32), array([[xyxy], ...], dtype=float32))
to a .txt file
'''


def write_txt(dict):
    file = open(r'D:\LSTM\boxes.txt', 'w')
    for x in dict:
        file.write('\n{x},{tensor}'.format(x=x, tensor=dict.get(x)))
    print('boxes.txt completed.')
    file.close()


'''
format_boxes removes the whitespace from boxes.txt such that all
numpy arrays fit on a single line and each line starts with Frame_no
'''


def format_boxes(path):
    file1 = open(path, 'r')
    new_file = open(r'D:\LSTM\boxes_formatted.txt', 'w')
    for x in file1:
        if x[0] == " ":
            new_file.write(x.strip())
            continue
        else:
            new_file.write('\n{line}'.format(line=x.strip()))
        new_file.close()
        file1.close()


