
from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
	return render(request,"index.html")

def about_us(request):
	return render(request,"about_us.html")


def industry(request):
	return render(request,"industry.html")

def other(request):
	return render(request,"other.html")

def contact_us(request):
	return render(request,"contact_us.html")


def coverage(request):
	return render(request,"coverage.html")


def join_our_panel(request):
	return render(request,"join_our_panel.html")


def qualitative(request):
	return render(request,"qualitative.html")

def quantitative(request):
	return render(request,"quantitative.html")
