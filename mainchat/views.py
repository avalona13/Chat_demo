from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Message
from .forms import ContentForm


@login_required(login_url='/')
def chat_detail(request):
    visitor = request.user
    try:
        Message.objects.filter(was_read=False,).exclude(author=visitor).update(was_read=True)
    except Message.DoesNotExist:
        contents = None
    finally:
        contents = Message.objects.all()
    form = ContentForm(request.POST or None)
    return render(request, 'mainchat/chat.html', {'form': form, 'contents': contents})
