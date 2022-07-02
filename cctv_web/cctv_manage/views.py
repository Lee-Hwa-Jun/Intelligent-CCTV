from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import File_list,User
from wsgiref.util import FileWrapper
import os

# Create your views here.
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

def index(request):
    # files = File_list.objects.all()
    files = os.listdir(BASE_DIR + "\\static\\files")
    files = [x[0:-4] for x in files]
    files_ = [[]]
    for x in files:
        try:
            if (x[0:11] == files_[-1][-1][0:11]):
                files_[-1].append(x)
            else:
                files_.append([x])
        except:
            files_[-1].append(x)
    return render(request,'cctv_manage/index.html',{'files' : files_})

def download(request,file_name):
    try:
        file_path = BASE_DIR + f'\\static\\files\\{file_name}'+'.mp4'
        wrapper = FileWrapper(open(file_path, 'rb'))
        response = HttpResponse(wrapper, content_type='video/mp4')
        response['Content-Disposition'] = 'inline; filename=' + os.path.basename(file_path)+'.mp4'
        return response
    except Exception as e:
        return None