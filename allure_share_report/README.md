This utility can be used to generate a shareable allure report as a zip file with out requiring to install allure plugin
These reports are easily accessible by any 3rd party stakeholders, with just needing 'python' to be present on their machines
This tool generates a zip file with a 'open_report.py' utility which can help open the allure report on any PC/MAC

prerequisites:
You should have the allure results generated in a directory

Steps:
1. CD to current folder - 'allure-share-report'

2. Execute the command from your command line tool:
       python3 generate_allure_report.py -r <path/to/allure-results>

3. On success, You would see message:
       Report zip file successfully generated to <Desktop path>.zip

4. Unzip the folder from the above path
       Observe there should be 'open_report.py' inside the unzipped folder

5. Run 'open_report.py' by double clicking on it [or] right click and launch it through 'python_launcher'
       It launches allure report on your default browser