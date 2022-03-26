from operator import le
import dash
import dash_bootstrap_components as dbc
from dash import Input, Output, State, dcc, html

from sidebar_left import left_sidebar
from sidebar_right import right_sidebar


app = dash.Dash(
    external_stylesheets=[dbc.themes.BOOTSTRAP],
    # these meta_tags ensure content is scaled correctly on different devices
    # see: https://www.w3schools.com/css/css_rwd_viewport.asp for more
    meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ],
)

content = html.Div(id="page-content")

app.layout = html.Div([dcc.Location(id="url"), right_sidebar, content, left_sidebar])


@app.callback(Output("page-content", "children"), [Input("url", "pathname")])
def render_page_content(pathname):
    if pathname == "/":
        return html.P("This is the content of the home page!")
    elif pathname == "/page-1":
        return html.P("This is the content of page 1. Yay!")
    elif pathname == "/page-2":
        return html.P("Oh cool, this is page 2!")
    # If the user tries to reach a different page, return a 404 message
    return dbc.Jumbotron(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ]
    )

@app.callback(
    Output("right-sidebar", "className"),
    [Input("right-sidebar-toggle", "n_clicks")],
    [State("right-sidebar", "className")],
)
def toggle_classname(n, classname):
    if n and classname == "":
        return "collapsed-right"
    return ""

@app.callback(
    Output("left-sidebar", "className"),
    [Input("left-sidebar-toggle", "n_clicks")],
    [State("left-sidebar", "className")],
)
def toggle_classname(n, classname):
    if n and classname == "":
        return "collapsed-left"
    return ""

@app.callback(
    Output("page-content", "className"),
    [Input("right-sidebar", "className"), 
     Input("left-sidebar", "className")],
)
def setting_class_content(right_sidebar, left_sidebar):
    # print(right_sidebar, left_sidebar)
    
    if right_sidebar != "collapsed-right" and left_sidebar != "collapsed-left":
        # print("both open")
        return "pageContentBo"
    elif right_sidebar == "collapsed-right" and left_sidebar != "collapsed-left":
        # print("only left open")
        return "pageContentOlc"
    elif right_sidebar != "collapsed-right" and left_sidebar == "collapsed-left":
        # print("only right open")
        return "pageContentOro"
    elif right_sidebar == "collapsed-right" and left_sidebar == "collapsed-left":
        # print("both closed")
        return "pageContentBc"
    return ""

@app.callback(
    Output("left-collapse", "is_open"),
    [Input("left-navbar-toggle", "n_clicks")],
    [State("left-collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open



@app.callback(
    Output("right-collapse", "is_open"),
    [Input("right-navbar-toggle", "n_clicks")],
    [State("right-collapse", "is_open")],
)
def toggle_collapse(n, is_open):
    if n:
        return not is_open
    return is_open


if __name__ == "__main__":
    app.run_server(port=8888, debug=True)