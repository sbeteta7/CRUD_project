from django import forms

from appAdmin.models import Project


class CreateNewTask(forms.Form):
    title = forms.CharField(label="Titulo de tarea", max_length=200,widget=forms.TextInput(attrs={'class':'input'}))
    description=forms.CharField(label="descripcion de la tarea", widget=forms.Textarea(attrs={'class':'input'}))

    project = forms.ModelChoiceField(
        label="Proyecto",
        queryset=Project.objects.all(),
        widget=forms.Select(attrs={'class': 'input'})
    )

class CreateNewProject(forms.Form):
    name = forms.CharField(label="Nombre del proyecto",max_length=200,widget=forms.TextInput(attrs={'class':'input'}))

