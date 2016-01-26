from django.forms import ModelForm, ModelChoiceField


from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

from property_inquiry.models import propertyInquiry
from property_inventory.models import Property


class PropertyInquiryForm(ModelForm):
    Property = ModelChoiceField(
        queryset=Property.objects.filter(status__contains='Available').exclude(
            structureType__contains='Vacant Lot').exclude(is_active__exact=False).order_by('streetAddress'),
        help_text='Select the property you would like to visit. Your request saved and you will be contacted within 5 business days to schedule the visit. Only "Available" properties with a structure are listed here.',
        label='Property to visit',
    )

    def __init__(self, *args, **kwargs):
        super(PropertyInquiryForm, self).__init__(*args, **kwargs)
        self.fields.keyOrder = [
            'applicant_name', 'applicant_email_address', 'applicant_phone', 'Property']
        self.helper = FormHelper()
        self.helper.form_id = 'propertyInquiryForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.label_class = 'col-lg-3'
        self.helper.field_class = 'col-lg-8'
        self.helper.form_method = 'post'
        self.helper.form_action = ''
        self.helper.add_input(Submit('submit', 'Submit'))

    class Meta:
        model = propertyInquiry
        exclude = ['user', 'showing_scheduled', 'applicant_ip_address']
