from django.shortcuts import render, redirect
from django.http import HttpResponse, FileResponse, JsonResponse
from django.views.generic import TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from django.conf import settings
from media.Recordings.size import get_file_size, get_folder_size
import os
from django.conf import settings
import zipfile
from django.contrib import messages
import shutil



# Create your views here.
record_dir = os.path.join(settings.MEDIA_ROOT, 'Recordings')
init_dir = os.getcwd()


@login_required
def review_index(request):
    videoid = ""
    files = []
    filepath_videos = settings.MEDIA_ROOT + '/Recordings'
    for filename in os.listdir(filepath_videos):
        if filename.endswith(".mkv"):
            files.append(filename)
            continue
        else:
            continue
    filepath = settings.MEDIA_ROOT + '/log.txt'
    file = open(filepath, "r")
    log = file.readlines()
    files = sorted(files)
    template = 'review/index.html'
    context = {
        'log': log,
        'review_active': 'active',
        'files': files,
        'video': 'sdf',
        # 'id': videoid,

    }
    print(files)
    file.close()
    return render(request, template, context)


@login_required
def video_info(request):
    if request.is_ajax and request.method == "POST":
        total, used, free = shutil.disk_usage("/")
        free_space = str(round(free / (2 ** 30), 2)) + ' GB'
        video = request.POST.get('video')
        recordings_size = get_folder_size('gb')
        video_size = get_file_size(video, size_type='mb')
        data = {
            'video_size': video_size,
            'recordings_size': recordings_size,
            'free_space': free_space,
        }
        return JsonResponse(data)

# @login_required
# def protect_media(request, filename):


@login_required
def download(request, file):
    file_dir = os.path.join(record_dir, file)
    response = FileResponse(open(file_dir, 'rb'))
    response['Content-Disposition'] = "attachment; filename=%s" % \
                                      file
    return response


@login_required
def download_log(request):
    file_dir = os.path.join(settings.MEDIA_ROOT, 'log.txt')
    response = FileResponse(open(file_dir, 'rb'))
    response['Content-Disposition'] = "attachment; filename=log.txt"
    return response


@login_required
def delete(request, file):
    file_dir = os.path.join(record_dir, file)
    os.remove(file_dir)
    print(file + " has been deleted")
    messages.success(request, str(file) + " has been deleted")
    return redirect('/review/#videos')


@login_required
def download_all_videos(request):
    os.chdir(record_dir)
    zip_obj = zipfile.ZipFile('Records.zip', 'w')
    files = os.listdir()
    for file in files:
        if file[-4:] == ".mkv":
            zip_obj.write(file)
        else:
            continue
    zip_obj.close()
    file_dir = os.path.join(record_dir, 'Records.zip')
    response = FileResponse(open(file_dir, 'rb'))
    response['Content-Disposition'] = "attachment; filename=Records.zip"
    os.chdir(init_dir)
    return response


@login_required
def delete_all_videos(request):

    os.chdir(record_dir)
    files = os.listdir()
    for file in files:
        if file[-4:] == ".mkv" or file == 'Records.zip':
            try:
                os.remove(file)
            except PermissionError:
                pass
        else:
            continue
    messages.success(request, "All recorded videos have been deleted")
    os.chdir(init_dir)
    return redirect('/review/#videos')
