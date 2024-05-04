from django.shortcuts import render
from keras.models import load_model
from keras.preprocessing import image
import numpy as np

# Load the Keras model
model = load_model('myapp/models/keras_model.h5')

def scan(request):
    if request.method == 'POST' and request.FILES['image']:
        # Get the uploaded image
        img = request.FILES['image']
        img = image.load_img(img, target_size=(224, 224))
        img = image.img_to_array(img)
        img = np.expand_dims(img, axis=0)
        img /= 255.0

        # Make prediction
        result = model.predict(img)
        class_idx = np.argmax(result)

        # Map class index to label
        labels = [
            "Tshirt (Allowed)", "Jeans (Allowed)", "Shoes (Allowed)",
            "Hoodies (Allowed)", "Pencil Skirts (Allowed)", "Blouse (Allowed)",
            "Dress (Allowed)", "Crop Top (Not Allowed)", "Sleeveless (Not Allowed)",
            "Tube (Not Allowed)"
        ]
        result = labels[class_idx]

        return render(request, 'myapp/scan.html', {'result': result})

    return render(request, 'myapp/scan.html')


def home(request):
    return render(request, "home.html")