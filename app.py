import uvicorn
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles


app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
with open("static/index.html") as indx:
    index = indx.read()

def wrap_resp(target: str, html: str) -> str:
    return f"""<div xxx-update="{target}">{html}</div>"""

@app.get("/", response_class=HTMLResponse)
async def root():
    return index
    
@app.get("/single-update", response_class=HTMLResponse)
async def single_update():
    html = """<p id="single-update">So easy!</p>"""
    return wrap_resp("single-update", html)

@app.get("/multiple-updates", response_class=HTMLResponse)
async def multiple_updates():
    update_1 = """<li id="item-1">htmxxx</li>"""
    update_2 = """<li id="item-3">greaterer</li>"""
    return wrap_resp("item-1", update_1) + wrap_resp("item-3", update_2)

@app.get("/nested-update/{x}", response_class=HTMLResponse)
async def nested_update(x: int):
    new_x = x + 1
    update = f"""
<p id="nested-update"><a href="/nested-update/{new_x}" xxx>I have update {x} times</a></p>
"""
    return wrap_resp("nested-update", update)


@app.get("/query-param-update", response_class=HTMLResponse)
async def qparam_update(request: Request):
    query_params = request.query_params
    name = query_params.get("name")
    html = f"""<p id="qparam-target">{name} is doing such a good job with this demo"""
    return wrap_resp("qparam-target", html)

@app.post("/form-post-update", response_class=HTMLResponse)
async def form_post_update(request: Request):
    html = f"""<p id="form-post-target">Form submitted!</p>"""
    return wrap_resp("form-post-target", html)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8080)