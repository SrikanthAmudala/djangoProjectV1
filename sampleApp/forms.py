from django import forms

from sampleApp.models import Task


class CreateBlogPostForm(forms.ModelForm):
    class Meta:
        model = Task
        # fields = "__all__"

        fields = ['title', 'desc', 'status', 'taskDueDate']


class UpdateBlogPostForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'desc', 'status', 'taskDueDate']

    def save(self, commit=True):
        todo = self.instance
        todo.title = self.cleaned_data['title']
        todo.desc = self.cleaned_data['desc']
        todo.status = self.cleaned_data['status']
        todo.taskDueDate = self.cleaned_data['taskDueDate']

        if commit:
            todo.save()
        return todo
