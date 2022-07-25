import os

if __name__ == '__main__':
    print("Please select a computer:")
    temp = input()
    if len(temp) < 2:
        temp = "0" + temp
    path = os.path.relpath("\\(class name)-" + temp + "\D:")
    os.startfile(path)
