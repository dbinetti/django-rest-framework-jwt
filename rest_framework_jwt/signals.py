# Django
from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.db.models.signals import pre_delete
from django.db.models.signals import m2m_changed

# Local
from .models import User

from .tasks import get_or_create_account_from_email
from .tasks import update_account_from_user
from .tasks import delete_account_from_user
from .tasks import add_account_roles_from_user_pk_set
from .tasks import remove_account_roles_from_user_pk_set


@receiver(pre_save, sender=User)
def user_pre_save(sender, instance, raw=False, **kwargs):
    if raw:
        return
    account, _ = get_or_create_account_from_email(instance.email)
    instance.id = account['user_id']
    return update_account_from_user(instance)

@receiver(pre_delete, sender=User)
def user_pre_delete(sender, instance, **kwargs):
    return delete_account_from_user(instance)

@receiver(m2m_changed, sender=User.roles.through)
def user_roles_changed(sender, instance, action, reverse, model, pk_set, **kwargs):
    if action == "pre_add":
        return add_account_roles_from_user_pk_set(instance, pk_set)
    if action == "pre_remove":
        return remove_account_roles_from_user_pk_set(instance, pk_set)
    return
