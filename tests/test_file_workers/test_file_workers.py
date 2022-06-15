import pytest

from my_funcs.file_workers import read_from_file


def create_test_data(test_data):
    with open("tests/test_file.txt", "a") as file:
        file.writelines(test_data)


def test_read_from_file():
    test_data = ['one\n', 'two\n', 'three']
    create_test_data(test_data)
    assert test_data == read_from_file("tests/test_file.txt")
