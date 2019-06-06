from django.http import Http404
from django.shortcuts import render
from . models import Question 

def index(request):
	latest_question_list = Question.objects.order_by('-pub_date')[:5]
	context = {'latest_question_list':latest_question_list
	}
	return render(request,'converter/index.html',context)

# Create your views here.
def details(request,question_id):
	try:
		question = Question.objects.get(pk=question_id)

	except Question.DoesNotExist:
		raise Http404('Question doesnot exist')

	return render(request,'converter/details.html',{'question':question})


def results(request,question_id):
	response = "you're looking at the results of question %s."
	return HttpResponse(response %question_id)

def vote(request,question_id):
	return HttpResponse("You're voting on question %s" %question_id)

# def homepage(request):
# 	return render(request, 'home.html')

# def convert_length(request):
# 	meter1 = request.GET['meter']
# 	c = meter1 * 2
# 	return render(request, 'convert_length.html',{'centimeter':float(c) })



# Create your views here.
