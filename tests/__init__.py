from mocktest import mock, MockTransaction

class MockMixin(object):
    def setUp(self):
        MockTransaction.__enter__()
        super(MockMixin, self).setUp()

    def tearDown(self):
        super(MockMixin, self).tearDown()
        MockTransaction.__exit__()

    def validate_mocks(self):
        """
        Forces a validation of mocks immediately instead of at the end of the test
        """
        MockTransaction.__exit__()
        MockTransaction.__enter__()
