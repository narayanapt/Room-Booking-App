from django.shortcuts import render
from django.contrib.auth.models import User
from .models import Visitor,Room,Booking
from .forms import UserRegistrationForm,VisitorForm,RoomsForm
from django.http import HttpResponseRedirect,HttpResponse
from django.urls import reverse
from django.db.models import Q

# Create your views here.




def index(request):
	return render(request,'room_booking/index.html')



def register(request): 

	if request.method == 'POST':
		user_form = UserRegistrationForm(request.POST)
		visitor_form = VisitorForm(request.POST)
		if user_form.is_valid() and visitor_form.is_valid():
			user_obj = user_form.save(commit = False)
			user_obj.set_password(user_obj.password)
			user_obj.save()
			visitor_obj = visitor_form.save(commit = False)
			visitor_obj.user = user_obj
			visitor_obj.save()
			return HttpResponseRedirect(reverse('room_booking:login'))
		else:
			context = {'user_form' : user_form, 'visitor_form': visitor_form}
	else:
		user_form = UserRegistrationForm()
		visitor_form = VisitorForm()
		context = {'user_form' : user_form, 'visitor_form': visitor_form}
	return render(request,'room_booking/register.html',context)


def user_home(request):
	if request.method == 'POST':
		flag = 0
		for x in request.POST.keys():
			if x=='room_name':
				flag=1

		if flag ==1:

			form = RoomsForm(request.POST)
			if form.is_valid():
				fd = form.cleaned_data['from_date']
				td = form.cleaned_data['to_date']
				user_obj= User.objects.get(username=request.user)
				b = Booking(from_date=fd,to_date=td,room=Room.objects.get(id=request.POST['room_name']),visitor=Visitor.objects.get(user=user_obj))
				b.save()
				vis = User.objects.get(username = request.user).visitor
				context = {'room':Room.objects.get(id=request.POST['room_name']),
				'user_info':request.user,
				'booking_obj_list':Booking.objects.filter(visitor=vis)}
				return render(request,'room_booking/bookings.html',context)
			# else:
			# 	return HttpResponseRedirect(reverse('room_booking:bookings'))



		else:

			form = RoomsForm(request.POST)
			if form.is_valid():
				fd = form.cleaned_data['from_date']
				td = form.cleaned_data['to_date']
				queries = Booking.objects.exclude((Q(from_date__lt=fd)&Q(to_date__lt=td))|(Q(from_date__gt=fd)&Q(to_date__gt=td)))
				room_list = []
				for q in queries:
					room_list.append(q.room.room_no)
				room_obj_list = Room.objects.exclude(room_no__in=room_list)
				context = {'rooms' : Room.objects.exclude(room_no__in=room_list),'form':form,'fd':fd,'td':td}
	else:
		form = RoomsForm()
		context = {'form' : form}
	return render(request,'room_booking/user_home.html', context)


def bookings(request):

	vis = User.objects.get(username = request.user).visitor
	context= {'booking_obj_list':Booking.objects.filter(visitor=vis)}
	return render(request,'room_booking/bookings.html',context)


