from pathlib import Path
from hexlet_pytest.example import reverse

def test_reverse():
    assert reverse('Hexlet') == 'telxeH'


def test_reverse_for_empty_string():
    assert reverse('') == ''



def get_test_data_path(filename):
    return Path(__file__).parent / 'test_data' / filename

def read_file(filename):
    return get_test_data_path(filename).read_text()

def test_reverse_long():
    before_html = read_file('reverse.txt')
    expected = read_file('result_reverse.txt')
    actual = reverse(before_html)

    assert actual == expected