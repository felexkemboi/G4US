from .models import Post
from django.utils import timezone
from django.shortcuts import render,get_object_or_404,redirect,render
from .forms	import	NewPostForm,SignUpForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
def home(request):
	return render(request,'index.html', {})

def list(request):
	posts	=	Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
	return	render(request,	'list.html',	{'posts':	posts})

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
			#post.published_date	=	timezone.now()
			post.save()
		return	redirect('detail',	pk=post.pk)
	else:
		form	=	NewPostForm()
		return	render(request,	'new.html',	{'form':	form})


def edit(request,pk):
	post = get_object_or_404(Post,pk= pk )
	if request.method == "POST":
		form = PostForm(request.POST,instance = post  )
		if form.is_valid():
			post = form.save(commit = False)
			post.author = request.user
			post.published_date = timezone.now()
			post.save()
			return redirect('detail', pk = post.pk )
	else:
		form = PostForm(instance = post )

	return render(request,'edit.html',{'form': form })