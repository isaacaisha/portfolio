# /home/siisi/portfolio/portfolio_app/forms.py

from django import forms
from .models import Project


class ProjectForm(forms.ModelForm):
    # override features to accept a comma-separated string
    features_csv = forms.CharField(
        required=False,
        widget=forms.Textarea(attrs={'rows': 3}),
        help_text="Enter each feature separated by commas."
    )

    class Meta:
        model = Project
        fields = ['title', 'slug', 'thumbnail', 'image', 'description', 'url']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Prepopulate features_csv when editing
        if self.instance and self.instance.pk:
            self.fields['features_csv'].initial = ', '.join(self.instance.features)

    def save(self, commit=True):
        instance = super().save(commit=False)
        # split CSV into list
        csv = self.cleaned_data.get('features_csv', '')
        instance.features = [f.strip() for f in csv.split(',') if f.strip()]
        if commit:
            instance.save()
        return instance
        

class ContactForm(forms.Form):
    name    = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Your name"
        })
    )
    email   = forms.EmailField(
        widget=forms.EmailInput(attrs={
            "class": "form-control",
            "placeholder": "you@example.com"
        })
    )
    phone   = forms.CharField(
        max_length=20,
        required=False,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "(123) 456-7890"
        })
    )
    subject = forms.CharField(
        max_length=150,
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Subject"
        })
    )
    message = forms.CharField(
        widget=forms.Textarea(attrs={
            "class": "form-control",
            "rows": 6,
            "placeholder": "Your message..."
        })
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for name, field in self.fields.items():
            classes = field.widget.attrs.get("class", "")
            # always add form-control
            classes = (classes + " form-control").strip()

            # if this field has errors (i.e. after binding a POST with invalid data),
            # add the Bootstrap invalid class
            if self.errors.get(name):
                classes += " is-invalid"

            field.widget.attrs["class"] = classes
            