# coding:utf-8
from django.shortcuts import render
from django.http import *


def index(request):
    return HttpResponse('hello halo')

#
# def index(request):
#     return HttpResponse('index')


