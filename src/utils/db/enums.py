# from django.db import models
# from django.utils.translation import gettext_lazy as _

#
# class CreateabilityLevel(models.IntegerChoices):
#     CUSTOM = 0, _("CUSTOM")
#     VISIBLE_FOR_SUPERUSERS = 1, _("VISIBLE FOR SUPERUSERS")
#     VISIBLE_FOR_ADMINS = 2, _("VISIBLE FOR ADMINS")
#     VISIBLE_FOR_OWNERS = 3, _("VISIBLE FOR OWNERS")
#     VISIBLE_FOR_EVERYONE = 4, _("VISIBLE FOR EVERYONE")
#
#
# class VisibilityLevel(models.IntegerChoices):
#     CUSTOM = 0, _("CUSTOM")
#     VISIBLE_FOR_SUPERUSERS = 1, _("VISIBLE FOR SUPERUSERS")
#     VISIBLE_FOR_ADMINS = 2, _("VISIBLE FOR ADMINS")
#     VISIBLE_FOR_OWNERS = 3, _("VISIBLE FOR OWNERS")
#     VISIBLE_FOR_EVERYONE = 4, _("VISIBLE FOR EVERYONE")
#
#
# class ChangebilityLevel(models.IntegerChoices):
#     CUSTOM = 0, _("CUSTOM")
#     CHANGEABLE_BY_SUPERUSERS = 1, _("CHANGEABLE BY SUPERUSERS")
#     CHANGEABLE_BY_ADMINS = 2, _("CHANGEABLE BY ADMINS")
#     CHANGEABLE_BY_OWNERS = 3, _("CHANGEABLE BY OWNERS")
#
#
# class DeletebilityLevel(models.IntegerChoices):
#     CUSTOM = 0, _("CUSTOM")
#     CHANGEABLE_BY_SUPERUSERS = 1, _("CHANGEABLE BY SUPERUSERS")
#     CHANGEABLE_BY_ADMINS = 2, _("CHANGEABLE BY ADMINS")
#     CHANGEABLE_BY_OWNERS = 3, _("CHANGEABLE BY OWNERS")
#
#
# class ObjectPermission(models.Model):
#     createbility_level = models.IntegerField(choices=CreateabilityLevel)
#     visibility_level = models.IntegerField(choices=VisibilityLevel)
#     changebility_level = models.IntegerField(choices=ChangebilityLevel)
#     deleteability_level = models.IntegerField(choices=DeletebilityLevel)
