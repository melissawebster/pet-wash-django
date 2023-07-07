from rest_framework.serializers import ModelSerializer, HyperlinkedRelatedField
from booking.models import Booking, Branch


class BranchModelSerializer(ModelSerializer):
    booking = HyperlinkedRelatedField(
        many = True,
        read_only = True,
        view_name='api:booking-detail'
    )

    class Meta:
        model = Branch
        fields = '__all__'


class BookingModelSerializer(ModelSerializer):
    branch = BranchModelSerializer(read_only=True)

    class Meta:
        model = Booking
        fields = '__all__'