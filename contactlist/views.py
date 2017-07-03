from django.shortcuts import render
from contactlist.models import Contact
from contactlist.serializers import ContactSerializer
from rest_framework import permissions
from contactlist.permissions import IsOwnerOrReadOnly
from rest_framework.decorators import api_view
from rest_framework.reverse import reverse
from rest_framework import renderers
from rest_framework.response import Response
from rest_framework import viewsets
from rest_framework.decorators import detail_route


# contactlist view and hyperlink view
class ContactViewSet(viewsets.ModelViewSet):
    # This text will be shown on the top of the contactlist view
    """
    you can `see list`, `create`, `retrieve`,
    `update` and `destroy` actions.
    """
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly,)

    # hyperlink class
    @detail_route(renderer_classes=[renderers.StaticHTMLRenderer])
    # This view give permission to admin for creating new contactlist
    def perform_create(self, serializer):
        serializer.save(admin=self.request.user)


# api-root view which show by visiting domain/api link
@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'contactlist': reverse('contact-list', request=request, format=format)
    })


# views for template
def ApiView(request):
    return render(request, 'contactlist/contactlist.html')


def JinjaView(request):
    contacts = Contact.objects.all()
    return render(request, 'contactlist/jinja.html', {'contacts': contacts})
