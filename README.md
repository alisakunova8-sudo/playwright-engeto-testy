# Playwright testy pro Engeto.cz

Tři automatizované testy vytvořené pomocí frameworku Playwright a pluginu pytest-playwright.

## Testované scénáře

1. Titulek stránky – ověří, že se hlavní stránka Engeto.cz správně načte
2. Navigace na FAQ – ověří, že odkaz FAQ vede na správnou stránku
3. Navigace na Python Akademii – ověří navigaci na podstránku kurzu

## Jak spustit testy

pytest test_playwright.py -v

