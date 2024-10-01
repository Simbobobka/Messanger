from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http.response import HttpResponse
from .forms import UserProfileForm
from .models import Chat, Message, User, UserProfile

    
def chatPage(request, chat_id=None):
    if request.user.is_anonymous:
        return render(request, 'home.html')
    user = request.user

    # Get all users excluding the current user
    users = User.objects.exclude(id=user.id)

    chats = user.chats.all()  # Assuming this returns the user's chats
    print(chats)
    selected_chat = None
    messages = None
    other_participant = None

    if chat_id:
        selected_chat = get_object_or_404(Chat, id=chat_id)
        id_chat = chat_id
        messages = selected_chat.message_set.all()

        # Exclude the current user from participants and get the other participant
        other_participant = selected_chat.participants.exclude(id=user.id).first()
    else:
        id_chat = 0
    context = {
        'users': users,  # List of users for the contact list
        'chats': chats,
        'selected_chat': id_chat,
        'messages': messages,
        'other_participant': other_participant,
    }
    return render(request, 'home.html', context)

@login_required
def startChat(request, user_id):
    user = request.user
    other_user = User.objects.get(id=user_id)

    # Check if a chat between these two users already exists
    chat = Chat.objects.filter(participants=user).filter(participants=other_user).first()

    if not chat:
        # Create a new chat if it doesn't exist
        chat = Chat.objects.create()
        chat.participants.add(user, other_user)

    # Redirect to the chat page with the new chat id
    return redirect('chat-detail', chat_id=chat.id)

@login_required
def profile(request):    

    user_profile, created = UserProfile.objects.get_or_create(user=request.user)
    if request.method == 'POST':
        form = UserProfileForm(request.POST, request.FILES, instance=user_profile)
        if form.is_valid():
            form.save()
    else:
        form = UserProfileForm(instance=user_profile)

    return render(request, 'profile.html', {'form':form})
    