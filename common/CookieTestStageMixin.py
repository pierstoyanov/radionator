class CookeTestStageMixin():
    """Set a test cookie on loading the view."""
    def setup_cookie(self, request, *args, **kwargs):
        self.request.session.set_test_cookie()

        super().__init__(*args, **kwargs)


