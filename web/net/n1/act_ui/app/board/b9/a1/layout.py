
from dash import dcc, html
from app.board.b9.a1.seed import board_id, board_user_store_id, board_button_submit_id, board_input_id, board_user_name_id, board_out_container_id

layout = html.Div(id=board_id,
                  children=[
                        html.H1(children='Hello Dash Button'),
                        html.H1(id=board_user_name_id),
                        html.Div(dcc.Input(id=board_input_id, type='text')),
                        html.Button('Submit', id=board_button_submit_id, n_clicks=0),
                        html.Div(id=board_out_container_id, children='Enter a value and press submit'),
                        dcc.Store(id=board_user_store_id),
], style={'width': '500'})


#layout = html.Div([
#    html.Div(dcc.Input(id='input-on-submit', type='text')),
#    html.Button('Submit', id='submit-val', n_clicks=0),
#    html.Div(id='container-button-basic',
#             children='Enter a value and press submit')
#])
