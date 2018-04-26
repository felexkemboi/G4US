from django.shortcuts import render,redirect
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