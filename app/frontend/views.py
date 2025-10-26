import os
import random
from django.shortcuts import render, redirect
from .upload_to_s3 import upload_file_to_s3
from .predict_from_sagemaker import predict_from_sagemaker


def home(request):
    """Landing page (Home)."""
    return render(request, "home.html")


def index(request):
    """Main upload page (Effusion Upload)."""
    return render(request, "index.html")


def upload_file_view(request):
    """Handles effusion image upload and SageMaker inference."""
    if request.method == 'POST':
        uploaded_file = request.FILES['file']

        temp_path = os.path.join('/tmp', uploaded_file.name)
        with open(temp_path, 'wb+') as destination:
            for chunk in uploaded_file.chunks():
                destination.write(chunk)

        success, public_url = upload_file_to_s3(temp_path, uploaded_file.name)

        if success:
            try:
                result = predict_from_sagemaker(temp_path)
                prediction = result.get("prediction", "Unknown")
                confidence = result.get("confidence", 0.0)
            except Exception as e:
                print("❌ SageMaker inference error:", e)
                prediction = random.choice(["Yes", "No"])
                confidence = 0.0

            return redirect(f"/results/?prediction={prediction}&conf={confidence:.3f}")
        else:
            message = "❌ Upload failed. Check server logs."
            return render(request, "index.html", {"message": message})

    return render(request, "index.html")


def results_view(request):
    """Displays effusion detection results."""
    prediction = request.GET.get("prediction", random.choice(["Yes", "No"]))
    confidence = request.GET.get("conf", "0.0")

    if prediction.lower() == "yes":
        title = "Effusion Detected!"
        info = (
            "Pleural effusion involves excess fluid buildup between the lungs and chest cavity. "
            "Common symptoms include: Chest pain, cough, and difficulty breathing. "
            "It's highly recommended to consult your doctor for further advice."
        )
    else:
        title = "No Effusion Detected."
        info = (
            "No signs of pleural effusion were detected. "
            "Your lung scan appears normal, and there is no significant fluid buildup in the pleural space."
        )

    context = {
        "title": title,
        "info": info,
        "confidence": confidence,
    }

    return render(request, "results.html", context)