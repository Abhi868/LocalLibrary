
# #Session model stores the session data
# from django.contrib.sessions.models import Session
# from django.contrib.auth.models import User
# from django.http import HttpResponse
# from catalog.models import LoggedInUser
# class OneSessionPerUserMiddleware:

#     def __init__(self, get_response):
#         self.get_response = get_response

#     def __call__(self, request):
#         print("inside call method")
       
#         # if request.user.is_authenticated:
#         #     print("Middleware executed")
#         #     print(request.user.last_login)
#         #     # current_session_key = request.LoggedInUser.session.session_key
#         #     user_id=request.user.id

#         #     # if there is a stored_session_key  in our database and it is
#             # different from the current sessipythonon, delete the stored_session_key
#             # session_key with from the Session table
#             # if current_session_key and current_session_key != request.session.session_key:
#             #     Session.objects.get(session_key=current_session_key).delete()

#             # request.user.logged_in_user.session_key = request.session.session_key
#             # request.user.logged_in_user.save()

#         # response = self.get_response(request)
#         # return HttpResponse(request.user.last_name)
#         return None