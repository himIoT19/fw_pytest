import os
import shutil
import argparse


def generate_allure_report_and_archive(result_dir):
    """ Execute the allure generate command """
    report_dir = 'allure-report'
    if not os.path.exists(result_dir):
        input(f'The given allure results directory [{result_dir}] does not exist. Enter to exit')
        exit(1)
    allure_cmd = f'allure generate {result_dir} -o {report_dir} --clean'
    return_code = os.system(allure_cmd)
    if return_code != 0:
        input("There was a problem while running allure generate command. Enter to exit")
        exit(return_code)

    # Copy the open_report.py file into allure report folder
    source_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'open_report.py')
    destination_file = os.path.join(report_dir, 'open_report.py')
    shutil.copy(source_file, destination_file)

    # Zip the allure report folder
    zip_file_name = 'allure-report'
    shutil.make_archive(zip_file_name, 'zip', root_dir=report_dir)
    # Remove generated allure report after zip it
    shutil.rmtree(report_dir, ignore_errors=True)
    # Remove old zip file if exists
    desktop_path = os.path.join(os.path.expanduser('~'), 'Desktop')
    old_zip_file = os.path.join(desktop_path, f'{zip_file_name}.zip')
    if os.path.exists(old_zip_file):
        os.unlink(old_zip_file)
    # Move the allure report zip file to user Desktop location
    shutil.move(f'{report_dir}.zip', desktop_path)
    print(f'Report zip file successfully generated to {os.path.join(desktop_path, zip_file_name)}.zip')


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-r', '--resultsdir', help='Path of the allure results')
    args = parser.parse_args()
    generate_allure_report_and_archive(args.resultsdir)


if __name__ == '__main__':
    main()

    # Usage1:
    #   python generate_allure_report.py --resultsdir C:\\Users\\username\\allure-results
    # Usage2:
    #   python generate_allure_report.py --resultsdir C:\\Users\\username\\allure-results  --reportdir allure-report
