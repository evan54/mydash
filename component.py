import dash_core_components as dcc
import dash_html_components as html

print('package in main.py:', __package__)


def Button(**kwargs):
    if 'className' in kwargs:
        kwargs.pop('className')
    return html.Button(className='btn btn-outline-secondary btn-sm', **kwargs)


def Row(children=None, **kwargs):
    """A convenience component that makes a Bootstrap row"""
    return html.Div(children=children, className='row', **kwargs)


def Col(children=None, bp=None, size=None, **kwargs):
    """A convenience component that makes a Bootstrap column"""
    if size is None and bp is None:
        col_class = 'col'
    elif bp is None:
        col_class = f'col-{size}'
    else:
        col_class = f'col-{bp}-{size}'
    return html.Div(children=children, className=col_class, **kwargs)


def Input(id=None, **kwargs):
    if 'style' in kwargs:
        kwargs['style'].update({'width': '100%'})
    else:
        kwargs['style'] = {'width': '100%'}

    if 'size' in kwargs:
        kwargs.pop('size')
    return dcc.Input(id=id, **kwargs)
