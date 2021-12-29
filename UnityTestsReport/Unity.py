import os
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from bs4 import BeautifulSoup


class Test:

    def __init__(self):
        self._project_path = ''
        self._xml_path = ''
        self._unity_path = ''
        self._platform = ''
        self._google_sheet_name = ''
        self._google_key_file = ''
        print(gspread.__file__)

    @property
    def project_path(self):
        return self._project_path

    @project_path.setter
    def project_path(self, project_path):
        self._project_path = project_path

    @property
    def xml_path(self):
        return self._xml_path

    @xml_path.setter
    def xml_path(self, xml_path):
        self._xml_path = xml_path

    @property
    def unity_path(self):
        return self._unity_path

    @unity_path.setter
    def unity_path(self, unity_path):
        self._unity_path = unity_path

    @property
    def platform(self):
        return self._platform

    @platform.setter
    def platform(self, platform):
        self._platform = platform

    @property
    def google_sheet_name(self):
        return self._google_sheet_name

    @google_sheet_name.setter
    def google_sheet_name(self, google_sheet_name):
        self._google_sheet_name = google_sheet_name

    @property
    def google_key_file(self):
        return self._google_sheet_name

    @google_key_file.setter
    def google_key_file(self, google_key_file):
        self._google_key_file = google_key_file

    # Run unity test via command line
    def run(self):
        print('running unity test...')
        project_path = "-projectPath {0}".format(self._project_path)
        test_result = "-testResults {0}".format(self._xml_path)
        test_platform = "-testPlatform {0}".format(self._platform)
        cmd = "Unity.exe -runTests {0} {1} {2}".format(project_path, test_result, test_platform)
        os.chdir(self._unity_path)
        os.system(cmd)

    # Get all test case results
    def get_results(self):
        test_result = []

        # Reading the xml result data
        with open(self._xml_path, 'r') as f:
            data = f.read()

        # Parse the xml result data using BeautifulSoup
        result_data = BeautifulSoup(data, "xml")

        # Get Time stamp header
        timestamp = result_data.find('test-run').get('start-time')
        timestamp = timestamp.split()
        test_result.append({'start-time': "Date: {0}\nTime: {1}".format(timestamp[0], timestamp[1])})

        # Finding all instances of test case
        test_cases = result_data.find_all('test-case')

        # Get Result
        for test_case in test_cases:
            test_result.append({'name': test_case.get('name'), 'result': test_case.get('result')})

        return test_result

    def update_google_sheet(self, test_data):
        print('updating google sheet...')
        scopes = [
            'https://www.googleapis.com/auth/drive',
            'https://www.googleapis.com/auth/drive.file',
            'https://www.googleapis.com/auth/drive.readonly',
            'https://www.googleapis.com/auth/spreadsheets',
            'https://www.googleapis.com/auth/spreadsheets.readonly',
        ]

        credential = ServiceAccountCredentials.from_json_keyfile_name(self._google_key_file, scopes)
        client = gspread.authorize(credential)
        test_report = client.open(self._google_sheet_name).sheet1
        test_report.delete_columns(1, 1)
        test_column = []
        result_column = []

        # Update the test result
        test_column.append('Test Case')
        result_column.append(test_data[0]['start-time'])
        for index, test in enumerate(test_data):
            if index == 0:
                continue
            test_column.append(test['name'])
            result_column.append(test['result'])

        test_report.insert_cols([test_column, result_column], 1)
