from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from .models import *
from django.template import loader
from django.urls import reverse
# import telebot
# from django.core.exceptions import PermissionDenied
# from django.views.decorators.csrf import csrf_exempt
# from datetime import datetime




# TOKEN = '6949284535:AAHNR3sl6uJM8MrtDydf6AyiQhecbRQMQyc'
# tbot = telebot.AsyncTeleBot(TOKEN)


# @csrf_exempt
# def bot(request):
#     if request.META['CONTENT_TYPE'] == 'application/json':

#         json_data = request.body.decode('utf-8')
#         update = telebot.types.Update.de_json(json_data)
#         tbot.process_new_updates([update])

#         return HttpResponse("")

#     else:
#         raise PermissionDenied
    
# @tbot.message_handler(commands=['start'])
# def greet(m):
#     tbot.send_message(m.chat.id, "Hello")

def login(request):
    mydata = User_auth.objects.all()
    temp_store = []
    for _ in mydata:
        temp_store.append(_.userName + _.password)
    if request.method == 'POST':
        name = request.POST.get('user_name')
        passs = request.POST.get('user_password')
        
        
        
        if name+passs in temp_store:
            request.session['name'] = name
            if request.session.modified:
                # Valid credentials, perform login action (e.g., set session, redirect to dashboard)
                request.session['name'] = name
                return redirect('member')
            
            return  member(request)
        else:
  
            error_message = 'Invalid username or password.'
            return render(request, 'login.html', {'error_message': error_message})  

            


    return render(request, "login.html")

def logout(request):
    request.session.flush()
    return redirect('login')

def deleteMember(request,id):
    memberList = Member.objects.get(id=id)
    memberList.delete()
    return redirect('member')



def deleteEvent(request,id):
    memberList = Event.objects.get(id=id)
    memberList.delete()
    return redirect('event')


def updateMember(request,id):
    memberListU = Member.objects.get(id=id)
    template = loader.get_template('edituser.html')
    context = {
    'memberListU': memberListU,
     }
    return HttpResponse(template.render(context, request))





def updateMemberRecord(request, id):
  
  userName = request.POST.get('userName')
  userId = request.POST.get('userId')
  depart = request.POST.get('depart')
  Year = request.POST.get('year')
  user_sex = request.POST.get('user_sex')
  user_skill = request.POST.get('skill')
  member = Member.objects.get(id=id)
  member.fisrtname = userName

  member.save()
  return HttpResponseRedirect(reverse('member'))


# def editUser(request):
#     name = request.session.get('name')
#     if name:
#         return render(request, "editUser.html")
#     else:
#         return redirect('login')



def base(request):
    return render(request, "base.html")











def member(request):
    memberList = Member.objects.all() 
    name = request.session.get('name')
    if name:
        if request.method == 'POST':
            userName = request.POST.get('userName')
            userId = request.POST.get('userId')
            depart = request.POST.get('depart')
            Year = request.POST.get('year')
            user_sex = request.POST.get('user_sex')
            user_skill = request.POST.get('skill')
            


            addUser = Member(fisrtname=userName, ugr=userId,sex=user_sex, department = depart , year=Year,skill = user_skill)
            addUser.save()

             
            return redirect('member')

        return render(request, "member.html" ,{'memberList': memberList})
    else:
        return redirect('login') 
    










def feedback(request):
    name = request.session.get('name')
    if name:
        return render(request, "feedback.html")
    else:
        return redirect('login')

def event(request):
    eventList = Event.objects.all() 
    
    name = request.session.get('name')
    if name:
        if request.method == 'POST':
            eventName = request.POST.get('eventName')
            location = request.POST.get('location')
            hour = request.POST.get('hour')
            date = request.POST.get('date')
          

            print(eventName,location,hour,date)
            addEvent= Event(eventName=eventName, location=location,hour=hour, date = date )
            addEvent.save()

        return render(request, "event.html" ,{'eventList': eventList})

    else:
        return redirect('login')



def dashboard(request):
    name = request.session.get('name')
    if name:
        return render(request, "dashboard.html")
    else:
        return redirect('login')


def settings(request):
    name = request.session.get('name')
    if name:
        return render(request, "settings.html")
    else:
        return redirect('login')
    




# @bot.message_handler(commands=['start'])
# def handle_start(message):
#     bot.reply_to(message, """Hello 👋 \nWelcome to the CSEC Dev bot. \n CSEC Development Division Official Channel @csec_devs Join \n \n \n \n ⚡️ For feedback click  /feedback """)
    
    



# @bot.message_handler(commands=['feedback'])
# def handle_feedback(message):
#     bot.reply_to(message, """Write Your feedback here ? """ )
#     bot.register_next_step_handler(message, handle_feedback_Q)





# def handle_feedback_Q(message):
#     username_acc = message.from_user.username
#     feed_msg =  message.text
#     current_date = datetime.now().strftime("%Y-%m-%d")
#     print(username_acc,feed_msg,current_date)
#     return handle_close(message)
    
    


# def handle_close(message):
    
  
#     bot.reply_to(message, """Thanks for Your Comment """ )



