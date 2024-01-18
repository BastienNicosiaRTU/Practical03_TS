from django.shortcuts import render, redirect
from .models import Message
from django.utils import timezone

def submit_message(request):
    if request.method == 'POST':
        # Assuming you have 'sender', 'receiver', and 'content' fields in your form
        sender = request.POST.get('sender')
        receiver = request.POST.get('receiver')
        content = request.POST.get('content')
        
        # Create and save the new message
        new_message = Message(sender=sender, receiver=receiver, content=content)
        new_message.save()

        # Redirect to the get_messages view or another appropriate page
        return redirect('get_messages')
    else:
        # Render the submission form template
        return render(request, 'MsgApp/message_submission_form.html')


def get_messages(request):
    # Code to retrieve and display messages
    latest_messages = Message.objects.order_by('-created_at')[:10]
    return render(request, 'MsgApp/message_board.html', {'messages': latest_messages})
