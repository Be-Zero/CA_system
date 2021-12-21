import os, config


def read_file(file_path):
    file_object = open(file_path, 'rb')
    text = file_object.read()
    file_object.close()
    return text


def save_file(default_path, text):
    file_object = open(default_path, 'wb')
    file_object.write(text)
    file_object.close()


def Delete(file_path):
    os.remove(file_path)