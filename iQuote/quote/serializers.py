from django.contrib.auth.models import User

from rest_framework import serializers

from quote.models import Quote

# class QuoteSerializer(serializers.HyperlinkedModelSerializer):
# 	owner = serializers.ReadOnlyField(source='owner.username')

# 	class Meta:
# 		model = Quote
# 		fields = ('url', 'id', 'owner', 'quote', 'category')

# class UserSerializer(serializers.HyperlinkedModelSerializer):
# 	quotes = serializers.HyperlinkedIdentityField(view_name='quote-detail', read_only=True)

# 	class Meta:
# 		model = User
# 		fields = ('url', 'id', 'username', 'quotes')


class QuoteSerializer(serializers.ModelSerializer):
	owner = serializers.ReadOnlyField(source='owner.username')

	class Meta:
		model = Quote
		fields = ('id', 'owner', 'quote', 'category')

class UserSerializer(serializers.ModelSerializer):
	quotes = serializers.PrimaryKeyRelatedField(many=True, queryset=Quote.objects.all())

	class Meta:
		model = User
		fields = ('id', 'username', 'quotes')

	def perform_create(self, serializer):
		serializer.save(owner=self.request.user)