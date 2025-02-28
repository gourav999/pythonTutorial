class TestAutomation:
    def __init__(self, tool):
        self.tool = tool

    def run_test(self):
        return f"Running tests using {self.tool}"

test = TestAutomation("Selenium")
print(test.run_test())
