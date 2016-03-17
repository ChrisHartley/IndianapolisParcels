from django import forms
from .models import UploadedFile
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, Div, Button, MultiField, Field, HTML
from crispy_forms.bootstrap import FormActions

class UploadedFileForm(forms.ModelForm):

    class Meta:
        model = UploadedFile
        exclude = []

    def __init__(self, *args, **kwargs):
        super(UploadedFileForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_id = 'UploadedFileForm'
        self.helper.form_class = 'form-inline'
        #self.helper.field_class = 'col-lg-6'
        #self.helper.label_class = 'col-lg-4'
        self.helper.form_tag = False
        self.helper.field_template = 'bootstrap3/layout/inline_field.html'
        self.helper.render_unmentioned_fields = False
        self.helper.layout = Layout(
            Fieldset(
                'Supporting Documents',
                InlineField('supporting_document'),
                InlineField('file_purpose'),
                InlineField('file_purpose_other_explanation'),
                css_class='well'
            )
        )
