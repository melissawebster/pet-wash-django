import pytest
import datetime
from model_bakery import baker
from booking.models import Booking
from rest_api.serializers import BookingModelSerializer

#verificar se o serializador é capaz de identificar dados inválidos e falhar na validação

@pytest.fixture
def wrong_booking_data():
    yesterday = datetime.date.today() - datetime.timedelta(days=1)
    booking = baker.make(Booking)
    return {
        'name': 'test name',
        'email': 'email@email.com',
        'pet_name': 'pet name',
        'date': yesterday,
        'shift': 'morning',
        'size': 0,
        'notes': 'blabla blabla',
        'booking': booking.pk,
    }

@pytest.mark.django_db
def test_invalid_booking_date(wrong_booking_data):
    serializer = BookingModelSerializer(data=wrong_booking_data)
    assert not serializer.is_valid()