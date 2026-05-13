from django.shortcuts import render
import qrcode
import base64
from io import BytesIO


def index(request):

    qr = None

    if request.method == "POST":

        text = request.POST.get("qr_text")

        qr_image = qrcode.make(text)

        buffer = BytesIO()
        qr_image.save(buffer, format='PNG')

        qr_base64 = base64.b64encode(buffer.getvalue()).decode()

        qr = f"data:image/png;base64,{qr_base64}"

    return render(request, 'qrapp/index.html', {'qr': qr})