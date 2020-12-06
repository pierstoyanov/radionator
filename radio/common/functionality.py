

def test_cooke(request):
    """
    Return the result of the last test cookie.
    returns cookie_state = bool
    """

    if request.session.test_cookie_worked():
        request.session.delete_test_cookie()
        cookie_state = True
    else:
        cookie_state = False

    return cookie_state
