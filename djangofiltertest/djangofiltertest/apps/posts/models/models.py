"""Models representing posts, now only jobs"""
from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.postgres.indexes import BrinIndex

from djangofiltertest.libs.models import (
    AuditedModel,
    UUIDPrimaryKey,
    PersistentModel,
    PersistentModelManager,
    PersistentModelQuerySet
)
from djangofiltertest.libs.helpers import slug_generator

class PostModel(UUIDPrimaryKey, AuditedModel):
    """
        Abstract model with basic info of a post
    """
    title = models.CharField(max_length=128, db_index=True, verbose_name=_("name"))
    email = models.EmailField(verbose_name=_("email"))
    post_category = models.ForeignKey(
        "posts_areas.PostArea",
        on_delete=models.SET_NULL,
        verbose_name=_("post category"),
        null=True,
        blank=True,
        related_name="+",
        db_index=False,
    )  # related_name with + --> no backward relations
    post_subcategory = models.ForeignKey(
        "posts_areas.PostArea",
        on_delete=models.SET_NULL,
        verbose_name=_("post sub category"),
        null=True,
        blank=True,
        related_name="+",
        db_index=False,
    )

    date_start = models.DateTimeField(_("start date"))
    date_end = models.DateTimeField(_("end date"))

    number = models.PositiveSmallIntegerField(_("amount to pay"))
    slug = models.SlugField(verbose_name=_("slug"), max_length=151)

    class Meta:
        abstract = True
        get_latest_by = ["created_at", "updated_at"]

    def __str__(self):
        return self.title

    def clean(self, *args, **kwargs):
        # Strip whitespaces
        fields = [
            "email",
        ]
        for field in fields:
            value = getattr(self, field, None)
            if value:
                setattr(self, field, value.strip())
        # check that start date its before end date
        if self.date_end and self.date_start and self.date_end <= self.date_start:
            raise ValidationError(_("Start date should be before end date"))
        # If user selected both categories, check that the parent is the correct
        # If only subcategory selected, fill the right parent.
        # If only category, do nothing.
        if self.post_subcategory:
            if self.post_category and self.post_subcategory.parent != self.post_category:
                raise ValidationError(_("Choosen categories does not match"))
            else:
                self.post_category = self.post_subcategory.parent


    def save(self, *args, **kwargs):
        """Override django save method of a post"""
        if not self.title:
            raise ValidationError({
                'title': ValidationError(_('Missing title.'), code='required'),
            })
        self.slug = slug_generator(self)
        self.full_clean()
        super(PostModel, self).save(*args, **kwargs)

    # This will come from the urls.py
    def get_absolute_url(self):
        """Return absolute url for a post element"""
        return reverse("v1:posts", kwargs={"slug": self.slug})


class Job(PostModel, PersistentModel):
    """
        Proposals of jobs. This model represents a company posting a job  that
        needs to be done, a product to be tested.
    """

    class Meta:
        verbose_name = _("job")
        verbose_name_plural = _("jobs")

    def get_absolute_url(self):
        """Return absolute url for a job element"""
        return reverse("v1:posts-job-detail", kwargs={"slug": self.slug})

