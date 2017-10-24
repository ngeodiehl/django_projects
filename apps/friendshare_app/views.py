from django.shortcuts import render,redirect
from models import *



def render_homepage(request):                                           # RENDER HOMEPAGE
    context = {
        'users' : User.objects.all()
    }
    return render(request, 'friendshare_app/homepage.html', context)





def render_account_builder(request):                                    # RENDER ACCOUNT BUILDER
    return render(request, 'friendshare_app/account_builder.html')


def build_account(request):                                             # BUILD ACCOUNT
    User.objects.create(
        name = request.POST['name'],
        email = request.POST['email'],
    )
    return redirect('/')






def render_display(request, x_id):                                           # RENDER ACCOUNT DISPLAY PAGE
    context = {
        'x' : User.objects.get(id = x_id)
    }
    return render(request, 'friendshare_app/account_display.html', context)




def render_account_fixer(request, x_id):
    context = {
        'x' : User.objects.get(id = x_id)
    }
    return render(request, 'friendshare_app/account_fixer.html', context)

def fix_account(request, x_id):
    new_user = User.objects.get(id = x_id)
    new_user.name = request.POST['name']
    new_user.email = request.POST['email']
    new_user.save()

    return redirect('/')



def delete_user(request, x_id):
    User.objects.get(id = x_id).delete()

    return redirect('/')
