# coding: utf-8
# @author: Lazy Yao
# @email: none
# @date: 2021/05/08 16:33

from django.shortcuts import HttpResponse, render, redirect


def login(request):
    return render(request, "login/login1.html")