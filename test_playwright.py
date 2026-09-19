from playwright.sync_api import Page, expect


def prijmi_cookies(page: Page):
    """Pomocná funkce - odklikne cookie lištu, pokud se objeví."""
    try:
        page.get_by_text("Souhlasím jen s nezbytnými").click(timeout=5000)
    except Exception:
        pass


def test_titulek_stranky(page: Page):
    """Test 1: Ověří, že se hlavní stránka správně načte a má očekávaný titulek."""
    page.goto("https://engeto.cz")
    expect(page).to_have_title("Kurzy programování a dalších IT technologií | ENGETO")


def test_navigace_na_faq(page: Page):
    """Test 2: Ověří, že odkaz FAQ v menu funguje a vede na správnou stránku."""
    page.goto("https://engeto.cz")
    prijmi_cookies(page)
    page.get_by_role("link", name="FAQ", exact=True).click()
    expect(page).to_have_url("https://engeto.cz/faq/")


def test_navigace_na_python_akademii(page: Page):
    """Test 3: Ověří, že kliknutí na Python Akademii vede na správnou podstránku."""
    page.goto("https://engeto.cz")
    prijmi_cookies(page)
    page.get_by_role("link", name="Python Akademie", exact=True).first.click()
    expect(page).to_have_url("https://engeto.cz/python-akademie/")