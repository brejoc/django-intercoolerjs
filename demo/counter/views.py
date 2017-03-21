from django.shortcuts import render

from counter.models import Counter


def index(request, template_name="index.html"):
    """\
    The index view, which basically just displays a button and increments
    a counter.
    """
    if request.GET.get('ic-request'):
        counter, created = Counter.objects.get_or_create(pk=1)
        counter.value += 1
        counter.save()
    else:
        counter, created = Counter.objects.get_or_create(pk=1)
        print(counter.value)
    context = dict(
        value=counter.value,
    )
    return render(request, template_name, context=context)
