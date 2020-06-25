from django.shortcuts import render,redirect, get_object_or_404
from .models import Project
from django.utils import timezone
from django.views.generic.edit import CreateView, DeleteView, UpdateView
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib import messages
from .forms import EditProfileForm
from django.contrib.auth import login
from django.shortcuts import redirect
from django.views.generic import CreateView
from .forms import StudentSignUpForm, LecSignUpForm, ReplyForm
from .models import User, Comm, reply
from django.contrib.auth.decorators import login_required
from .decorators import student_required, lecturer_required
from django.utils.decorators import method_decorator


def home(request):
    if request.user.is_authenticated:
        if request.user.is_lecturer :
            return redirect('l_dashboard')
        elif request.user.is_student:
            return redirect('s_dashboard')
  
    return render(request, 'home.html', {})



@login_required
@student_required
def student(request):
	projects = Project.objects.filter(owner = request.user)

	return render(request, 'students/home.html',{"projects":projects})


@login_required
@lecturer_required
def lecturer(request):
	return render(request, 'lecturers/home.html',{})

class ProjectCreate(CreateView):
    model = Project
    fields = ['title','supervisor','owner','project_description','project_category','document']
    template_name = 'project_add_form.html'

    def form_valid(self, form):
    	project = form.save(commit=False)
    	project.save()
    	return redirect('s_dashboard')

class StudentMessage(CreateView):
    model = Comm
    fields = ['subject','mess']
    template_name = 'mess_add_form.html'

    def form_valid(self, form):
        ssage = form.save(commit=False)
        ssage.owner = self.request.user
        me = self.request.user.id
        proj = get_object_or_404(Project, owner = me)
        ilec = proj.supervisor
        ssage.lec = ilec
        ssage.created_time = timezone.now()
        ssage.save()
        return redirect('s_dashboard')


class StudentSignUpView(CreateView):
    model = User
    form_class = StudentSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'student'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('s_dashboard')

class LecSignUpView(CreateView):
    model = User
    form_class = LecSignUpForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'lecturer'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('l_dashboard')

def communicate(request):
    me = request.user.id
    messagess = Comm.objects.filter(lec = me)

    return render(request,'communicate.html',{'messagess':messagess})

def chat(request, pk):
    chatt = get_object_or_404(Comm, pk=pk)
  
    return render(request, 'chat.html', {'chatt':chatt})


