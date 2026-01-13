Projekt 3 – Automatizované testy (Playwright)

Tento projekt obsahuje automatizované UI testy webové stránky ENGETO vytvořené pomocí knihoven Playwright a pytest-playwright.

Použité technologie
- Python
- pytest
- Playwright
- pytest-playwright

Testovaná stránka
- https://engeto.cz

Struktura projektu
- `tests/test_engeto.py` – testovací scénáře
- `tests/conftest.py` – fixture pro otevření stránky a ošetření cookie banneru

Testovací scénáře
Projekt obsahuje 4 automatizované testy:
1. Ověření titulku stránky
2. Ověření viditelnosti odkazu „Kurzy“
3. Ověření funkčnosti odkazu „Kurzy“ (kliknutí + kontrola URL)
4. Ověření existence patičky stránky

Spuštění testů

Spuštění testů (headless)
```bash
pytest -v
