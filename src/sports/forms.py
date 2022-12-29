from django import forms
from .models import Team, Post


class TeamForm(forms.ModelForm):
    class Meta:
        model = Team
        fields = "__all__"
        labels = {
            "name": "Nom de l'équipe",
            "country": "Le pays",
            "name_of_field": "Nom du stade"
        }
        exclude = ["slug"]


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = "__all__"
        exclude = ["slug"]
