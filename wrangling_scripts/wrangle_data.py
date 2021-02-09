import pandas as pd
import plotly.graph_objs as go

def return_figures():
    """Creates four plotly visualizations

    Args:
        None

    Returns:
        list (dict): list containing the four plotly visualizations

    """

    # first chart plots total population over time as line
    df = pd.read_csv('data/berlin_districts.csv')
    
    graph_one = [go.Scatter(
      x = df['year'],
      y = df['Berlin'],
      mode = 'lines'
      )] 

    layout_one = dict(title = 'Total Population {}-{}'.format(str(df['year'].min()), str(df['year'].max())),
                xaxis = dict(title = 'Year'),
                yaxis = dict(title = 'Population')
                )

    # second chart plots german vs foreign population as grouped bar
    df = pd.read_csv('data/berlin_population.csv')
    
    graph_two = [
        go.Bar(x=df['year'], y=df['german'], name='German'),
        go.Bar(x=df['year'], y=df['foreign'], name='Foreign')
    ]

    layout_two = dict(title = 'German vs Foreign Population {}-{}'.format(str(df['year'].min()), str(df['year'].max())),
                xaxis = dict(title = 'Year'),
                yaxis = dict(title = 'Population'),
                barmode='stack'
                )


    # third chart plots population by district as line
    df = pd.read_csv('data/berlin_districts.csv')
    graph_three = [go.Scatter(x=df['year'], y=df[col], mode='lines', name=col) for col in df.columns[1:-1]]

    layout_three = dict(title = 'Population by Neighbourhood {}-{}'.format(str(df['year'].min()), str(df['year'].max())),
                xaxis = dict(title = 'Year'),
                yaxis = dict(title = 'Population')
                       )
    
    # fourth chart shows rural population vs arable land
    df = pd.read_csv('data/berlin_ages.csv')
    new_cols = ['year']
    for i in range(1, len(df.columns)):
        nums = df.columns[i].split('-')
        new_cols.append((int(nums[0]) + int(nums[1])) / 2.0)
    df.columns = new_cols
    df['total'] = df[df.columns[1:]].sum(axis=1)
    for col in df.columns[1:-1]:
        df[col] = (df[col] * col) / df['total']
    df['avg_age'] = df[df.columns[1:-1]].sum(axis=1)
    df = df[['year', 'avg_age']]
    
    graph_four = [go.Scatter(
      x = df['year'],
      y = df['avg_age'],
      mode = 'lines'
      )]

    layout_four = dict(title = 'YoY Avg Age {}-{}'.format(str(df['year'].min()), str(df['year'].max())),
                xaxis = dict(title = 'Year'),
                yaxis = dict(title = 'Avg Age (yrs)'),
                )
    
    # append all charts to the figures list
    figures = []
    figures.append(dict(data=graph_one, layout=layout_one))
    figures.append(dict(data=graph_two, layout=layout_two))
    figures.append(dict(data=graph_three, layout=layout_three))
    figures.append(dict(data=graph_four, layout=layout_four))

    return figures