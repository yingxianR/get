from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
# Create your views here.
def index(request):
	return render(request,"index.html")

#登录操作

def login_action(request):
	if request.method == 'POST':
		username = request.POST.get('username','')
		password = request.POST.get('password','')
		if username == 'admin' and password == 'admin123':
			response = HttpResponseRedirect('/event_manage/')
			#response.set_cookie('user',username,3600) #设置cookie;
			request.session['user'] = username #设置session;
			return response
		else: 
			return render(request,'index.html',{'error':'username or password error!'})
#发布会管理
def event_manage(request):
	#username = request.COOKIES.get('user','') #读取 浏览器 cookie
	username = request.session.get('user','') #读取 浏览器 session
	return render(request,'event_manage.html',{"user":username})