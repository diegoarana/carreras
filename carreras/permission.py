from functools import wraps
from django.core.exceptions import PermissionDenied, ObjectDoesNotExist

def is_owner_permission_required(model, pk_name='pk'):
    def decorator(view_func):
        def wrap(request, *args, **kwargs):
            pk = kwargs.get(pk_name, None)
            if pk is None:
                raise RuntimeError('decorator requires pk argument to be set (got {} instead)'.format(kwargs))
            is_owner_func = getattr(model, 'is_owner', None)
            if is_owner_func is None:
                raise RuntimeError('decorator requires model {} to provide is_owner function)'.format(model))
            o=model.objects.get(pk=pk) #raises ObjectDoesNotExist
            if o.is_owner(request.user):
                return view_func(request, *args, **kwargs)
            else:
                raise PermissionDenied
        return wraps(view_func)(wrap)
    return decorator