from django.shortcuts import render
from voting.models import ContactUS, Candidate_votes, Election, Voted
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login,logout
from django.shortcuts import redirect

# Create your views here.
def home(request):
    # return HttpResponse("This is my Voting  Page")
    return render(request, 'index.html')

def index(request):
    # return HttpResponse("This is my Voting  Page")
    return render(request, 'index.html')

def voting(request):
    active_elections = Election.objects.filter(is_over=False)
    candidates_lists = []
    for election in active_elections:
        candidates = Candidate_votes.objects.filter(Election=election)
        candidates_lists.append({'election': election, 'candidates': candidates})

    # return HttpResponse("This is my Voting  Page")
    return render(request, 'voting.html', {'candidates_lists': candidates_lists})

def contact(request):
    if request.method=='POST':
        contact = ContactUS()
        name = request.POST.get('name')
        email = request.POST.get('email')
             
        message= request.POST.get('message')
        contact.name=name
        contact.email=email
          
        contact.message=message
        contact.save()
        return HttpResponse("Data Inserted Succesfully")

    # return HttpResponse("This is my Voting  Page")
    return render(request, 'contact.html')

def login_user(request):
    if request.method=='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            print("Sucessfully logged In")
            return redirect('voting')
    # return HttpResponse("This is my Voting  Page")
    return render(request, 'login.html')

def logout_user(request):
      logout(request)
      return render(request,'index.html')

def signup(request):
    if request.method=='POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        user=User()
        user.username= username 
        user.email=email 
        user.set_password(password)
        user.save()
        return redirect('login.html')
    # return HttpResponse("This is my Voting  Page")
    return render(request, 'signup.html')

def send_vote(request, candidatename):
    username = request.user.username
    if Voted.objects.filter(user = username).exists():
        print('yfyffgfhghg')
        return redirect('result.html')
    else:
        candidates = Candidate_votes.objects.get(name = candidatename)
        candidates.votes +=1
        candidates.save()

        new_vote = Voted()
        new_vote.user = username
        new_vote.vote = True
        new_vote.save()
    # Result Page
    return redirect('result.html')

def result(request):
    result = Candidate_votes.objects.filter(Election__is_over=False)
    return render(request, 'result.html',{'result':result})
    
