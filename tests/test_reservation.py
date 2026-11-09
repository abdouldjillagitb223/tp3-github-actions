import pytest
from app.reservation import Stock, Reservation

@pytest.fixture
def stock():
    return Stock(5)
    
def test_reservation_2_unit(stock):
    
    result=Reservation(stock)
    statut= result.reserver(2)
    
    assert statut=="confirmee"
    assert stock.quantite==3
    
def test_reservation_6_unit(stock):
    resultat=Reservation(stock)
    statut=resultat.reserver(6)
    
    assert statut=="refusee"
    assert stock.quantite==5

def test_reservation_5_unit(stock):
    result=Reservation(stock)
    statut=result.reserver(5)
    
    assert statut=="confirmee"
    assert stock.quantite==0

def test_reservation_0_unite(stock):
    reservation = Reservation(stock)

    with pytest.raises(ValueError, match="Quantite positive requise"):
        reservation.reserver(0)

    assert stock.quantite == 5