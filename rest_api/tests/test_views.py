import pytest
from rest_framework.test import APIClient
import datetime
from booking.models import Branch
from rest_api.serializers import BranchModelSerializer
from model_bakery import baker

#teste para salvar agendamentos de banho
@pytest.fixture
def booking_data():
    today = datetime.date.today()
    branch = baker.make(Branch)
    return {
        'name': 'test name',
        'email': 'email@email.com',
        'pet_name': 'pet name',
        'date': today,
        'shift': 'morning',
        'size': 0,
        'notes': 'blabla blabla',
        'branch': branch.pk,
    }

@pytest.fixture
def user():
    return baker.make('auth.User')

@pytest.mark.django_db
def test_create_booking(user, booking_data):
    client = APIClient()
    client.force_authenticate(user)
    answer = client.post('/api/booking', booking_data)
    assert answer.status_code == 201

@pytest.mark.django_db
def test_all_petshops():
    client = APIClient()
    answer = client.get('/api/booking')
    assert len(answer.data['results']) == 0


