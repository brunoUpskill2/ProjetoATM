from django.shortcuts import redirect
import functools
from django.contrib.auth import get_user_model 
from django.conf import settings

User = get_user_model()
    
def password_require(func):
    """
    If a user wants to log in with a password, they must already have a password.
    """
    @functools.wraps(func)
    def wrapper(request, *args, **kwargs):
        phone_number = request.session.get('User')
        try:
            user = User.objects.get(phone=phone_number)
        except User.DoesNotExist:
            return redirect('User:login')
        else:
            if user.password:
                return func(request, *args, **kwargs)
            else:
                return redirect('User:login')
    return wrapper


def phone_number_require(redirect_to, session_name):
    """
    This decorator checks if there is a phone number in the session or not.
    Note that the phone numbers entered by the user are saved in the sessions.
    """
    def method_wrapper(func):
        def arguments_wrapper(request, *args, **kwargs):
            phone_number = request.session.get(session_name)
            if phone_number:
                return func(request, *args, **kwargs)
            return redirect('User:%s' % redirect_to)
        return arguments_wrapper
    return method_wrapper


def anonymous_required(func):
    """
    If the users want to login, they should be anonymous users.
    """
    @functools.wraps(func)
    def as_view(request, *args, **kwargs):
        redirect_to = kwargs.get('next', settings.LOGIN_REDIRECT_URL)
        if request.user.is_authenticated:
            return redirect(redirect_to)
        response = func(request, *args, **kwargs)
        return response
    return as_view
