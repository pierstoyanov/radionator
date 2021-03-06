def test_cookie(request):
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


class CookeTestResultMixin:
    """From a CBV, get the result of the last test cookie and
    set bool session variable cookie_state"""
    # def get_cookie_state(self, request, *args, **kwargs):
    #
    #     cookie_state = test_cooke(request)
    #     request.session['cookie_state'] = cookie_state
    #
    def get_context_data(self, *args, **kwargs):
        context = super(CookeTestResultMixin, self).get_context_data(*args, **kwargs)
        context['cookie_state'] = test_cookie(self.request)
        return context

    # def dispatch(self, request, *args, **kwargs):
    #     context = super(CookeTestResultMixin, self).get_context_data(*args, **kwargs)
    #     context['cookie_state'] = test_cookie(self.request)
    #     return super(CookeTestResultMixin, self).dispatch(request, *args, **kwargs)



# TODO Make this mixin work