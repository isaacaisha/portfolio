# /home/siisi/portfolio/portfolio_app/views.py

from django.shortcuts         import render, redirect
from django.core.mail         import send_mail
from django.contrib           import messages
from django.conf              import settings
from django.utils.translation import gettext as _
from django.utils             import timezone
from .models                  import Project, ContactMessage
from .forms                   import ProjectForm, ContactForm


def index(request):
    projects = Project.objects.all().order_by('id')
    date_str = timezone.now().strftime(_("%a %d %B %Y"))

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            
            # 1) send the email
            send_mail(
                subject       = f"[Portfolio Contact] {cd['subject']}",
                message       = (
                    f"From: {cd['name']} <{cd['email']}>\n"
                    f"Phone: {cd.get('phone','– not provided –')}\n\n"
                    f"{cd['message']}"
                ),
                from_email     = settings.DEFAULT_FROM_EMAIL,
                recipient_list = [settings.DEFAULT_FROM_EMAIL],
                fail_silently  = False,
            )

            # 2) persist it
            ContactMessage.objects.create(
                name    = cd['name'],
                email   = cd['email'],
                phone   = cd.get('phone',''),
                subject = cd['subject'],
                message = cd['message']
            )

            messages.success(request, _("Thanks! Your message has been sent."))
            return redirect("index")

        else:
            # push a general error message
            messages.warning(request, _("Please correct the errors below and try again."))
            # DO NOT re-create form; keep the bound form with errors

    else:
        form = ContactForm()

    return render(request, "index.html", {
        "projects": projects,
        "form":     form,
        "date":     date_str,
    })
    

def admin_proxy(request):
    """
    Redirect normal users away from /admin/ with an error message,
    but let superusers through to the real admin at /superadmin/.
    """
    if not request.user.is_superuser:
        messages.warning(request, _("Access denied: you must be a superuser to view the admin panel."))
        return redirect('index')

    # superuser → forward them to the real admin
    return redirect('admin:index')  # this reverse-resolves to /superadmin/ by default


def project_create(request):
    # Deny non-superusers
    if not request.user.is_authenticated or not request.user.is_superuser:
        messages.warning(request, _("Access denied: you must be a superuser to add projects."))
        return redirect('index')

    if request.method == 'POST':
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, _("Project created successfully!"))
            return redirect('index')
    else:
        form = ProjectForm()

    return render(request, 'project_form.html', {
        'form': form,
        'date': timezone.now().strftime(_("%a %d %B %Y"))
    })


def notifications(request):
    """
    List all ContactMessage entries for superusers.
    """
    if not request.user.is_superuser:
        messages.warning(request, _("Access denied: you must be a superuser to view notifications."))
        return redirect('index')

    msgs = ContactMessage.objects.order_by('-sent_at')
    return render(request, 'notifications.html', {
        'messages_list': msgs,
        'date': timezone.now().strftime(_("%a %d %B %Y"))
    })
