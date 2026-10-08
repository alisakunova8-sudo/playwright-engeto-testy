# Playwright testy pro Engeto.cz

Tři automatizované testy vytvořené pomocí frameworku Playwright a pluginu pytest-playwright.

## Testované scénáře

1. **Titulek stránky** – ověří, že se hlavní stránka Engeto.cz správně načte a má očekávaný titulek.
2. **Navigace na FAQ** – ověří, že odkaz FAQ vede na správnou stránku.
3. **Navigace na Python Akademii** – ověří, že odkaz Python Akademie vede na správnou podstránku kurzu.

## Použité technologie

- Python
- pytest
- Playwright
- pytest-playwright

## Požadavky

- Python 3.10 nebo novější
- pip

## Instalace

1. Naklonujte repozitář:

```bash
git clone https://github.com/alisakunova8-sudo/playwright-engeto-testy.git
cd playwright-engeto-testy
```

2. Vytvořte virtuální prostředí.

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

### Windows

```bash
python -m venv venv
venv\\Scripts\\activate
```

3. Nainstalujte závislosti:

```bash
pip install -r requirements.txt
```

4. Nainstalujte prohlížeče pro Playwright:

```bash
playwright install
```

## Spuštění testů

Spuštění všech testů:

```bash
pytest -v
```

Nebo pouze soubor s testy:

```bash
pytest test_playwright.py -v
```

## Poznámka

Testy používají pytest-playwright fixture `page` a Playwright `expect()` assertions.

Cookie lišta je ošetřena pomocnou funkcí `prijmi_cookies()`, aby se opakovaná logika nemusela psát v každém testu zvlášť.
