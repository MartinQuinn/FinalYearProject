from django.shortcuts import render , redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
# Create your views here.

# sign up function 
def signup(request):
    if request.method =='POST':
        # checking to if passwords match
        if request.POST['password1'] == request.POST['password2']:

            try:
                #checking to see if username is taken
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error':'Username already taken.'})
            except User.DoesNotExist:
                # if the user does not exist it is added to the database
                user = User.objects.create_user(request.POST['username'],password=request.POST['password1'])
                login(request, user)
                return render(request, 'accounts/signup.html')
        else:
            #if Passwords dont match it sends an error message
            return render(request, 'accounts/signup.html', {'error':'Passwords don\'t match.'})
    else:
        # if there is no information it will pass the page again to await input "POST"
        return render(request, 'accounts/signup.html')

# login 
def loginview(request):
    if request.method =='POST':
        # using django built in function to authenticate a user logging in
        user = authenticate(username=request.POST['username'], password=request.POST['password'])
        # if the user exists, user gets logged in
        if user is not None:
            login(request, user)
            # if the user wants to get to the accounts section but  
            # is not logged in it will redirect the to the login 
            # page, but when successfully logged in it will send 
            # them to the page they originally wanted to go to 
            if 'next' in request.POST:
                    return redirect(request.POST['next'])
            # message to prompt user was successfully logged in
            return render(request, 'accounts/login.html', {'error':'Login successful!'})
        else:
            # if the information was not valid it sends the error message 
            return render(request, 'accounts/login.html', {'error':'No valid information.'})
    else:
        # if there is no information it will pass the page again to await input "POST"
        return render(request, 'accounts/login.html')
