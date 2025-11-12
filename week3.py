from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from markdown import markdown
from pathlib import Path

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def week3_readme():
    """Render Week 3 README.md as HTML."""
    md_path = Path(__file__).parent / "week3_readme.md"

    if not md_path.exists():
        return "<h1>Week 3 README not found.</h1>"

    md_content = md_path.read_text(encoding="utf-8")
    html_content = markdown(
        md_content,
        extensions=["fenced_code", "tables", "toc", "attr_list"]
    )

    html = f"""
    <html>
    <head>
        <title>Week 3 — CNNs (INFS 6359)</title>
        <style>
            body {{
                font-family: system-ui, sans-serif;
                margin: 2rem auto;
                max-width: 900px;
                line-height: 1.6;
                color: #222;
            }}
            h1, h2, h3 {{ color: #1f2937; }}
            h1 {{ border-bottom: 2px solid #ddd; padding-bottom: .3em; }}
            pre, code {{
                background: #f3f4f6;
                padding: .2em .4em;
                border-radius: 4px;
                font-size: 0.95em;
            }}
            a {{ color: #2563eb; text-decoration: none; }}
            a:hover {{ text-decoration: underline; }}
            table {{ border-collapse: collapse; margin: 1em 0; }}
            th, td {{ border: 1px solid #ccc; padding: 0.4em 0.6em; }}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """
    return html
