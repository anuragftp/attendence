from django.shortcuts import render
from django.views.generic import View

# Create your views here.


class HomeView(View):
	template_name='core/welcome.html'


	def get(self,request,*args,**kwargs):
		return render(request,self.template_name)

	# def post(self,request,*args,**kwargs):
	# 	form=self.form_class(request.POST)
	# 	if form.is_valid():
	# 		form.save()
	# 		return redirect('signin_view')

	# 	context={'form':form}

	# 	return render(request,self.template_name,context)