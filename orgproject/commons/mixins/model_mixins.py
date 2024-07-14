from rest_framework import mixins


class SafeDeleteModelMixin(mixins.DestroyModelMixin):

    def perform_destroy(self, instance):
        if hasattr(instance, 'is_deleted'):
            instance.is_deleted = True
            update_fields = ['is_deleted']
            if hasattr(instance, 'updated_at'):
                update_fields += ['updated_at']
            instance.save(update_fields=update_fields)
        else:
            raise AttributeError("`is_deleted` field not found. Make sure you are using "
                                 "SafeDeleteAbstractModel")
