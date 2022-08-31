from django.contrib import admin
from django.urls import path
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
# from app.models import Smod
from django.core.files.storage import default_storage


def post(request):
    print(request.FILES)
    file = request.FILES['docfile']
    file_name = default_storage.save(file.name, file)
    return HttpResponse(f"file: {file_name}")


urlpatterns = [
    path('admin/', admin.site.urls),
    path('upload/', csrf_exempt(post), name='upload')
]
