from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[1]


def test_text_splitter_uses_its_supported_package():
    """Keep the app compatible with current LangChain package layout."""
    app_source = (PROJECT_ROOT / "app.py").read_text(encoding="utf-8")

    assert "from langchain_text_splitters import RecursiveCharacterTextSplitter" in app_source
    assert "from langchain.text_splitter import RecursiveCharacterTextSplitter" not in app_source


def test_deployment_requirements_include_text_splitters():
    requirements = (PROJECT_ROOT / "requirements.txt").read_text(encoding="utf-8")

    assert "langchain-text-splitters>=0.3.11" in requirements
