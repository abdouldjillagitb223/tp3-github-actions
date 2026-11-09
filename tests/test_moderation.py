from unittest.mock import Mock
from app.moderation import decider
import pytest 

modele=Mock()
modele.predict.return_value="spam"

def test_verifie_decision_bloc():
    decision= decider(modele, "Offre miracle")
    
    assert decision=="bloquer"
    modele.predict.assert_called_once_with("Offre miracle")
    
def test_verifie_decision_auto():
    modele = Mock()
    modele.predict.return_value = "normal"
    
    decision=decider(modele, "Bonjour, comment allez-vous ?")
    
    assert decision=="autoriser"
    
def test_erreur_modele_est_propagee():
    modele = Mock()

    modele.predict.side_effect = RuntimeError("Modele indisponible")

    with pytest.raises(RuntimeError, match="Modele indisponible"):
        decider(modele, "Bonjour, comment allez-vous ?")