from django.shortcuts import render, get_object_or_404, redirect
from .models import TeamMember, Location, TeamName
from .forms import MemberForm, MemberUpdateForm, TeamForm, TeamUpdateForm
from django.contrib import messages
from datetime import datetime


def welcome(request):
    # get all locations
    all_teams = TeamName.objects.all()

    # get all team members
    all_members = TeamMember.objects.all()

    # check if there are any teams in the database
    teams_exist = all_teams.exists()

    # filter out managers from the list of all members
    members = [member for member in all_members if member.role == 'Member']

    # pass both members and locations to the template
    return render(request, 'pages/landing.html', {
        'members': members, 'all_teams': all_teams, 'teams_exist': teams_exist})


# using form for member creation w/ form validation
def new_member(request):
    if request.method == 'POST':
        form = MemberForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('welcome')
    else:
        form = MemberForm()
    return render(request, 'pages/new_team.html', {'form': form, 'heading': 'Create New Member'})


# using form for team creation w/ form validation
def new_team(request):
    if request.method == 'POST':
        form = TeamForm(request.POST)
        if form.is_valid():
            # Process the form data
            form.save()
            return redirect('welcome')
    else:
        form = TeamForm()
    return render(request, 'pages/new_team.html', {'form': form, 'heading': 'Create New Team'})


# view members details. Denies ability to view manager details.
def member_details(request, member_id):
    member = get_object_or_404(TeamMember, pk=member_id)
    # check if the member is a manager
    if member.role == 'Manager':
        # redirect users to the landing page
        return redirect('welcome')
    else:
        return render(request, 'pages/member_details.html', {'member': member})


# view for list of individual teams incl. manager/s of team.
def view_team(request, team_id):
    all_teams = TeamName.objects.all()
    selected_team = get_object_or_404(TeamName, pk=team_id)
    all_members = selected_team.teammember_set.all()  # retrieve all members associated with the selected team
    context = {
        'all_teams': all_teams,
        'selected_team': selected_team,
        'all_members': all_members
    }
    return render(request, 'pages/view_team.html', context)


# update a member and details via form w/ delete option
def member_update(request, member_id):
    # retrieve the member object
    member = get_object_or_404(TeamMember, pk=member_id)

    if request.method == 'POST':
        # bind the form with the data from the POST request
        form = MemberUpdateForm(request.POST, instance=member)
        if form.is_valid():
            if form.cleaned_data['delete']:
                member.delete()
                return redirect('welcome')
            form.save()
            return redirect('member_details', member_id=member_id)
    else:
        form = MemberUpdateForm(instance=member)
    # render the template with the form
    return render(request, 'pages/member_update.html', {'form': form})


def team_update(request, team_id):
    team = get_object_or_404(TeamName, pk=team_id)
    if request.method == 'POST':
        form = TeamUpdateForm(request.POST, instance=team)
        if form.is_valid():
            if form.cleaned_data['delete']:
                team.delete()
                return redirect('welcome')
            form.save()
            return redirect('view_team', team_id=team_id)
    else:
        form = TeamUpdateForm(instance=team)
    return render(request, 'pages/update_team.html', {'selected_team': team, 'form': form})


def locations(request):
    all_locations = Location.objects.all()
    return render(request, 'pages/locations.html', {'all_locations': all_locations})


def teams(request):
    all_teams = TeamName.objects.all()
    return render(request, 'pages/view_team.html', {'all_teams': all_teams})
