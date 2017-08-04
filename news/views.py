from django.shortcuts import render, get_object_or_404
from news.models import Subject, Post, Thread
from django.shortcuts import redirect
from django.contrib import messages, auth
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.template.context_processors import csrf
from .forms import StoryForm, PostForm, SubjectForm
from django.forms import formset_factory
from polls.forms import PollSubjectForm, PollForm
from polls.models import PollSubject
from home.models import Team, Player, User

teams = Team.objects.all()


@login_required()
def new_subject(request):
    if request.method == "POST":
        form = SubjectForm(request.POST)
        if form.is_valid():
            subject = form.save(commit=False)
            subject.save()

            messages.success(request, "You have added a new News Subject!")

            return redirect(news)
    else:
        form = SubjectForm()
    return render(request, 'form.html', {'form': form,
                                         'heading_text': 'Create new News Subject',
                                         'form_action': reverse('forum'),
                                         'button_text': 'Save Subject',
                                         'teams': teams})

# need edit subject
# def edit_subjecy(request, subject.id)
# need delete subject


@login_required
def new_story(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    poll_subject_formset = formset_factory(PollSubjectForm, extra=3)
    if request.method == "POST":
        thread_form = StoryForm(request.POST)
        post_form = PostForm(request.POST, request.FILES)
        poll_form = PollForm(request.POST)
        poll_subject_formset = poll_subject_formset(request.POST)
        if thread_form.is_valid() and post_form.is_valid():
            if request.POST.get('is_a_poll', None) and poll_form.is_valid() and poll_subject_formset.is_valid():

                thread = thread_form.save(commit=False)
                thread.subject = subject
                thread.user = request.user
                thread.save()

                post = post_form.save(commit=False)
                post.user = request.user
                post.thread = thread
                post.save()

                poll = poll_form.save(commit=False)
                poll.thread = thread
                poll.save()

                for subject_form in poll_subject_formset:
                    subject = subject_form.save(commit=False)
                    subject.poll = poll
                    subject.save()

                messages.success(request, "You have created a new thread with a poll!")

                return redirect(reverse('story', args={thread.pk}))

            else:

                thread = thread_form.save(commit=False)
                thread.subject = subject
                thread.user = request.user
                thread.save()

                post = post_form.save(commit=False)
                post.user = request.user
                post.thread = thread
                post.save()

                messages.success(request, "You have created a new thread!")

                return redirect(reverse('story', args={thread.pk}))
    else:
        thread_form = StoryForm()
        post_form = PostForm()
        poll_form = PollForm()
        poll_subject_formset = poll_subject_formset()

    args = {
        'thread_form': thread_form,
        'heading_text': 'Start new Story',
        'post_form': post_form,
        'subject': subject,
        'poll_form': poll_form,
        'poll_subject_formset': poll_subject_formset,
        'teams': teams
    }

    args.update(csrf(request))

    return render(request, 'news/thread_form.html', args)

# need edit story and delete story functions


def news(request):
    return render(request, 'news/news.html', {'subjects': Subject.objects.all().order_by('team'),
                                              'teams': teams})


def subject(request, subject_id):
    subject = get_object_or_404(Subject, pk=subject_id)
    return render(request, 'news/subject.html', {'subject': subject,
                                                 'users': User.objects.all(),
                                                 'teams': teams})


def story(request, thread_id):
    thread_ = get_object_or_404(Thread, pk=thread_id)
    args = {'thread': thread_,
            'teams': teams}
    args.update(csrf(request))
    return render(request, 'news/story.html', args)


@login_required
def new_post(request, thread_id):
    thread = get_object_or_404(Thread, pk=thread_id)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.thread = thread
            post.user = request.user
            post.save()

            messages.success(request, "Your post has been added to the thread!")

            return redirect(reverse('story', args={thread.pk}))
    else:
        form = PostForm()

    args = {
        'form': form,
        'heading_text': 'Add Post',
        'form_action': reverse('new_post', args={thread.id}),
        'button_text': 'Make Post',
        'teams': Team.objects.all().order_by("-name")
    }
    args.update(csrf(request))

    return render(request, 'form.html', args)


@login_required
def edit_post(request, thread_id, post_id):
    thread = get_object_or_404(Thread, pk=thread_id)
    post = get_object_or_404(Post, pk=post_id)

    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            messages.success(request, "You have updated your Post!")

            return redirect(reverse('story', args={thread.pk}))
    else:
        form = PostForm(instance=post)

    args = {
        'form': form,
        'heading_text': 'Edit Post',
        'form_action': reverse('edit_post', kwargs={"thread_id": thread.id, "post_id": post.id}),
        'button_text': 'Update Post',
        'teams': Team.objects.all().order_by("-name")
    }
    args.update(csrf(request))

    return render(request, 'form.html', args)


@login_required
def delete_post(request, thread_id, post_id):
    post = get_object_or_404(Post, pk=post_id)
    thread_id = post.thread.id
    post.delete()
    # need are you sure you want to delete see team delete in home.views for ideas
    messages.success(request, "Your post was deleted!")

    return redirect(reverse('story', args={thread_id}))


@login_required
def thread_vote(request, thread_id, subject_id):
    thread = Thread.objects.get(id=thread_id)

    subject = thread.poll.votes.filter(user=request.user)

    if subject:
        messages.error(request, "You already voted on this! You're not trying to cheat are you?")
        return redirect(reverse('story', args={thread_id}))

    subject = PollSubject.objects.get(id=subject_id)

    subject.votes.create(poll=subject.poll, user=request.user)

    messages.success(request, "We've registered your vote!")

    return redirect(reverse('story', args={thread_id}))