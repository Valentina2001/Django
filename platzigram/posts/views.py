# Django
from django.shortcuts import render

# Utilities
from datetime import datetime

posts = [
	{
		'title': 'Mont blac',
		'user': {
			'name': 'Yesica Cortés',
			'picture': 'https://picsum.photos/200/200/?image=1010'
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'photo': 'https://picsum-photos/800/600?image=1036'
		
	},
	{
		'title': 'Vía Láctea',
		'user': {
			'name': 'C. Vander',
			'picture': 'https://picsum.photos/200/200/?image=378'
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'photo': 'https://picsum-photos/800/600?image=1056'
		
	},
	{
		'title': 'Nuevo auditorio',
		'user': {
			'name': 'Thespiartist',
			'picture': 'https://picsum.photos/200/200/?image=996'
		},
		'timestamp': datetime.now().strftime('%b %dth, %Y - %H:%M hrs'),
		'photo': 'https://picsum-photos/800/600?image=1032'
		
	},
]


def list_posts(request):
	'''List existing posts'''
	return render(request, 'feed.html', {'posts': posts})
