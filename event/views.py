from django.shortcuts import render, get_object_or_404, redirect
from event.models import Event, EventCreator, EventAttendence
from django.contrib.auth.models import User
from django.views import generic
from django.urls import reverse, reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def index(request):
    return render(request, 'index.html')

class EventListView(LoginRequiredMixin, generic.ListView):
    model = Event
    paginate_by = 5

class EventDetailView(LoginRequiredMixin, generic.DetailView):
    model = Event

class EventAttendenceCreate(LoginRequiredMixin, generic.CreateView):
    model = EventAttendence
    fields = ['profile', 'name', 'email', 'date_of_birth', 'phone_no', 'event']

    # def get_initial(self):
    #     initial = super().get_initial()
    #     initial['event'] = self.request.
    #     return initial
    
    def get_context_data(self, **kwargs):
        context = super(EventAttendenceCreate, self).get_context_data(**kwargs)
        context["event"] = get_object_or_404(Event, pk=self.kwargs['pk'])
        return context

    def get_success_url(self):
        return reverse('event-detail', kwargs={'pk': self.kwargs['pk'],})

class EventAttendenceDetail(generic.DetailView):
    model = EventAttendence

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('events')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})
