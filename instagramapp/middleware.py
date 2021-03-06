
from django.shortcuts import redirect
from django.urls import reverse

class ProfileCompletionMiddleware:
    """Profile completion 
    
    Ensure every user that is interacting with the platform have their 
    profile picture and biography 
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        if not request.user.is_anonymous:
            profile = request.user.profile
            if not profile.picture or not profile.biography:
                if not request.path == reverse('users:update_profile'):
                    return redirect('users:update_profile')

        response = self.get_response(request)
        return response