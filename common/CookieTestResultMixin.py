def test_cooke(request):
    """
    Return the result of the last staged test cookie.
    returns cookie_state = bool
    """

    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        cookie_state = True
    else:
        cookie_state = False

    return cookie_state


class CookeTestResultMixin():
    """From a CBV, get the result of the last test cookie and
    set bool session variable cookie_state"""
    def setup_cookie(self, request, *args, **kwargs):
        super().__init__(*args, **kwargs)

        cookie_state = test_cooke(self.request)
        self.request['cookie_state'] = cookie_state


# TODO Make this mixin work