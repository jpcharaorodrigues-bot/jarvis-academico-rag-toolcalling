from app.tools.agenda_tools import consultar_agenda


def test_consultar_agenda():
    resultado = consultar_agenda("semana")

    assert "periodo" in resultado
    assert "eventos" in resultado
