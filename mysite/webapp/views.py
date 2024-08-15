from django.shortcuts import redirect, render
from .forms import CreateUserForm, LoginForm, CreateRecordForm, UpdateRecordForm

from django.contrib.auth.models import auth
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from webapp.models import Record
from django.contrib import messages


def home(request):
    return render(request, "webapp/index.html")

def register(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account created successfully!")
            return redirect('the-login')
        
    context={'form':form}
    return render(request, 'webapp/register.html', context=context)

#The login view

def the_login(request):
    form = LoginForm()
    if request.method == 'POST':
        form=LoginForm(request, data=request.POST)
        if form.is_valid():
            username=request.POST.get('username')
            password=request.POST.get('password')

            user=authenticate(request, username=username, password=password)

            if user is not None:
                auth.login(request, user)
                return redirect('dashboard')

    context={'form':form}
    return render(request, 'webapp/the_login.html', context=context)


#the logout

def the_logout(request):
    auth.logout(request)
    messages.success(request, "Your loged out successfully!")
    return redirect('the-login')



#the dashboard
@login_required(login_url='login/')
def dashboard(request):
    my_records = Record.objects.all()
    context={'records':my_records}
    return render(request, 'webapp/dashboard.html', context=context)


@login_required(login_url='login/')
def create_record(request):
    form=CreateRecordForm()
    if request.method == 'POST':
        form=CreateRecordForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record is created successfully!")
            return redirect('dashboard')
    context={'form':form}
    return render(request, 'webapp/create-record.html', context=context)


@login_required(login_url='login/')
def update_record(request, pk):
    record=Record.objects.get(id=pk)
    form=UpdateRecordForm(instance=record)
    if request.method == 'POST':
        form = UpdateRecordForm(data=request.POST, instance=record)
        if form.is_valid():
            form.save()
            messages.success(request, "Your record is updated successfully!")
            return redirect('dashboard')
    context={'form':form}
    return render(request, 'webapp/update-record.html', context=context)


#singular view
@login_required(login_url='login/')
def view_record(request, pk):
    record=Record.objects.get(id=pk)
    messages.success(request, "Your record is delated successfully!")
    return render(request, 'webapp/view-record.html', {'record':record})



#delete
@login_required(login_url='login/')
def delete_record(request, pk):
    record=Record.objects.get(id=pk)
    if request.method == 'POST':
        record.delete()
        messages.success(request, "Your record was delated successfully!")
        return redirect('dashboard')
    return render(request, 'webapp/delete-record.html', {'record':record})