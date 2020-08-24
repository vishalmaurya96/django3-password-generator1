from django.shortcuts import render
from django.http import HttpResponse
import random
# Create your views here.
def home(request):
    return render(request,'generator/home.html')

def generate(request):
    return render(request,'generator/generate.html')


def lottery(request):
        lotteryspace=list("abcdefghijklmnopqrstuvwxyz")
        if request.GET.get('upper'):
            lotteryspace.extend(list("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
        if request.GET.get('spc_chars'):
            lotteryspace.extend(list("!@#$%&*"))
        if request.GET.get('num'):
            lotteryspace.extend(list("0123456789"))

        thelottery=""
        length=int(request.GET.get('len'))
        for x in range(length):
            thelottery += random.choice(lotteryspace)
        return render(request,'generator/lottery.html',{'lottery':thelottery})
