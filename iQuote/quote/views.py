# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404

from rest_framework import status

from .models import Quote
from .serializers import QuoteSerializer

#========== ROOT API endpoint ==================

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
	return Response({
		'quotes': reverse('quote-list', request=request, format=format) 
		})
	# add the reverse link to all other views.

from rest_framework.views import APIView

class QuoteList(APIView):
	'''
	List all the quotes or create a new one!
	'''

	def get(self, request, format=None):

		quotes = Quote.objects.all()
		serializer = QuoteSerializer(quotes, many=True)
		return Response(serializer.data)

	def post(self, request, format=None):

		serializer = QuoteSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class QuoteDetail(APIView):
	'''
	Retreive, update or delete quotes.
	'''

	def get_object(self, pk):
		
		try:
			return Quote.objects.get(pk=pk)
		except Quote.DoeNotExist:
			raise Http404

	def get(self, request, pk, format=None):

		quote = self.get_object(pk)
		serializer = QuoteSerializer(quote)
		return Response(serializer.data, status=status.HTTP_200_OK)

	def put(self, request, pk, format=None):

		quote = self.get_object(pk)
		serializer = QuoteSerializer(quote, data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

	def delete(self, request, pk, format=None):

		quote = self.get_object(pk)
		quote.delete()
		return Response(status=status.HTTP_204_NO_CONTENT)
