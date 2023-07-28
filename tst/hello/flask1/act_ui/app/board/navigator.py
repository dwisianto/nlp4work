import dash_bootstrap_components as dbc

# , active=True, disabled=True
nav_menu = dbc.Nav(
    [
        dbc.NavLink("Home", href="/board0",external_link=True),
        dbc.NavLink("Board1", href="/board1", external_link=True),
        dbc.NavLink("Board2", href="/board2", external_link=True),
        dbc.NavLink("Board3", href="/board3", external_link=True),
        dbc.NavLink("Feedback", href="/feedback", external_link=True),
        dbc.NavLink("Logout", href="/logout", external_link=True),
    ]
)
