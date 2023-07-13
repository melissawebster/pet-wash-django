from pytest_django.asserts import assertTemplateUsed
import pytest


@pytest.mark.django_db
def test_booking_view_should_return_template(client):
    response = client.get('/create-booking/')
    assert response.status_code == 200
    assertTemplateUsed(response, 'create-booking.html')