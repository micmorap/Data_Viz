
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#install this package to start: 
#pip install dash pandas
#conda install dash

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd


#Step 1:
    
#app = dash.Dash(name= "Mike_first_dash_app")
app = dash.Dash(__name__)

#Step 2: upload a dataset using Plotly:
tips = px.data.tips()
fig = px.scatter(tips, x= 'total_bill', y= 'tip')

#HTML Variables to layout object
title = html.H1(children='Hello Mike')

text_div = html.Div(children = '''
         Dash: A exercise to create a Web application framework for data.
         Guide taken from blog.logrocket.com/data-visualization-interfaces-python-dash/
         Author: Bekhruz Tuychiev
         ''')
         
graph_to_display = dcc.Graph(id = 'example-graph', figure = fig)          

list_elements = html.Div([
    dcc.Dropdown(options=[
        {'label': 'Number one', 'value': 'Eins'},
        {'label': 'Number two', 'value': 'Zwei'},
        {'label': 'Number three', 'value': 'Drei'}
            
        ],
        value = 'Number one',
        multi = True
        )],
        
        style = {"width": 200}
    )


slider = html.Div([
    dcc.Slider(
        min = 0,
        max = 9,
        marks = {i: 'Step{}'.format(i) for i in range(10)},
        value = 5
        
        )
    ])


#Step 4: consolidate layout with above variables:
app.layout = html.Div(children =[
    title,
    text_div,
    graph_to_display,
    list_elements,
    slider         
    ])
             

if __name__ == '__main__':
    app.run_server(debug = True)
    
    
     