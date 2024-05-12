from django import forms
from .models import TeamMember, TeamName


# Creation of new members with teams and locations
class MemberForm(forms.ModelForm):
    class Meta:
        model = TeamMember
        fields = ['name', 'role', 'location', 'team', 'start_date']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super(MemberForm, self).__init__(*args, **kwargs)
        self.fields['role'].choices = [('Member', 'Member')]


# Update of current members accessed through member_details
class MemberUpdateForm(forms.ModelForm):
    delete = forms.BooleanField(required=False)

    class Meta:
        model = TeamMember
        fields = ['name', 'role', 'location', 'team', 'start_date', 'delete']
        widgets = {
            'start_date': forms.DateInput(attrs={'type': 'date'}, format='%Y-%m-%d'),
        }

    def __init__(self, *args, **kwargs):
        super(MemberUpdateForm, self).__init__(*args, **kwargs)
        self.fields['role'].choices = [('Member', 'Member')]


# Simple form to add a team (empty)
class TeamForm(forms.ModelForm):
    class Meta:
        model = TeamName
        fields = ['team']


# To change name of current team
class TeamUpdateForm(forms.ModelForm):
    delete = forms.BooleanField(required=False)

    class Meta:
        model = TeamName
        fields = ['team', 'delete']
