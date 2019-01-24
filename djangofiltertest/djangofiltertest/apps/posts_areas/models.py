"""Categories that a post can belong to"""
from django.db import models
from django.utils.translation import ugettext_lazy as _

from djangofiltertest.libs.models import AuditedModel, UUIDPrimaryKey


class PostAreaModel(UUIDPrimaryKey, AuditedModel):
    """
        Model where we will save categories of working areas.
        I.e., when testers have to select in profile which profession they have
        the options will be taken from this app.
    """

    name = models.CharField(max_length=128,db_index=False,verbose_name=_('name'))
    parent = models.ForeignKey(
        'self',
        on_delete=models.CASCADE,
        verbose_name=_("parent category"),
        null=True,
        blank=True,
        related_name="postareas",
        related_query_name="postarea",
        db_index=False,
    )

    class Meta:
        abstract = True
        ordering = ['name', '-parent__id']

    def __str__(self):
        if self.parent:
            return self.parent.name + ' - ' + self.name
        return self.name


class PostArea(PostAreaModel):
    """Concrete model of a posts area or category"""
    class Meta:
        verbose_name = _('post area')
        verbose_name_plural = _('post areas')
    pass
