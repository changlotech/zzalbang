from django.forms import ModelForm

from galleryapp.models import Gallery


class GalleryCreationForm(ModelForm):
    class Meta:
        # 모델은
        model = Gallery
        #다음과 같은 모델의 필드들을
        fields = ['image', 'title', 'description']
