from .models import Post
from django.utils import timezone
from django.shortcuts import render,get_object_or_404,redirect,render
from .forms	import	NewPostForm,SignUpForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
def index(request):
	return render(request,'relax.html', {})

def home(request):
	posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request,'home.html', {'posts': posts})

def posts(request):
	posts = Post.objects.filter(created_date__lte=timezone.now()).order_by('created_date')
	return render(request, 'posts.html', {'posts':	posts})

def detail(request,pk):
	post = get_object_or_404(Post,pk= pk )
	return render(request,'detail.html', {'post':post})

def delete(request,pk):
	post = get_object_or_404(Post,pk= pk )
	return render(request,'delete.html', {'post':post})



def	new(request):
	if	request.method	==	"POST":
		form	=	NewPostForm(request.POST)
		if	form.is_valid():
			post	=	form.save(commit=False)
			#post.author	=	request.user
			post.created_date	=	timezone.now()
			post.save()
		return	redirect('posts',	pk=post.pk)
	else:
		form	=	NewPostForm()
		return	render(request,	'new.html',	{'form':	form})


def edit(request,pk):
	post = get_object_or_404(Post,pk= pk )
	if request.method == "POST":
		form = NewPostForm(request.POST,instance = post  )
		if form.is_valid():
			post = form.save(commit = False)
			#post.author = request.user
			post.created_date = timezone.now()
			post.save()
			return redirect('detail', pk = post.pk )
	else:
		form = NewPostForm(instance = post )

	return render(request,'edit.html',{'form': form })