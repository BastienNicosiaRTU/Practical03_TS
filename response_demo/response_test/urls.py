from django.urls import path
from . import views

urlpatterns = [
    path('simple/', views.simple_response, name='simple_response'),
    path('redirect/', views.redirect_response, name='redirect_response'),
    path('json/', views.json_response, name='json_response'),
    path('file/', views.file_response, name='file_response'),
    path('streaming/', views.streaming_response, name='streaming_response'),
    path('notfound/', views.not_found_response, name='not_found_response'),
    path('badrequest/', views.bad_request_response, name='bad_request_response'),
    path('forbidden/', views.forbidden_response, name='forbidden_response'),
    path('notallowed/', views.method_not_allowed_response, name='method_not_allowed_response'),
    path('servererror/', views.server_error_response, name='server_error_response'),
    
]
