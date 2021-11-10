from django.core.exceptions import PermissionDenied
from .models import Profile

def user_is_entry_author(function):
    def wrap(request, *args, **kwargs):
        profile = Profile.objects.filter(user=request.user).first()
        if not profile:
            return function(request, *args, **kwargs)
        else:
            raise PermissionDenied
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap