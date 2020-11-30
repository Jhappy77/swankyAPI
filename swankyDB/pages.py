## I have no idea if we want to keep this fiel within swankyDB or refactor
## This is the basis upon which webpages will be rendered. We will need to discuss
## app architecture later.
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth import authenticate, login, logout


from django.contrib import messages 

# Our custom forms
from .forms import CustomCreateUserForm

#(∩ ͡° ͜ʖ ͡°)⊃━☆ﾟ. * ･ ｡ﾟ,  Some magic for automatically making a user registration form, and saving the users to the DB
# https://www.youtube.com/watch?v=tUqUdu0Sjyc
def registerPage(request):
    form = CustomCreateUserForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() #Registers the user

            user = form.cleaned_data.get('username')
            messages.success(request, 'Your account, '+ user + ' has signed up!')
            return redirect('loginPagePlaceholder')

    context = {'form':form}
    return render(request, 'pathtohtmlfile?', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('pathToRedirectTo')
        else:
            messages.info(request, 'You entered an incorrect username or password')
    
    context = {}
    return render (request, 'pathtoHTMLFile', context)


#TODO: Logout User path

"""
In HTML File:

<div>
<form method="POST" action="">
    {% csrf_token %}
    {{form.as_p}}
    <input type="submit" name="Create User" />
    {{form.errors}}
</form>
    {% for message in messages %}
    <p id="messsages">{message}</p>
    {% endfor %}
</div>

# To make modifications: https://www.youtube.com/watch?v=tUqUdu0Sjyc?t=676
"""

