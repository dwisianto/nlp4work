
from dash import dcc
from dash import html
from dash import dash_table
import dash_bootstrap_components as dbc


from act.actions import act_conf
from act.comment_letter3 import comment_letter_base, CommentLetterWebDb
from app.board.b7.b72.seed import board_db # board_df, keyword_list_dict, file_name_list_dict


app_style24 = {'fontSize': 36, 'font-family': 'serif'}
app_style_cell = {'fontSize': 18, 'font-family': 'serif', 'maxWidth': 0, 'textOverflow': 'ellipsis', 'overflow': 'hidden' }
app_style_header = {'font-family': 'serif', 'backgroundColor': 'rgb(255,204,204)', 'color': 'rgb(255,255,255)'}
app_style_label = {'fontSize': 24, 'font-family': 'serif', 'margin-left': '3px'}



# #                        html.Hr(),
app_layout_row_title = dbc.Row([
      dbc.Col(
          [
              html.H2("Full Text Search", style=app_style24),
          ],
          width=True,
      ),
    ], align="end",
)

app_layout_row_search_query_example = dbc.Row([
    dbc.Col([
        html.P(children=f'Example Query:', style=app_style_label),
        dcc.Dropdown(id=act_conf.sqlite_search_query_dropdown_id,
                     options= comment_letter_base.q_var,
                     placeholder='*',
                     multi=False),
    ], width=4),
    dbc.Col([
        html.P(children=f'Search Query:', style=app_style_label),
        dcc.Input(value=act_conf.sqlite_search_query_value,
                  id=act_conf.sqlite_search_query_cmd_id,
                  placeholder='Filter',
                  debounce=True,
                  style={'width': 1000, 'height':35} ),
        html.Button("search", id=act_conf.sqlite_search_query_example_button_id),

    ], width=8),
])

app_layout_row_search_query = dbc.Row([
        dbc.Col([
            html.P(children=f'Query:', style=app_style_label),
            dcc.Input(value=act_conf.sqlite_search_query_value,
                      id=act_conf.sqlite_search_query_id,
                      placeholder='Filter',
                      debounce=True,
                      style={'width': 1000, 'height':500}),
            html.Button("search", id=act_conf.sqlite_search_query_button_id),
        ],width=8)
    ])


#                 columns=[{'name': i, 'id': i} for i in board_db.db_df.columns],
#                 data=board_db.db_df.to_dict('records'),
app_layout_row_search_table = dbc.Row([
    dbc.Col([html.H5("Search Results", style=app_style_label),
             dash_table.DataTable(id=act_conf.sqlite_search_table_id,
                                  style_header=app_style_header,
                                  style_cell=app_style_cell,
                                  data=board_db.db_df.to_dict('records'),
                                  page_size=5,
                                  export_format='xlsx',
             )
    ], width=True, )
], align="end", )


app_layout_row_search_message_active_cell = html.Div(id=act_conf.sqlite_search_message_id)
app_layout_row_search_message_json = html.Pre(id=act_conf.sqlite_search_message_json_id)


# app_layout_row_search_query,
# app_layout_row_filter,
# app_layout_row_data_table,
# app_layout_row_data_table_message_active_cell,
layout = dbc.Container([app_layout_row_title,
                        app_layout_row_search_query_example,
                        app_layout_row_search_table,
                        app_layout_row_search_message_active_cell,
                        ],fluid=True)