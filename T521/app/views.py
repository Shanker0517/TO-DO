from django.shortcuts import render,redirect
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.views import LoginView
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Task
# Create your views here.
class UserRegistration(FormView):
    template_name='registration/register.html'
    form_class=UserCreationForm
    # redirect_authenticated_user=True
    success_url=reverse_lazy('tasks')
    def form_valid(self, form):
        user=form.save()
        if user is not None:
            login(self.request,user)
            return super(UserRegistration, self).form_valid(form)
    # def get(self, *args, **kwargs):
    #     if self.request.user.is_authenticated:
    #         return redirect('tasks')
    #     return super(UserRegistration, self).get(*args, **kwargs)



class UserLogin(LoginView):
    template_name='registration/login.html'
    fields='__all__'
    redirect_authenticated_user=True
    def get_success_url(self):
        return reverse_lazy('tasks')
        
    

class TaskList(LoginRequiredMixin,ListView):
    model=Task
    context_object_name='items'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["items"] = context["items"].filter(user=self.request.user)
        context["count"] = context["items"].filter(complete=False).count()
        return context
    
    
    # template_name='app/task_list.html'
    # paginate_by=3

class TaskDetail(DetailView):
    model=Task
    context_object_name='items'

class TaskCreate(CreateView):
    model=Task
    fields=['title','decription','complete']
    success_url=reverse_lazy('tasks')
    template_name='app/task_add.html'
    def form_valid(self, form):
        form.instance.user=self.request.user
        return super(TaskCreate, self).form_valid(form)

class TaskUpdate(UpdateView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('tasks')
    template_name='app/task_update.html'

class TaskDelete(DeleteView):
    model=Task
    fields='__all__'
    success_url=reverse_lazy('tasks')
    template_name='app/task_delete.html'
