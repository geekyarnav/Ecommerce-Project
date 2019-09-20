from django.contrib.auth import authenticate, login, get_user_model
from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import ContactForm,LoginForm,RegisterForm

def home_page(request):
    if request.user.is_authenticated:
        username_is = "Arnav using context"
        context = { "username_is": request.user}
    else:
        context = {"username_is": request.user}

    return render(request,"base/base.html",context)    

# def home_page2(request):
#     context={
#         "title" : "HomePage",
#         "content": "Welcome to HomePage",
#     }
#     if request.user.is_authenticated:

#         context["premuim_content"] = "Welcome to Premium home page"
#     return render(request,"home/home_page.html", context)

def about_page(request):
    context={
         "title" : "aboutPage",
         "content" : "Welcome to AboutPage"
     }
    return render(request,"about/about_page.html",context)    

def contact_page(request):
     contact_form = ContactForm(request.POST or None)
     context = {
         'title':'Contact_page',
         'form': contact_form
     }
     if contact_form.is_valid():
         print(contact_form.cleaned_data)
     return render(request,'contact/contact_page.html', context)


def login_page(request):
    form = LoginForm(request.POST or None)
    context={
            'form':LoginForm()
    } 
    #print("USER LOGGED IN")
    #print(request.user.is_authenticated)    
    if form.is_valid():
        print(form.cleaned_data)
        username=form.cleaned_data.get("username")
        password=form.cleaned_data.get("password")
        user=authenticate(request,username=username,password=password)
        #print(request.user.is_authenticated())
        if user is not None:
             #print(user.is_authenticated())
             #login(request, user)
            context['form'] = LoginForm()
             #redirect to success login page
            return redirect('/login')
        else:
            print("EndUser")
    return render(request,'auth/login.html',context)    

User=get_user_model()
def registration_page(request):
    form = RegisterForm(request.POST or None)
    context={
        'form':form
    }
    if form.is_valid():
        print(form.cleaned_data)
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        password2 = form.cleaned_data.get("password2")
        email = form.cleaned_data.get("email")
        new_user = User.objects.create(username=username, email=email, password=password)
        new_user.save()
    return render(request,'auth/register.html',context)   

# #testing static files

# def index(request):
    
#     return render(request,"index.html",{})