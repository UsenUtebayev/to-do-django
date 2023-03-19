

def add_username_to_context(request):
    username = None
    if request.user.is_authenticated:
        username = request.user.username

    return {'username': username}
