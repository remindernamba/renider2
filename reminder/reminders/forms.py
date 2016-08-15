from django import forms
from note.models import Group


class CreateGroup(forms.ModelForm):

    class Meta:
        model = Group
        fields = ('name', 'user',)
