from .forms import CommentForm
from django.shortcuts import render, get_object_or_404, redirect
from .models import Project, Issue, Comment
from .forms import IssueForm
from .forms import ProjectForm, CommentForm
from django.views.decorators.http import require_POST
from django.contrib import messages


def create_project(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('project_list')
    else:
        form = ProjectForm()
    return render(request, 'project_form.html', {'form': form})


def project_list(request):
    projects = Project.objects.all()
    return render(request, 'project_list.html', {'projects': projects})


def project_detail(request, pk):
    project = get_object_or_404(Project, pk=pk)
    issues = project.issues.all()
    return render(request, 'project_detail.html', {'project': project, 'issues': issues})


def issue_detail(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    return render(request, 'issue_detail.html', {'issue': issue})


def create_issue(request, pk):
    project = get_object_or_404(Project, pk=pk)
    if request.method == 'POST':
        form = IssueForm(request.POST)
        if form.is_valid():
            issue = form.save(commit=False)
            issue.project = project
            issue.created_by = request.user
            issue.save()
            return redirect('project_detail', pk=project.pk)
    else:
        form = IssueForm()
    return render(request, 'issue_form.html', {'form': form, 'project': project})


def issue_detail(request, pk):
    issue = get_object_or_404(Issue, pk=pk)
    comments = issue.comments.all()

    if request.method == 'POST':
        comment_form = CommentForm(request.POST)
        if comment_form.is_valid():
            comment = comment_form.save(commit=False)
            comment.issue = issue
            comment.author = request.user
            comment.save()
            return redirect('issue_detail', pk=issue.pk)
    else:
        comment_form = CommentForm()

    return render(request, 'issue_detail.html', {
        'issue': issue,
        'comments': comments,
        'comment_form': comment_form,
    }
    )


def landing(request):
    return render(request, 'landing.html')


@require_POST
def toggle_issue(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    issue.is_completed = not issue.is_completed
    issue.save()
    msg = "Marked complete" if issue.is_completed else "Marked incomplete"
    messages.success(request, f"Issue '{issue.title}' {msg}.")
    return redirect('issue_detail', pk=issue.id)


@require_POST
def delete_issue(request, issue_id):
    issue = get_object_or_404(Issue, id=issue_id)
    title = issue.title
    issue.delete()
    messages.success(request, f"Issue '{title}' deleted.")
    # Or wherever you want to go after deleting
    return redirect('project_list')
