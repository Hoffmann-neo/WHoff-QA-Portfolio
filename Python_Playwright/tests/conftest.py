import pytest

@pytest.fixture(scope="session")
def launch_browser_args():
    return {
        "headless": False,
        "slow_mo": 300,
        "args": ["--start-maximized"]
    }

@pytest.fixture(scope="session")
def browser_context_args(browser_context_args):
    return {
        **browser_context_args,
        "viewport": None
    }