# /home/siisi/portfolio/portfolio_app/models.py

from django.db import models
from django.db.models import JSONField
from django.utils.translation import get_language


class Project(models.Model):
    title       = models.CharField(max_length=100)
    slug        = models.SlugField(
        unique=True,
        help_text="Used for modal_id, e.g. 'portfolioModal1'"
    )
    thumbnail   = models.CharField(
        max_length=200,
        help_text="Static path: 'assets/img/portfolio/...jpg'"
    )
    image       = models.CharField(
        max_length=200,
        help_text="Static path for modal image"
    )
    description = models.TextField(
        help_text="Short blurb under the title"
    )
    # Store features per language in a JSON field: {"en": [...], "es": [...], ...}
    features    = JSONField(
        default=dict,
        blank=True,
        help_text="Mapping of language codes to feature lists"
    )
    url         = models.URLField(
        max_length=300,
        blank=True,
        help_text="Full external URL for the 'See Project' button"
    )

    def modal_id(self):
        return self.slug

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        # Handy if you link directly to the modal
        return f"#{self.modal_id()}"

    @property
    def localized_features(self):
        """
        Return features list for current language,
        falling back to English if not available.
        """
        lang = get_language()[:2]
        return self.features.get(lang) or self.features.get('en', [])


class ContactMessage(models.Model):
    name      = models.CharField(max_length=100)
    email     = models.EmailField()
    phone     = models.CharField(max_length=20, blank=True)
    subject   = models.CharField(max_length=150)
    message   = models.TextField()
    sent_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.subject} from {self.name}"
        