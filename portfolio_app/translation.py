# /home/siisi/portfolio/portfolio_app/translation.py

from modeltranslation.translator import translator, TranslationOptions
from .models import Project, ContactMessage


class ProjectTR(TranslationOptions):
    fields = ('title', 'description',)


class ContactMessageTR(TranslationOptions):
    fields = ('subject', 'message',)


translator.register(Project, ProjectTR)
translator.register(ContactMessage, ContactMessageTR)
