from rest_framework import serializers
from contactlist.models import Contact

# contact serializer for readonly view
class ContactSerializer(serializers.ModelSerializer):
    admin = serializers.ReadOnlyField(source='admin.username')
    class Meta:
        model = Contact
        fields = ('id', 'name', 'contact_number', 'admin')

# contact serialization for creating hyperlink
class ContactSerializer(serializers.HyperlinkedModelSerializer):
    admin = serializers.ReadOnlyField(source='admin.username')
    
    class Meta:
        model = Contact
        fields = ('url', 'id', 'name', 'contact_number', 'admin',)

