from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Registration


def home(request):
    return render(request,'user_registration/index.html')
    #validate the form and Registration the user
def signup(request):
        #checks wether the method is post or not
    if request.method=='POST':
        name=request.POST.get('firstname',None)
        lastname=request.POST.get('lastname',None)
        email=request.POST.get('email',None)
        address=request.POST.get('address',None)
        phonenumber=request.POST.get('phonenumber',None)
        gender=request.POST.get('gender',None)
        date=request.POST.get('dateo',None)
        password1=request.POST.get('password1',None)
        password2=request.POST.get('password',None)
        
        if password1==password2: #confirm the password
            Registration_object=Registration() #creates the object of the Registration
            Registration_object.first_name=name
            Registration_object.gender=gender
            Registration_object.phone_number=phonenumber
            Registration_object.date_of_birth=date
            Registration_object.address=address
            Registration_object.password=password2
            Registration_object.email=email
            Registration_object.save()
            return render(request,'user_registration/login.html',{'note':'welcome ','welcome':Registration_object.first_name})
        else:
            return render(request,'user_registration/login.html',{'error': 'passowrd error','fname':name,})
    else:
        return render(request,'user_registration/signup.html')
    #checks the session and help the user to login
def login(request):        
    if request.session.has_key('username'): #check the cookies if the user is already signed in
        tag=request.session['username']
        return render(request,'user_registration/home.html')
    else:
        if request.method == 'POST':
            try:
                #takes the input from the form
                username=request.POST['username']
                passwordd=request.POST['password']
                Registration.objects.get(email=username,password=passwordd) #validate the user
                user=Registration.objects.filter(email=username) #search if the user exists
                if user:
                    username=request.POST['username']
                    request.session['username']=username #creates the session and store for future as cookies
                    tag=request.session['username'] #for BeatX_profile from Add friend table
                    #return redirect("pro")
                    return render(request,'Foodempire_profile/index.html')
                else:
                    return render(request,'user_registration/login.html',{'error': 'User not found'})
            except:
                 return render(request,'user_registration/login.html',{'error': 'one of the information is not correct'})
        else:
            return render(request,'user_registration/login.html')

def logout(request):
    try:
        del request.session['username'] #delete the previously saved cookies
    except:
        pass
    return render(request,'user_registration/login.html',{'se':'please login to continue'})
