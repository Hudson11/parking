from rest_framework import viewsets
from .models import Parking
from .serializers import ParkingSerializer
from rest_framework.decorators import action
from rest_framework.response import Response
from datetime import datetime
from datetime import timezone
from .pagination import LargeResultsSetPagination


class ParkingView(viewsets.ModelViewSet):
    queryset = Parking.objects.all()
    serializer_class = ParkingSerializer
    pagination_class = LargeResultsSetPagination

    @action(detail=True, methods=['put'])
    def pay(self, request, pk=None):
        plate = Parking.objects.get(id=pk)

        if plate.pay:
            return Response({'message': 'Paid out'})

        plate.pay = True
        plate.save()

        return Response({'message': 'Paid out'})

    @action(detail=True, methods=['put'])
    def out(self, request, pk=None):
        plate = Parking.objects.get(id=pk)

        if not plate.pay:
            return Response({'message': 'Pay is Required'})

        now = datetime.now()
        print(now)
        now.replace(tzinfo=timezone.utc).isoformat()
        create = datetime.strptime(str(plate.create).split('.')[0], '%Y-%m-%d %H:%M:%S')
        diff_minutes = abs((create - now).seconds) / 60

        plate.check_out = True
        plate.minutes = f'{int(diff_minutes)} minutes'
        plate.save()

        return Response({'message': 'Check-out'})
