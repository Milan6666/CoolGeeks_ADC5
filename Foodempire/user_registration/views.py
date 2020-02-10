from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

#home function
def home(request):
    return render(request,'user_registration/home.html')
    #validate the form and Registration the user
#sign function or register for new user 
def signup(request):
    if request.method=="POST":
        username=request.POST['username']
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        email=request.POST['email']
        password1=request.POST['password1']
        password2=request.POST['password2']
        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'The username is already taken!!!')
                return redirect('user_registration:signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request, 'The email alreay exists')
                return redirect('user_registration:signup')
            else:
                user=User.objects.create_user(username=username, first_name=first_name, last_name=last_name, email=email, password=password2)
                user.save()
                return redirect('user_registration:login')
        else:
            messages.info(request, 'The passwords did not match!!!')
            return redirect('user_registration:signup')
    else:
        return render(request, 'user_registration/signup.html')

# for login function
def login(request):
    if request.method=="POST":
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('user_registration:home')
        else:
            messages.info(request, 'Please enter valid username and password!!!')
            return redirect('user_registration:login')
    else:
        return render(request, 'user_registration/login.html')

#for logout function
def logout(request):
    auth.logout(request)
    return redirect('user_registration:home')


def aboutUs(request):
    return render(request, 'user_registration/aboutUs.html')


HOME_PER_PAGE = 3
#pagination for home
def homePage(request):
    home = home.objects.all()
    query = ""
    if request.GET:
        query = request.GET.get('q', '')
        #The empty string handles an empty request
    home = search(str(query))

    # pagination
    page = request.GET.get('page', 1)#page to show in adress bar
    paginator = Paginator(HOME_PER_PAGE)
    try:
        home = paginator.page(page)
    except PageNotAnInteger:
        home = paginator.page(1)
        #If searched page is not an integer, deliver first page.
    except EmptyPage:
        home = paginator.page(paginator.num_pages)
        #If searched page is out of range(e.g. 9999), deliver last page.

    return render(request, "user_registration/home.html", {"user_registration" : home, "query" : query})

#search function
def search(query=None):
    queryset = []
    queries = query.split(" ")
    for q in queries:
        home = home.objects.filter(
            Q(title__icontains=q) |
            Q(detail__icontains=q)
            )
        for course in home:
            queryset.append(course)

    return list(set(queryset))


def user_profile(request):
    user_id=request.user
    user=User.objects.get(pk=user_id.id)
    return render(request, 'user_registration/profile.html', {'user':user})

#for updating a profile
def update(request):
    user_info=request.user
    user=User.objects.get(pk=user_info.id)
    return render(request, 'user_registration/profile.html', {'user':user})

def update_completed(request):
    user_info=request.user
    user=User.objects.get(pk=user_info.id)
    if request.method=="POST":
        user.username=request.POST['username']
        user.first_name=request.POST['first_name']
        user.last_name=request.POST['last_name']
        user.email=request.POST['email']
        if User.objects.filter(username=user.username).exists():
            messages.info(request, 'This username is already taken!!!')
            return redirect('user_registration:user_profile')
        elif User.objects.filter(email=user.email).exists():
            messages.info(request, 'This email is already taken!!!')
            return redirect('user_registration:user_profile')
        else:
            user.save()
            messages.info(request, 'Your profile has been successfully updated!!!')
            return render(request, 'user_registration/profile.html')
    else:
        return render(request, 'user_registration/profile.html')




#pegination
def homePage(request,SIZE,PAGENO):
    skip = SIZE * (PAGENO - 1)
    post = Posts.objects.all().order_by('-post_date')[skip: (PAGENO * SIZE)]
    noOfPages = int(ceil(Posts.objects.all().count()/SIZE))
    query = ""
    if request.GET:
        query = request.GET['searchKey']
        post = search(str(query))
        return render(request, 'post/index.html', {'posts': post})
    return render(request, 'post/index.html', {'posts': post, 'noOfPages': range(1,noOfPages+1)})