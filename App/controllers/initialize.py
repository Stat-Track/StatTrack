from .user import create_user
from .campus import create_campus
from .faculties import create_faculty
from App.database import db


def initialize():
    db.drop_all()
    db.create_all()
    create_user('bob', 'bobpass', role='admin')
    create_user('rob','robpass')
    create_user('alice', 'alicepass',role='admin')
    create_user('james','jamespass')

    uwi_mona = create_campus('UWI Mona')
    uwi_sta = create_campus('UWI STA')
    uwi_5islands = create_campus('UWI Five Islands')
    uwi_cavehill = create_campus('UWI Cave Hill')
    
    create_faculty('Science & Technology',uwi_mona.id) 
    create_faculty('Science & Technology',uwi_sta.id)
    create_faculty('Science & Technology',uwi_5islands.id)
    create_faculty('Science & Technology',uwi_cavehill.id)
    create_faculty('Engineering',uwi_mona.id)
    create_faculty('Engineering',uwi_sta.id)
    create_faculty('Engineering',uwi_5islands.id)
    create_faculty('Engineering',uwi_cavehill.id)
    create_faculty('Social Sciences',uwi_mona.id)
    create_faculty('Social Sciences',uwi_sta.id)
    create_faculty('Social Sciences',uwi_5islands.id)
    create_faculty('Social Sciences',uwi_cavehill.id)
    create_faculty('Law',uwi_mona.id)
    create_faculty('Law',uwi_sta.id)
    create_faculty('Law',uwi_cavehill.id)
    create_faculty('Medical Sciences',uwi_sta.id)
    create_faculty('Medical Sciences',uwi_cavehill.id)

    
