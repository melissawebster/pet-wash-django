from datetime import date
import pytest
from model_bakery import baker
from booking.models import Booking


#fixture faz com que a função possa ser usada como parâmetro em outros testes
@pytest.fixture
def booking():
    booking = baker.make(
        Booking,
        name = 'Floki',
        date = date.today(),
        shift = 'Morning'
    )
    return booking


@pytest.mark.django_db
def test_booking_should_return_string_format(booking):
    assert str(booking) == f'Floki: {date.today()} - Morning'
