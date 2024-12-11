import allure


class AssertStatus:

    def __init__(self, title):
        #  maybe some set up is expected before assertion method call
        self.title = title

    def __enter__(self):
        #  maybe some set up is expected before assertion method call
        pass

    def __exit__(self, exc_type, exc_val, exc_tb):
        assertion_status = 'PASS' if exc_val is None else 'FAIL !!!'
        status_body = ''
        if isinstance(exc_val, (AssertionError, Exception)):
            status_body = str(exc_val)
        name = f"{self.title} >>> {assertion_status}"
        allure.attach(body=status_body, name=name, attachment_type=allure.attachment_type.TEXT)
