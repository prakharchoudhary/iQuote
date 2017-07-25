# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.contrib.auth.models import User
from django.http import Http404

from rest_framework import status
from rest_framework.renderers import StaticHTMLRenderer
from rest_framework import generics
from rest_framework import permissions

from .models import Quote
from .serializers import QuoteSerializer, UserSerializer
from .permissions import IsOwnerOrReadOnly

#========== ROOT API endpoint ==================

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.reverse import reverse

@api_view(['GET'])
def api_root(request, format=None):
	'''
	view to render the root of our API
	'''
	return Response({
		'quotes': reverse('quote-list', request=request, format=format),
		'users': reverse('user-list', request=request, format=format),
		})


#=============================== GENERIC CLASS-BASED VIEWS =============================================

class QuoteList(generics.ListCreateAPIView):
	'''
	List all the quotes or create a new one!
	'''
	queryset = Quote.objects.all()
	serializer_class = QuoteSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,]

	def perform_create(self, serializer):
		serializer.save(owner = self.request.user)

class QuoteDetail(generics.RetrieveUpdateDestroyAPIView):
	'''
	Retrieve, update or delete quotes for a single user.
	'''
	queryset = Quote.objects.all()
	serializer_class = QuoteSerializer
	permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly,]


class UserList(generics.ListAPIView):
	'''
	list all the users.
	'''
	queryset = User.objects.all()
	serializer_class = UserSerializer


class UserDetail(generics.RetrieveAPIView):
	'''
	retrieve details of a single user.
	'''
	queryset = User.objects.all()
	serializer_class = UserSerializer
