class CookieTestStageMixin:
    """Set a test cookie on loading the view."""
    # def setup_cookie(self, request, *args, **kwargs):

    def dispatch(self, request, *args, **kwargs):
        request.session.set_test_cookie()
        return super(CookieTestStageMixin, self).dispatch(request, *args, **kwargs)
