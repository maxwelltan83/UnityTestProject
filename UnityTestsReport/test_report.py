import Unity

# Run Unity Test Project and update google sheet

unity_test = Unity.Test()

# Configure setting
unity_test.unity_path = 'C:\\UnityProject\\2022.1.0b2\\Editor'
unity_test.project_path = 'C:\\UnityTestProject\\Test-2D-Projects'
unity_test.xml_path = "{0}\\Assets\\Tests\\EditMode\\TestResults\\results.xml".format(unity_test.project_path)
unity_test.platform = 'editmode'
unity_test.google_sheet_name = 'Unity 2D Tests Report'
unity_test.google_key_file = 'C:\\UnityTestProject\\UnityTestsReport\\config\\service_token.json'

# Execute Test and update
unity_test.run()
test_result = unity_test.get_results()
unity_test.update_google_sheet(test_result)
