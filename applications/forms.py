from django import forms
from django.core.urlresolvers import reverse
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit, Layout, Fieldset, ButtonHolder, Div, Button, MultiField, Field, HTML, Div
from crispy_forms.bootstrap import FormActions, InlineRadios, PrependedAppendedText, InlineField
from .models import Application, UploadedFile
from property_inventory.models import Property
from applicants.models import Organization
from django.forms.models import inlineformset_factory
from applicants.widgets import AddAnotherWidgetWrapper
from django.core.exceptions import ValidationError


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


class ApplicationForm(forms.ModelForm):
    Property = forms.ModelChoiceField(
        queryset=Property.objects.exclude(status__contains='Sale approved by MDC').exclude(is_active__exact=False).exclude(
            status__contains='Sold').exclude(status__contains='Sale approved by Board of Directors', renew_owned=True).order_by('streetAddress'),
        help_text='Select the property you are applying for. One property per application.',
        required=False
    )
    organization = forms.ModelChoiceField(
        queryset=Organization.objects.all(),
        widget=AddAnotherWidgetWrapper(
            forms.Select(),
            Organization,
        ),
        help_text='If you are applying on behalf of an organization or another individual please add or select.',
        required=False
    )
    status = forms.IntegerField(
        required=False
    )
    save_for_later = forms.CharField(required=False)

    class Meta:
        model = Application
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        app_id = kwargs.pop('id')
        super(ApplicationForm, self).__init__(*args, **kwargs)
        #self.fields['conflict_board_rc'].required = True
        #self.fields['active_citations'].required = True
        #self.fields['tax_status_of_properties_owned'].required = True
        #self.fields['prior_tax_foreclosure'].required = True
        #self.fields['scope_of_work'].required = False
        #self.fields['proof_of_funds'].required = False
        #self.fields['prior_tax_foreclosure'].required = True
        #self.fields['status'].value = 3
        self.fields['organization'].queryset = Organization.objects.filter(
            user=user).order_by('name')
        self.helper = FormHelper()
        self.helper.form_id = 'ApplicationForm'
        self.helper.form_class = 'form-horizontal'
        self.helper.field_class = 'col-lg-6'
        self.helper.label_class = 'col-lg-4'
        self.helper.render_unmentioned_fields = False
        self.helper.layout = Layout(
            Fieldset(
                'About You',
                Field('conflict_board_rc'),
                Field('conflict_board_rc_name'),
                Field('active_citations'),
                Field('tax_status_of_properties_owned'),
                Field('other_properties_names_owned'),
                Field('prior_tax_foreclosure'),
                Field('organization'),

                css_class='well'
            ),
            Fieldset(
                'Select a property',
                Div('Property'),
                HTML('<div class="form-group"><div class="control-label col-lg-4">Status: </div><div id="status" class="col-lg-6 form-control-static"></div></div>'),
                HTML('<div class="form-group"><div class="control-label col-lg-4">Structure Type: </div><div id="structureType" class="form-control-static col-lg-6"></div></div>'),
                HTML('<div class="form-group"><div class="control-label col-lg-4">Sidelot Eligible: </div><div id="sidelot_eligible" class="form-control-static col-lg-6"></div></div>'),
                HTML('<div class="form-group"><div class="control-label col-lg-4">Price: </div><div id="price" class="form-control-static col-lg-6"></div></div>'),
                HTML('<div class="form-group"><div class="control-label col-lg-4">NSP: </div><div id="nsp_boolean" class="form-control-static col-lg-6"></div></div>'),
                HTML('<div class="form-group"><div class="control-label col-lg-4">Homestead Only: </div><div id="homestead_only" class="form-control-static col-lg-6"></div></div>'),
                HTML('<div id="nsp" class="panel panel-danger" style="display:none"><div class="panel-heading"><h3 class="panel-title">NSP</h3></div><div class="panel-body">This property is a Neighborhood Stabilization Program (NSP) property. NSP properties were originally purchased by the City using special federal funds and thus development of these properties carry additional requirements. You can find out more about these requirements <a href="//www.renewindianapolis.org/nsp-requirements/" target="_blank">here</a>.</div></div>'),
                css_class='well'
            ),
            Fieldset(
                'Application Type',
                Div('application_type'),
                css_class='well'
            ),
            Fieldset(
                'Ownership and Use',
                Field('long_term_ownership'),
                Field('is_rental'),
                Field('nsp_income_qualifier'),
                css_class='standard-app well'
            ),
            Fieldset(
                'Planned Improvements',
                Field('planned_improvements'),
                Field('timeline'),
                css_class='standard-app homestead-app well'
            ),
            Fieldset(
                'Budget and Funding',
                Field(PrependedAppendedText('estimated_cost', '$', '.00')),
                Field('source_of_financing'),
                css_class='standard-app homestead-app well'
            ),
            Fieldset(
                'Sidelot Eligiblity',
                Field('sidelot_eligible'),
                css_class='sidelot-app well'
            ),
            Fieldset(
                'Uploaded Files',
                HTML('<p>Before your application can be submitted for review you must attach both a scope of work and proof of funds, as referenced earlier. You can upload those files here.</p>'),

                HTML('''<p>Previously uploaded files:<ul>
                        {% for file in uploaded_files_all %}
                            <li>{{ file }} <img src="{{STATIC_URL}}admin/img/icon_deletelink.gif" id='uploadedfile_{{ file.id }}' class='uploaded_file_delete' alt='[X]'></img></li>
                            {% empty %}
                                <li>No files are associated with this application.</li>
                        {% endfor%}
                        </ul>
                    </p>'''),
                HTML('<div class="form-group"><div class="control-label col-lg-4">Scope of Work</div><div id="sow-file-uploader" class="form-control-static col-lg-6">Drop your scope of work file here to upload</div>'),
                HTML('<div class="help-block col-lg-6 col-lg-offset-4">We highly recommend using our <a href="http://www.renewindianapolis.org/wp-content/uploads/Example-Scope-of-Work-updated.xls">spreadsheet</a> or <a href="http://www.renewindianapolis.org/wp-content/uploads/Example-Scope-of-Work-updated-printable.pdf">printable template</a> as a starting point.</div></div>'),
                HTML('<div class="form-group"><div class="control-label col-lg-4">Elevation View</div><div id="elevation-file-uploader" class="form-control-static col-lg-6">Drop your elevation view file here to upload</div>'),
                HTML('<div class="help-block col-lg-6 col-lg-offset-4">If you are proposing new construction on a vacant lot you must upload an elevation view of your proposed construction.</div></div>'),
                HTML('<div class="form-group"><div class="control-label col-lg-4">Proof of Funds</div><div id="pof-file-uploader" class="form-control-static col-lg-6">Drop your proof of funds file here to upload</div>'),
                HTML("""<div class="help-block col-lg-6 col-lg-offset-4">
                            Upload documents demonstrating your plan to pay for your proposed improvements as outlined
                            in the "Budgeting and Financing" section. Examples include: a bank statement, a completed
                            and notarized affidavit, pre-approval letter from a lender, etc
                            <ol>
                            <li>Rehabilitation projects, including homes for rental or for sale projects, must
                                show acceptable proof of funds for 75-100% of the total project costs less any
                                materials on hand.  An <a href="http://www.renewindianapolis.org/wp-content/uploads/Affidavit-self.pdf" target="_blank">affidavit of funds</a> (PDF) may be used for up to 25% of the total
                                project costs.</li>
                            <li>All proposed new construction projects require proof of funds for 75% of the
                                total project costs.  An <a href="http://www.renewindianapolis.org/wp-content/uploads/Affidavit-self.pdf" target="_blank">affidavit of funds</a> (PDF) may be used for up to 25% of the total
                                project costs.</li>
                            </ol></div></div>"""
                     ),
                HTML('<p>To delete an uploaded file, click "Save Incomplete Application", then scroll down and click the red "X" after the file name.</p>'),
                css_class='standard-app homestead-app well'
            ),
            FormActions(
                Button('cancel', 'Cancel'),
                Submit('save_for_later', 'Save Incomplete Application'),
                Submit('save', 'Validate and Submit Application'),
            )
        )
        self.helper.form_method = 'post'
        self.helper.form_action = reverse('process_application', kwargs={
                                          'action': 'save', 'id': app_id})

    def validate_for_submission(self, *args, **kwargs):
        app_id = kwargs.pop('id')
        cleaned_data = super(ApplicationForm, self).clean()
        application_type = cleaned_data.get('application_type', None)
        conflict_board_rc = cleaned_data.get('conflict_board_rc', None)
        conflict_board_rc_name = cleaned_data.get(
            'conflict_board_rc_name', None)
        tax_status_of_properties_owned = cleaned_data.get(
            'tax_status_of_properties_owned', None)
        prior_tax_foreclosure = cleaned_data.get('prior_tax_foreclosure', None)
        active_citations = cleaned_data.get('active_citations', None)

        planned_improvements = cleaned_data.get('planned_improvements')
        timeline = cleaned_data.get('timeline')
        estimated_cost = cleaned_data.get('estimated_cost')
        source_of_financing = cleaned_data.get('source_of_financing')

        long_term_ownership = cleaned_data.get('long_term_ownership')
        is_rental = cleaned_data.get('is_rental')
        nsp_income_qualifier = cleaned_data.get('nsp_income_qualifier')
        property_selected = cleaned_data.get('Property')
        proof_of_funds = cleaned_data.get('proof_of_funds')
        sidelot_eligible = cleaned_data.get('sidelot_eligible', None)

        if conflict_board_rc is None:
            self.add_error("conflict_board_rc", ValidationError(
                'This is a required question.'))

        if conflict_board_rc is True and conflict_board_rc_name == '':
            self.add_error("conflict_board_rc_name", ValidationError(
                "You anwsered Yes above, please provide a name."))

        if tax_status_of_properties_owned is None:
            self.add_error('tax_status_of_properties_owned',
                           ValidationError('This is a required question.'))

        if tax_status_of_properties_owned == Application.DELINQUENT_STATUS:
            self.add_error('tax_status_of_properties_owned', ValidationError(
                "Delinquent tax payers are not eligible to purchase properties from Renew Indianapolis"))

        if active_citations is None:
            self.add_error('active_citations', ValidationError(
                "This is a required question"))

        if prior_tax_foreclosure is None or prior_tax_foreclosure is True:
            self.add_error('prior_tax_foreclosure', ValidationError(
                "If you have previously lost a property in a tax foreclosure in Marion County you are not eligible to purchase properties from Renew Indianapolis."))

        if property_selected is None or property_selected == "":
            self.add_error('Property', ValidationError(
                "You must select a property"))

        if Application.SIDELOT == application_type:
            msg = "This is a required question."
            if not sidelot_eligible:
                self.add_error('sidelot_eligible', ValidationError(msg))
            if property_selected is not None and property_selected.structureType != "Vacant Lot":
                self.add_error('application_type', ValidationError(
                    'The property you have selected is not a vacant lot and hence is ineligible for our sidelot program.'))

        if Application.HOMESTEAD == application_type or Application.STANDARD == application_type:
            msg = "This is a required field."
            if not planned_improvements or planned_improvements == "":
                self.add_error('planned_improvements', ValidationError(msg))
            if not timeline or timeline == "":
                self.add_error('timeline', ValidationError(msg))
            if not estimated_cost or estimated_cost == 0:
                self.add_error('estimated_cost', ValidationError(msg))
            if not source_of_financing or source_of_financing == "":
                self.add_error('source_of_financing', ValidationError(msg))
            if UploadedFile.objects.filter(file_purpose__exact=UploadedFile.PURPOSE_SOW).filter(application__exact=app_id).count() == 0:
                self.add_error(None, ValidationError(
                    'You must upload a separate scope of work document with your application'))
            if UploadedFile.objects.filter(file_purpose__exact=UploadedFile.PURPOSE_POF).filter(application__exact=app_id).count() == 0:
                self.add_error(None, ValidationError(
                    'You must upload a separate proof of funds document with your application'))

            if Application.STANDARD == application_type:
                if not long_term_ownership or long_term_ownership == "":
                    self.add_error('long_term_ownership', ValidationError(msg))
                if is_rental is None:  # boolean value
                    self.add_error('is_rental', ValidationError(msg))
                if not nsp_income_qualifier and property_selected.nsp and nsp_income_qualifier == "":
                    self.add_error('nsp_income_qualifier', ValidationError(
                        "Since this is a rental NSP property you must list who will be conducting tenant income qualification."))
                if property_selected is not None and property_selected.homestead_only:
                    self.add_error('application_type', ValidationError(
                        'The property you have selected is marked "homestead only" but you indicated a Standard application.'))

        return len(self.errors) == 0


