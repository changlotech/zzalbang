from django.http import HttpResponseForbidden

from galleryapp.models import Gallery


def gallery_ownership_required(func):
    def decorated(request, *args, **kwargs):
        gallery = Gallery.objects.get(pk=kwargs['pk'])
        if not gallery.writer == request.user:
            return HttpResponseForbidden()
        return func(request, *args, **kwargs)
    return decorated