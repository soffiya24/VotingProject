from django.contrib import admin
from voting.models import Candidate_votes, ContactUS, Election, Voted
# Register your models here.
admin.site.register(Candidate_votes)
admin.site.register(ContactUS)
admin.site.register(Election)
admin.site.register(Voted)