# class ApplicationFormTemplate(forms.ModelForm):
#     def __init__(self, *args, **kwargs):
#         super(ApplicationFormTemplate, self).__init__(*args, **kwargs)
#         self.helper = FormHelper()
#         self.helper.form_tag = False
#         self.helper.form_class = 'form-horizontal'
#         self.helper.field_class = 'col-lg-6'
#         self.helper.label_class = 'col-lg-4'
#         self.helper.render_unmentioned_fields = True
#
#
# class ApplicationForm0(ApplicationFormTemplate):
#     class Meta:
#         model = Application
#         fields = ('organization','conflict_board_rc','conflict_board_rc_name','active_citations','tax_status_of_properties_owned','other_properties_names_owned','prior_tax_foreclosure')
#
#     # def __init__(self, *args, **kwargs):
#     #     super(ApplicationFormTemplate, self).__init__()
#     #     self.helper.layout = Layout(
#     #         Fieldset(
#     #             'About You',
#     #             Field('organization'),
#     #             Field('conflict_board_rc'),
#     #             Field('conflict_board_rc_name'),
#     #             Field('active_citations'),
#     #             Field('tax_status_of_properties_owned'),
#     #             Field('other_properties_names_owned'),
#     #             Field('prior_tax_foreclosure'),
#     #             css_class='well'
#     #         )
#     #     )
#
#     def clean(self):
#         cleaned_data = super(ApplicationForm0, self).clean()
#         conflict_board_rc = cleaned_data.get('conflict_board_rc')
#         conflict_board_rc_name = cleaned_data.get('conflict_board_rc_name')
#         tax_status_of_properties_owned = cleaned_data.get('tax_status_of_properties_owned')
#         prior_tax_foreclosure = cleaned_data.get('prior_tax_foreclosure')
#         active_citations = cleaned_data.get('active_citations')
#         print "conflict_board_rc_name",conflict_board_rc_name
#         print "conflict_board_rc",conflict_board_rc,"."
#         print type(conflict_board_rc)
#
#         if conflict_board_rc is None:
#             self.add_error('conflict_board_rc',"This is a required question.")
#
#         if conflict_board_rc is True and conflict_board_rc_name is None:
#             self.add_error('conflict_board_rc_name',"You anwsered Yes above, please provide a name.")
#
#         if tax_status_of_properties_owned == Application.DELINQUENT_STATUS:
#             self.add_error('tax_status_of_properties_owned',"Delinquent tax payers are not eligible to purchase properties from Renew Indianapolis")
#
#         if active_citations is None or active_citations is True:
#             # Active citations are not an automatic disqualication so we don't throw an error.
#             #self.add_error('active_citations',"Fix ur stuff")
#             pass
#
#         if prior_tax_foreclosure is None or prior_tax_foreclosure is True:
#             self.add_error('prior_tax_foreclosure', "If you have previously lost a property in a tax foreclosure in Marion County you are not eligible to purchase properties from Renew Indianapolis.")
#
#
#
#
# class ApplicationForm1(forms.ModelForm):
#     class Meta:
#         model = Application
#         fields = ('Property','application_type')
#
#     # def __init__(self, *args, **kwargs):
#     #     ApplicationFormTemplate.__init__(ApplicationFormTemplate)
#     #     self.helper.layout = Layout(
#     #         Fieldset(
#     #             'Select a Property',
#     #             Field('Property'),
#     #             Field('application_type'),
#     #             css_class='well'
#     #         )
#     #     )
#
# class ApplicationForm2(forms.ModelForm):
#     class Meta:
#         model = Application
#         fields = ('long_term_ownership','is_rental','nsp_income_qualifier')
#
#     def clean(self):
#         cleaned_data = super(ApplicationForm2, self).clean()
#         is_rental = cleaned_data.get('is_rental')
#         if is_rental is True and nsp_income_qualifier is None:
#             self.add_error('nsp_income_qualifier', 'This')
#
# class ApplicationForm2_1(forms.ModelForm):
#     class Meta:
#         model = Application
#         fields = ('nsp_income_qualifier',)
#
# class ApplicationForm3(forms.ModelForm):
# 	class Meta:
# 		model = Application
# 		fields = ('planned_improvements','scope_of_work','timeline','team_members')
#
# class ApplicationForm4(forms.ModelForm):
# 	class Meta:
# 		model = Application
# 		fields = ('source_of_financing', 'proof_of_funds', 'grant_funds')
#
# class ApplicationForm5(forms.ModelForm):
# 	class Meta:
# 		model = Application
# 		fields = ('sidelot_eligible',)
