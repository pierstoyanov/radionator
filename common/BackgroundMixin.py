from radionator.profiles.models import Profile


class BackgroundMixin(object):
    """If user is logged in, this mixin returns
    the value of Profile.background as context variable
    in order to change the template bg"""

    def get_context_data(self, request, *args, **kwargs):
        if request.user.is_authenticated():
            context = super(BackgroundMixin, self).get_context_data(request, *args, **kwargs)
            profile = Profile.objects.get(user=request.user)
            context['background'] = profile.background

            return context
