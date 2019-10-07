from django.shortcuts import render,redirect,get_object_or_404
from.models import admitpasent
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from.forms import Createnewac , UserUpdateForm , ProUpdate , pupdate
from django.contrib.auth.decorators import login_required
from django.views.generic import DeleteView
from django.contrib.auth.mixins import UserPassesTestMixin,LoginRequiredMixin


# Create your views here.
@login_required(login_url='login')
def park(request):
	if request.method == 'POST':
		admit=admitpasent()
		admit.name=request.POST['name']
		admit.gender=request.POST['gender']
		admit.birthdate=request.POST['birthdate']
		admit.diseases=request.POST['diseases']
		admit.address=request.POST['address']
		admit.admit_charge=request.POST['admit_charge']
		admit.user=request.user
		admit.save()
		messages.success(request,f'Your data ensart success now')
		return redirect('admit')
	else:
		return render(request,'user/index.html')



def showpatient(request):
	patient=admitpasent.objects.all()
	return render(request,'user/show.html',{'p':patient })

#sign up new user (create new user) in out project 

def register(request):
	if request.method == 'POST':
		form = Createnewac(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			messages.success(request,f'your account created {username}')
			return redirect('login')
	else:
		form = Createnewac()
	return render(request,'user/signup.html',{'form':form})


#user profile update code 

def profile(request):
	if request.method == 'POST':
		u_f = UserUpdateForm(request.POST,instance = request.user)
		p_f = ProUpdate(request.POST,
			            request.FILES,
						instance = request.user.userprofile)
		if u_f.is_valid() and p_f.is_valid():
			u_f.save()
			p_f.save()
			messages.success(request, f'Your account has been updated!')
			return redirect('profile')
	else:
		u_f = UserUpdateForm(instance = request.user)
		p_f = ProUpdate(instance = request.user.userprofile)

	context = {
			'u':u_f,
			'p':p_f
	}
	

	return render(request,'user/profile.html',context)


def patiantupdate(request,pid):
	if request.method == 'POST':
		f = pupdate(request.POST,request.admitpasent.user,instance=get_object_or_404(admitpasent,id=pid))
		if f.is_valid():
			f.save()
			return redirect('patientdetail')
	else:
		f = pupdate(instance=get_object_or_404(admitpasent,id=pid))
		

	return render(request,'user/pupdate.html',{'f':f})


class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = admitpasent
    success_url = '/'

    def test_func(self):
        post = self.get_object()
        if self.request.user == post.user:
            return True
        return False
