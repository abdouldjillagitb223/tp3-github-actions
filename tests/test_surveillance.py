from unittest.mock import patch
from app.surveillance import surveiller
import pytest

def test_surveiller_015():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat=surveiller(0.15)
        
        assert resultat=="alerte"
        
        notifier.assert_called_once_with("Taux eleve")

def test_surveiller_005():
    with patch("app.surveillance.envoyer_notification") as notifier:
        resultat=surveiller(0.05)
        
        assert resultat=="ok"
        notifier.assert_not_called()

def test_surveiller_010():
    with patch("app.surveillance.envoyer_notification") as notifier:
        
        resultat=surveiller(0.10)
        
        assert resultat=="ok" 
        
def test_erreur_notification_est_propagee():
    with patch("app.surveillance.envoyer_notification") as notifier:

        notifier.side_effect = RuntimeError("Service non configure")

        with pytest.raises(RuntimeError, match="Service non configure"):
            surveiller(0.15)        