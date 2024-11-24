from django.db.models import Avg
from rest_framework import serializers
from movies.models import Movie


class MovieSerializer(serializers.ModelSerializer):
    rate = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Movie
        fields = '__all__'

    def get_rate(self, obj):
        stars_avg = obj.reviews.aggregate(Avg('stars'))['stars__avg']

        if stars_avg:
            return round(stars_avg, 1)

        return None
