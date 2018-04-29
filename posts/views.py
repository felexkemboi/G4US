from .models import Post,Comment
from ebooks.models import Document
from django.utils import timezone
from django.shortcuts import render,get_object_or_404,redirect,render
from .forms	import	NewPostForm,SignUpForm,CommentForm
from django.urls import reverse_lazy
from django.views import generic

# Create your views here.
def index(request):
	return render(request,'relax.html', {})

def home(request):
	ebook = Document.objects.all()
	posts = Post.objects.all() #order_by('created_date')
	return render(request,'home.html', {'posts': posts,'ebooks':ebook,})

def posts(request):
	posts =  Post.objects.order_by('created_date')
	return render(request, 'posts.html', {'posts':posts,})

def detail(request,pk):
	post = get_object_or_404(Post,pk= pk )
	return render(request,'detail.html', {'post':post})

def delete(request,pk):
	post = get_object_or_404(Post,pk= pk )
	return render(request,'delete.html', {'post':post})



def	new_post(request):
	if	request.method	==	"POST":
		form = NewPostForm(request.POST)
		if	form.is_valid():
			post = form.save(commit=False)
			#post.author	=	request.user
			post.created_date	=	timezone.now()
			post.save()
		return	redirect('home')
	else:
		form = NewPostForm()
		return	render(request,	'new_post.html',	{'form':	form})


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

def comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.author= request.user
            comment.save()
            return redirect('detail', pk=post.pk)
    else:
        form = CommentForm()
    return render(request, 'comment.html', {'form': form})

def remove(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    comment.delete()
    return redirect('detail', pk=comment.post.pk)