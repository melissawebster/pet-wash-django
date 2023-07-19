import datetime
from rest_framework.serializers import (
    ModelSerializer, 
    HyperlinkedRelatedField,
    PrimaryKeyRelatedField,
    ValidationError
)
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


class BranchRelatedCustomSerializer(PrimaryKeyRelatedField):
    def __init__(self, **kwargs):
        self.serializer = BranchModelSerializer
        super().__init__(**kwargs)

    def use_pk_only_optimization(self):
        return False
    
    def to_representation(self, value):
        return self.serializer(value, context=self.context).data


class BookingModelSerializer(ModelSerializer):
    branch = BranchRelatedCustomSerializer(
        queryset = Branch.objects.all(),
        read_only=False
    )

    def validate_data(self, value):
        today = datetime.date.today()
        if value < today:
            raise ValidationError('You cannot book a bath on a past day.')
        return value
    
    class Meta:
        model = Booking
        fields = '__all__'