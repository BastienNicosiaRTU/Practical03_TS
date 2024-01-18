from django.urls import path
from .views import submit_message, get_messages
from django.views.generic import RedirectView

urlpatterns = [
    path('submit/', submit_message, name='submit_message'),
    path('get/', get_messages, name='get_messages'),
    path('', RedirectView.as_view(pattern_name='submit_message'), name='message_root'),
]

