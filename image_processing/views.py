from django.shortcuts import render
from django.http import JsonResponse
from django.views import View
from .models import Image, Description
from .forms import ImageUploadForm


class ImageUploadView(View):
    def get(self, request, *args, **kwargs):
        form = ImageUploadForm()
        return render(request, 'upload_image.html', {'form': form})

    def post(self, request, *args, **kwargs):
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            image = form.save()
            description_text = "This is a generated description."
            Description.objects.create(image=image, description_text=description_text)
            return JsonResponse({"message": "Image uploaded and processed.", "image_id": image.id})
        else:
            return JsonResponse({"errors": form.errors}, status=400)
