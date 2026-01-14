from playwright.sync_api import sync_playwright

def debug_console():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Listen for console messages
        page.on("console", lambda msg: print(f"CONSOLE: {msg.text}"))
        page.on("pageerror", lambda err: print(f"ERROR: {err}"))

        try:
            page.goto("file:///app/picofile.html")
            page.wait_for_timeout(1000) # Give it a second to potentially crash
        except Exception as e:
            print(f"Exception: {e}")

        browser.close()

if __name__ == "__main__":
    debug_console()
