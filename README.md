# Unity Test Project

## In the repo contain is 2 project floder and 1 manual test report:
  1. Test-2D-Projects:
     - This is a Unity project which include the test case and test scene.
  
  2. UnityTestsReport:
     - This is written in python language, it will run the Unity test case and update the google sheet.
  
  3. 2D Test Report.docx:
     - This is a 2D manual test report consist of 10 test case.

## Unity Test Result via Google Sheet:
  1. Here is the link to "Unity 2D Test Report"
     - https://docs.google.com/spreadsheets/d/1-BUq582bLhM91lx8Q0AtdqHWLlYLH-w8P2ZF8KSzK0w/edit?usp=sharing

## Before Installation:
  1. I recommend to clone this repo to your C: drive root

## Installation for Test-2D-Projects:
  1. Install Unity 2022.1.0b2 (Beta)
  2. Open the Test-2D-Project folder with Unity 2022.1.0b2 (Beta)

## Installation for UnityTestsReport:
  1. Install Python 3.9:
     - Download "Windows x86-64 executable installer" from here:
       - https://www.python.org/downloads/release/python-390/
  
  2. Install PyCharm Community Version:
     - https://www.jetbrains.com/pycharm/download/#section=windows

  3. Open the UnityTestsReport folder with PyCharm
  4. In the PyCharm application select the bottom tap name "terminal"
     - Alternative from top select View -> Tool Windows -> Terminal
  
  5. In PyCharm in the terminal enter the following command to install the package:
     - pip install -r requirements.txt

  6. To run the Unity and update google sheet:
     1. In PyCharm on the left panel project directory right-click on "test_report.py"
     2. Select "Run 'test_report' option
