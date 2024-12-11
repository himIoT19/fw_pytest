import os
import sys
import time

import pytest


def get_report_path():
    return os.path.join(os.getcwd(), r'report/Report_' + time.strftime('%d%b%Y_%H%M%S'))


def get_allure_dir_path(args: list) -> str:
    """
    This method is used to get or generate allure report path, if path is not mentioned in the cmd line args
    :param args: list of cmd line arguments
    :return: str obj - path of allure report
    """
    return args[args.index('--alluredir') + 1] if '--alluredir' in args else get_report_path()


def trigger_functional_tests():
    """
    This method is supposed to trigger functional tests for given config file (like, api/ui)
    :return:
    """
    cla = f'--alluredir,{report_dir}'
    pytest.main(cla.split(','))


if __name__ == "__main__":
    cmd_line_args = sys.argv[1:]
    report_dir = get_allure_dir_path(cmd_line_args)

    trigger_functional_tests()
