import pytest
from app.texte import nettoyer_texte

def test_texte_Mm():
    texte="BONJOUR monde"
    result=nettoyer_texte(texte)
    assert result=="bonjour monde"

@pytest.mark.parametrize(
    "entree, attendu",
    [("BONJOUR monde", "bonjour monde"),("déjà propre", "déjà propre")]
)

def teste_texte_param(entree, attendu):
    assert nettoyer_texte(entree)==attendu
    
@pytest.mark.parametrize(
    "entree",
    [(123),(None)]
)
def teste_texte_param(entree):
    with pytest.raises(TypeError):
        assert nettoyer_texte(entree)