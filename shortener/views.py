import random
import string

from django.http import HttpResponseRedirect
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import URL


def generate_code():
    return ''.join(
        random.choices(
            string.ascii_letters + string.digits,
            k=6
        )
    )


@api_view(['POST'])
def shorten_url(request):

    original_url = request.data.get('url')

    code = generate_code()

    URL.objects.create(
        original_url=original_url,
        short_code=code
    )

    return Response({
        "short_code": code,
        "short_url": f"http://127.0.0.1:8000/{code}"
    })


from django.shortcuts import get_object_or_404

def redirect_url(request, code):
    url = get_object_or_404(URL, short_code=code)
    return HttpResponseRedirect(url.original_url)