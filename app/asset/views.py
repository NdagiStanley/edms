from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import *
from .models import *
from photologue.forms import UploadZipForm
from .mayan import documentUpload


def uploadPhoto(request):
    if request.method == "POST":
        imageform = PhotoUploadForm(request.POST or None, request.FILES or None)
        zipform = UploadZipForm(request.POST or None, request.FILES or None)
        # to save single image
        if imageform.is_valid():
            imageform.save()
            messages.success(request, "photos uploaded")
        # to save a zip of image
        if zipform.is_valid():
            zipform.save()
            messages.success(request, "zip of photos uploaded")
        return redirect("uploadPhoto")
    imageform = PhotoUploadForm()
    zipform = UploadZipForm()
    data = {"title": "upload image", "imageform": imageform, "zipform": zipform}
    return render(request, "asset/uploadPhoto.html", data)


def uploadDocument(request):
    if request.method == "POST":
        response = documentUpload(request)
        # create a document object
        Document.objects.create(
            description=response["description"],
            document_type=response["document_type"],
            fileUrl=response["url"],
            downloadUrl=response["downloadUrl"],
            previewUrl=response["previewUrl"],
            document_id=response["id"],
            label=response["label"],
            language=response["language"],
        )
        messages.success(request, "document uploaded")
        return redirect("uploadDocument")

    form = documentForm()
    data = {"title": "upload document", "documentForm": form}
    return render(request, "asset/uploadDocument.html", data)


def viewDocument(request):
    document = Document.objects.all()
    data = {"title": "view document", "documents": document}
    return render(request, "asset/viewDocument.html", data)
