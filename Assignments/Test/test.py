import os


def writeData():
    data = "Hello world!"
    with open("test.txt", "a") as f:
        f.write(data)
        f.close()


def openFile():
    with open("test.txt", "r") as f:
        data = f.read()
        print(data)
        f.close()



if __name__ == "__main__":
    writeData()
    openFile()
