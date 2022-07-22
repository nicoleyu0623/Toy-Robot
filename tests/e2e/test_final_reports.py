# @Time : 22/7/22 7:57 pm
# @Original Author : Nicole Yu
# @File : test_final_reports.py
# @Project: AUTOMATION

import sys


def test_myoutput(capsys):  # or use "capfd" for fd-level
    print("hello")
    sys.stderr.write("world\n")
    captured = capsys.readouterr()
    assert captured.out == "hello\n"
    assert captured.err == "world\n"
    print("next")
    captured = capsys.readouterr()
    assert captured.out == "next\n"
