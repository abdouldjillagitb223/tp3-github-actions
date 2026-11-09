from app.livraison import frais_livraison

def test_livraison_panier_ordinaire():
    # Arrange
    montant = 120
    # Act
    resultat = frais_livraison(montant)
    # Assert
    assert resultat == 25
    
def test_livraison_panier_ordinaire299():
    # 1-test
    montant=299
    resultat=frais_livraison(montant)
    assert resultat==25
    
def test_livraison_panier_ordinaire300():
    # 2- test
    montant=300
    resultat=frais_livraison(montant)
    assert resultat==0

def test_livraison_panier_ordinaire301():
    # 3- test
    montant=301
    resultat=frais_livraison(montant)
    assert resultat==0

def test_livraison_panier_ordinaire0():
    montant=0
    resultat=frais_livraison(montant)
    assert resultat==25