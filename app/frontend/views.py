from django.shortcuts import render
from .upload_to_s3 import upload_file_to_s3
import os

def upload_file_view(request):
    message = None
    if request.method == 'POST':
        uploaded_file = request.FILES['file']
        temp_path = os.path.join('/tmp', uploaded_file.name)

        with open(temp_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        success, public_url = upload_file_to_s3(temp_path, uploaded_file.name)

        if success:
            message = f"✅ Uploaded successfully! <a href='{public_url}' target='_blank'>View file</a>"
        else:
            message = "❌ Upload failed. Check server logs."

    # 👇 this must match the template filename exactly
    return render(request, 'upload.html', {'message': message})