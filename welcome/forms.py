from django import forms
from .models import TeamMember, TeamName


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


class TeamForm(forms.ModelForm):
    class Meta:
        model = TeamName
        fields = ['team']


class TeamUpdateForm(forms.ModelForm):
    delete = forms.BooleanField(required=False)

    class Meta:
        model = TeamName
        fields = ['team', 'delete']
