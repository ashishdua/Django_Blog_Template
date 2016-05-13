#from django.http import HttpResponse
from django.shortcuts import get_object_or_404,render
#from forms import feedbackForm
from .models import blogPost
#from .models import feedback
from django.views.generic import View

# Create your views here.
def blog_list(request):
	blogs=blogPost.objects.all()
	#feedbacks=feedback.objects.all()
	return render(request,'blogApp/blog_list.html',{'blogs':blogs})



def blog_detail(request,pk):
	blogs=get_object_or_404(blogPost,pk=pk)
	return render(request,'blogApp/blog_detail.html',{'blogs':blogs})


#def feedback_form(request):
#	feedbacks=feedback.objects.all()
#	return render(request,'blogApp/blog_list.html',{'feedbacks':feedbacks})

#class myForm(View):

#	def get(self,request):
#		form = feedbackForm
		#return render(request,'/blogs',locals())
#		return HttpResponse("get")

#	def post(self,request):
#		return HttpResponse("post")