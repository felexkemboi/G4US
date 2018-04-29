from django.shortcuts import render,redirect,get_object_or_404
from .forms import DocumentForm
from .models import Document

def upload(request):
	if request.method == 'POST':
		form = DocumentForm(request.POST,request.FILES)
		if form.is_valid():
			#handle_uploaded_file(request.FILES['file'])
			form.save()
			return redirect('home')
	else:
		form = DocumentForm()
	return render(request,'upload.html',{'form':form})
"""
def ebooks(request):
	ebook = Document.objects.all()
	return render(request, 'ebook.html', {'ebooks': ebook,})

"""

def detail(request,pk):
	document = get_object_or_404(Document,pk=pk )
	return render(request,'ebook-detail.html', {'document':document})

def edit(request,pk):
	document = get_object_or_404(Document,pk= pk )
	if request.method == "POST":
		form = DocumentForm(request.POST,instance = document  )
		if form.is_valid():
			post = form.save(commit = False)
			#post.author = request.user
			#post.created_date = timezone.now()
			post.save()
			return redirect('ebook-detail', pk = post.pk )
	else:
		form = DocumentForm(instance = document )

	return render(request,'ebook-edit.html',{'form': form })
