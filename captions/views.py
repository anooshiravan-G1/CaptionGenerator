import subprocess
#import cv2
import psycopg2
import os
import re
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.urls import reverse

from .models import ImageCaption
from .forms import ImageUploadForm



def captionAndImageOutput(request, pk):
    image = ImageCaption.objects.get(pk=pk)
    image_url = image.image.url
    return render(request, 'caption.html', {'caption': image.caption, 'image_url': image_url})


def generate_caption(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():

            image_file = request.FILES['image']
            with open('temp_image.jpg', 'wb') as f:
                f.write(image_file.read())
            image_path = 'temp_image.jpg'

            # Define the command to run
            checkpoint_path = "im2txt/model/Hugh/train/newmodel.ckpt-2000000"
            vocab_file = "im2txt/data/Hugh/word_counts.txt"
            command = f"python im2txt/run_inference.py --checkpoint_path={checkpoint_path} --vocab_file={vocab_file} --input_files={image_path}"

            # Run the command and capture the output
            output = subprocess.check_output(command, shell=True)

            # Parse the output to extract the caption
            modelOutput = output.decode("utf-8").strip()
            # Split the modelOutput into lines
            lines = modelOutput.splitlines()
            # Get the last 3 lines
            caption = '\n'.join(lines[-3:])
            caption = '\n'.join(line + '\n' for line in caption.split('\n'))
            caption = re.sub(r'\(p=0.\d+\)', '', caption)

            #os.remove(image_path)
            image_caption = ImageCaption()
            image_caption.image = form.cleaned_data['image']
            image_caption.caption = caption
            image_caption.save()
            # return HttpResponse(f"Caption generated and saved: {caption}")
            pk = image_caption.pk
            url = reverse('captions:captionAndImageOutput', args=[pk])
            return redirect(url)
    else:
            form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})


