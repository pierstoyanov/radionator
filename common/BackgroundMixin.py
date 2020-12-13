from radionator.profiles.models import Profile


class BackgroundMixin(object):
    """If user is logged in, this mixin returns
    the value of Profile.background as context variable
    in order to change the template bg"""

    def get_context_data(self, *args, **kwargs):
        context = super(BackgroundMixin, self).get_context_data(*args, **kwargs)
        if self.request.user.is_authenticated:
            profile = Profile.objects.get(user=self.request.user)
            context['background'] = profile.background
            return context
