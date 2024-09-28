from django import forms
from django.utils.safestring import mark_safe
from django.utils.translation import gettext_lazy as _

from src.apps.media.models import File


class FileForm(forms.ModelForm):
    file = forms.FileField(
        widget=forms.FileInput,
        help_text=_("Select a file to upload.")
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.instance and self.instance.pk and self.instance.file:
            file_url = self.instance.url
            file_link = mark_safe(f'<a href="{file_url}" target="_blank">{file_url}</a>')
            help_text = _("Uploaded file. Download current file: {file_link}").format(file_link=file_link)
            self.fields["file"].help_text = help_text

    class Meta:
        model = File
        fields = "__all__"
