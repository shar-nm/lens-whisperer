from django import forms

from .models import Article


INPUT_CLASSES = 'w-100 py-1 px-3 rounded-xl border'


class NewArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('category', 'title', 'image', 'camera','lens','aperture','shutter_speed','Iso','description',)

        widgets = {
            'category': forms.Select(attrs={
                'class': INPUT_CLASSES
            }),
            'title': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'image': forms.FileInput(attrs={
                'class': INPUT_CLASSES
            }),
            'camera': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
             'lens': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'aperture': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            
            'shutter_speed': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'Iso': forms.TextInput(attrs={
                'class': INPUT_CLASSES
            }),
            'description': forms.Textarea(attrs={
                'class': INPUT_CLASSES
            })
        }