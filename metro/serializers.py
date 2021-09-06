from django.db.models import Q
from rest_framework import serializers


from .models import Station, Line


class StationLineSerializer(serializers.ModelSerializer):
    station = serializers.CharField(source='name')
    line = serializers.CharField(source='line.name')
    color = serializers.CharField(source='line.color')

    class Meta:
        model = Station
        fields = [
            'station',
            'line',
            'color'
        ]


def station_get_or_create(data):
    lines = Line.objects.filter(name=data['line'])
    if lines.exists():
        line = lines.first()
        pass
    else:
        line_data = {'name': data['line'], 'color': data['color']}
        line = Line.objects.create(**line_data)

    stations = Station.objects.filter(Q(name=data['station']) & Q(line__color=data['color']))
    if stations.exists():
        station = stations.first()
    else:
        station_data = {'name': data['station'], 'line': line, 'code_name': data['station']+line.name}
        station = Station.objects.create(**station_data)
    return station
