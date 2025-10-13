from .models import Core
from staff.models import Staff

def core_context(request):
    core = None
    try:
        core = Core.objects.only('official_name').first()
    except Core.DoesNotExist:
        core = None

    return {"core":core}    

def staff_context(request):
    staff = None
    try:
        staff = Staff.objects.only('admin').filter(admin=True)
    except Staff.DoesNotExist:
        staff = None

    return {"is_staff":staff}