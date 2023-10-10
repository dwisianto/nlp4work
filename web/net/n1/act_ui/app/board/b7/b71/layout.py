
from dash import dcc
from dash import html
from dash import dash_table
import dash_bootstrap_components as dbc


from act.actions import act_conf
from app.board.b7.b71.seed import board_df, keyword_list_dict, file_name_list_dict


app_style24 = {'fontSize': 32, 'font-family': 'serif'}
app_style_cell = {'fontSize': 18, 'font-family': 'serif', 'maxWidth': 0, 'textOverflow': 'ellipsis', 'overflow': 'hidden'}
app_style_header = {'font-family': 'serif', 'backgroundColor': 'rgb(255,204,204)', 'color': 'rgb(255,255,255)'}
app_style_label = {'fontSize': 24, 'font-family': 'serif', 'margin-left': '3px'}

app_layout_row_title = dbc.Row([
      dbc.Col(
          [
              html.H1(id='username',style=app_style24),
              dcc.Store(id='user-store'),
          ],
          width=True,
      ),
    ], align="end",
)

app_layout_row_filter = dbc.Row([
    dbc.Col([
        html.P(children=f'Filename Filter:', style=app_style_label),
        dcc.Dropdown(id=act_conf.exploration_id_filter_file_name, options=file_name_list_dict, multi=True)
    ], width=3),
    dbc.Col([
        html.P(children=f'Keyword Filter:', style=app_style_label),
        dcc.Dropdown(id=act_conf.exploration_id_filter_keyword, options=keyword_list_dict, multi=True)
    ], width=3),
    dbc.Col([
        html.P(children=f'Sentence Text Filter', style=app_style_label),
        dcc.Input(id=act_conf.exploration_id_filter_sentence_text, value='',
                  placeholder='Filter', debounce=True, style={'width':'80%', 'height': '40%'}),
        html.Button("explore", id=act_conf.exploration_id_filter_button_exe),
    ], width=6),

])



# ,'fontWeight':'bold'
app_layout_row_data_table=dbc.Row([
        dbc.Col([
                dash_table.DataTable(
                    id=act_conf.exploration_id_table,
                    style_cell=app_style_cell,
                    style_header=app_style_header,
                    #sytle_cell_conditional=[ ],
                    columns=[ {'name': i, 'id': i} for i in board_df.columns ],
                    data= board_df.to_dict('records'),
                    page_size=10,
                    export_format='xlsx',
                    css=[{'selector':'.export','rule':'position:absolute;right:15px;bottom:-30px'}],
                ),
            ],
        ),
    ],
    align=True,
)


app_layout_row_data_table_message_active_cell = dbc.Row([
    dbc.Col([
            html.Div(id=act_conf.exploration_id_message_active_cell)
        ], width=10),
    ], align=True)


layout = dbc.Container([app_layout_row_title,
                        html.Hr(),
                        app_layout_row_filter,
                        app_layout_row_data_table,
                        app_layout_row_data_table_message_active_cell,
                        ],fluid=True)