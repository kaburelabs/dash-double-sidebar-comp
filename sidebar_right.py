import dash_bootstrap_components as dbc
from dash import dcc, html

# we use the Row and Col components to construct the sidebar header
# it consists of a title, and a toggle, the latter is hidden on large screens
right_sidebar_header = dbc.Row(
    [
        dbc.Col(
            [
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon right-icon-custom"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="right-navbar-toggle",
                ),
                html.Button(
                    # use the Bootstrap navbar-toggler classes to style
                    html.Span(className="navbar-toggler-icon right-icon-custom"),
                    className="navbar-toggler",
                    # the navbar-toggler classes don't set color
                    style={
                        "color": "rgba(0,0,0,.5)",
                        "border-color": "rgba(0,0,0,.1)",
                    },
                    id="right-sidebar-toggle",
                ),
            ],
            # the column containing the toggle will be only as wide as the
            # toggle, resulting in the toggle being right aligned
            width="auto",
            # vertically align the toggle in the center
            align="center",
        ),
        dbc.Col(html.P("transcription", className="font-sm")),
    ]
)

right_sidebar = html.Div(
    [
        right_sidebar_header,
        # we wrap the horizontal rule and short blurb in a div that can be
        # hidden on a small screen
        html.Div(
            [
                html.Hr(),
                html.P(
                    "Sidebar Right",
                    className="lead",
                ),
            ],
            id="right-blurb",
        ),
        # use the Collapse component to animate hiding / revealing links
        dbc.Collapse(

            [html.Div(f"Itens in the second Sidebar{n}") for n in range(0, 10)],
            id="right-collapse",
        ),
    ],
    id="right-sidebar",
)
