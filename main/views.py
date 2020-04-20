from django.shortcuts import render
from main.models import Message
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.db.models import Q
from django.http.response import HttpResponseRedirect

def handler404(request, *args, **kwargs):
    return HttpResponseRedirect('login/')
    
@user_passes_test(lambda u: u.is_superuser)
def messagesStat(request):
    msgs=Message.objects.all()
    users = User.objects.all()
    userdict=[]
    for i in users:
        msg_sent=Message.objects.filter(sender=i)
        msg_recv=Message.objects.filter(recipient=i)
        userdict.append({'username':i.username,'msg_sent':msg_sent,'msg_recv':msg_recv,'sent_total':str(len(msg_sent)),'recv_total':str(len(msg_recv))})
    content ={'userdict':userdict}
    return render(request, 'stat.html', content)

@login_required(login_url='/login')
def userProfile(request):
    all_users = User.objects.values('username').exclude(username=request.user.username)
    content = {'users':all_users,'username':request.user.username}
    return render(request, 'userlist.html', content)

def chat(request):
    recipient_user = User.objects.get(username=request.POST['nickname'])
    msgs = Message.objects.filter((Q(sender=recipient_user) & Q(recipient=request.user)) | (Q(recipient=recipient_user) & Q(sender=request.user)))
    content = {'nickname':request.POST['nickname'],'msgs':msgs}
    return render(request, 'write_message.html', content)
    
def sendMessage(request):
    uid = User.objects.get(username=request.POST['nickname'])
    msg = Message(
        recipient=uid,
        sender=request.user,
        content=request.POST['content']
    )
    msg.save()
    return chat(request)
