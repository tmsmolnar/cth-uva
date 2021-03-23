import pandas as pd
from bokeh.models import ColumnDataSource, HoverTool, LinearInterpolator, CategoricalColorMapper, Paragraph
from bokeh.plotting import figure
from bokeh.palettes import Category20b_20
from bokeh.layouts import column, row
from bokeh.io import show, curdoc


def load_data(path_to_file, index, sheet):

    """

    Load the dataset, select which column should be the index, and which sheet of the dataset should be loaded.

    Parameters:    
        path_to_file: string
                The path to the file the user wants to load
                The datasets can be found under the datasets folder

        index: integer
                The column the user wants to consider as index

        sheet: string or integer
                The name or number of the sheet the user wants to load
                0 - Elementary school
                1 - Special school
                2 - Technical school
                3 - Vocational school
                4 - High school


    Returns:
        a DataFrame

    """

    dataFrame = pd.read_excel(path_to_file, index_col=index, sheet_name=sheet)
    
    if 'Adatok' in dataFrame.columns:
        for value in dataFrame['Adatok']:
            if value == 'Összeg / Csongrád-Csanád megye':
                value_new = 'Összeg / Csongrád megye'
                dataFrame = dataFrame.replace({value: value_new})
    else:
        pass

    #dataFrame = dataFrame.fillna(0).astype(int)

    return dataFrame

def merge_dataFrames_index(dataFrame_1, dataFrame_2):

    """
    Merge two DataFrames based on their indexes

    Parameters:
        dataFrame_1, dataFrame_2: string
            The name of the DataFrames the user wants to merge

    Returns:
        a DataFrame
    """

    dataFrames = [dataFrame_1, dataFrame_2]
    merged_dataFrames = pd.concat(dataFrames)

    return merged_dataFrames

def merge_dataFrames_column(dataFrame_1, dataFrame_2):

    """
    Merge two DataFrames based on their columns

    Parameters:
        dataFrame_1, dataFrame_2: string
            The name of the DataFrames the user wants to merge

    Returns:
        a DataFrame

    """

    dataFrames = [dataFrame_1, dataFrame_2]
    merged_dataFrames = pd.concat(dataFrames, axis=1)

    return merged_dataFrames

def clean_index(dataFrame):

    """
    Clean the index columns from unnecessary words, punctuations

    Parameters:
        dataFrame: string
            The name of the DataFrame in which the user wants to clean the index

    Returns:
        a DataFrame

    """

    for index in dataFrame.index:
        splitted_index = index.split(".")
        new_index = splitted_index[0]
        dataFrame = dataFrame.rename(index={index:new_index})

    return dataFrame

def clean_index_year(dataFrame):

    """
    Clean those indexes, where the index contains the years and removes the word 'year'

    Parameters:
        dataFrame: string
            The name of the dataFrame in which the user wants to clean the index

    Returns:
        a DataFrame

    """

    for index in dataFrame.index:
        splitted_index = index.split(" ")
        new_index = splitted_index[2]
        dataFrame = dataFrame.rename(index={index:new_index})

    return dataFrame

def clean_regions(dataFrame):

    """
    Clean those columns that contains the regions, to contain only the name of the region.

    Parameters:
        dataFrame: string
            The name of the DataFrame in which the users wants to clean the region columns

    Returns:
        a DataFrame

    """

    for value in dataFrame['Region']:
        splitted_value = value.split(" ")
        new_value = splitted_value[2]
        dataFrame = dataFrame.replace({value: new_value})

    return dataFrame

def clean_column(dataFrame):
    
    """
    Clean the columns from unnecessary words and punctuations.

    Parameters:
        dataFrame: string
            The name of the DataFrame in which the user wants to clean the columms

    Returns:
        a DataFrame

    """

    for column in dataFrame:
        splitted_column = column.split(" ")
        new_column = splitted_column[0]
        dataFrame = dataFrame.rename(columns={column: new_column})

    return dataFrame

def clean_age(dataFrame):

    """
    Clean those columns that contains the ages of the students, and change the word 'éves' to 'yrs'.

    Parameters:
        dataFrame: string
            The name of the DataFrame in which the user wants to clean the columns containing the ages

    Returns:
        a DataFrame

    """

    for value in dataFrame['Age']:
        splitted_value = value.split(" ")
        new_value = splitted_value[0] + " yrs"
        dataFrame = dataFrame.replace({value: new_value})

    return dataFrame

def two_to_one_regions(data_1, data_2, sheet_index):

    """
    This function is the main function to be used on the transformation of data that contains the regions! Loads the data, merges the DataFrames,
    cleans the columns, indexes, rename columns to make it readable and understandable.

    Parameters:
        data_1, data_2: strings
            The paths of the files the user wants to load and work with
        
        sheet_index: integer
            The number of the sheet the user wants to work with
            0 - Elementary school
            1 - Special school
            2 - Technical school
            3 - Vocational school
            4 - High school

    Returns:
        a DataFrame

    """


    df1 = load_data(data_1, index = 1, sheet = sheet_index)
    df2 = load_data(data_2, index = 1, sheet = sheet_index)

    result = merge_dataFrames_index(df1, df2)
    result = result.rename(columns={'Adatok': 'Region', 'Összeg': 'Number of students'})
    result.index.name = None
    result = result.rename_axis("Year", axis='columns')



    result = clean_index(result)
    result = clean_regions(result)

    return result

def two_to_one_years(data_1, data_2, sheet_index):

    """
    This function is the main function to be used on the transformation of data that contains the ages of students! Loads the data, merges the DataFrames,
    cleans the columns, indexes, rename columns to make it readable and understandable.

    Parameters:
        data_1, data_2: strings
            The paths of the files the user wants to load and work with
        
        sheet_index: integer
            Has to be zero, as there is only one sheet for these datasets

    Returns:
        a DataFrame

    """

    df1 = load_data(data_1, index=0, sheet = sheet_index)
    df2 = load_data(data_2, index=0, sheet = sheet_index)

    result = merge_dataFrames_index(df1, df2)
    result = result.rename(columns={'Életkor (köznevelés)': 'Age', 'Összeg': 'Number of students'})
    result['Number of students'] = result['Number of students'].fillna(0).astype(int)    
    result.index.name = None
    result = result.rename_axis("Year", axis='columns')

    
    result = clean_index_year(result)
    result = clean_index(result)
    result = clean_age(result)

    return result

def two_to_one_regions_gradszakma(data_1, data_2):
    """
    This function is for only one case, where the graduated datasets differ, because of the KSH! Loads the data, merges the DataFrames,
    cleans the columns, indexes, rename columns to make it readable and understandable.

    Parameters:
        data_1, data_2: strings
            The paths of the files the user wants to load and work with
        
    Returns:
        a DataFrame

    """

    df1 = load_data(data_1, index=1, sheet=1)
    df2 = load_data(data_1, index=1, sheet=2)
    df3 = load_data(data_2, index=1, sheet=1)

    df2  = df1 + df2

    result = merge_dataFrames_index(df2, df3)
    result = result.rename(
        columns={'Adatok': 'Region', 'Összeg': 'Number of students'})
    result.index.name = None
    result = result.rename_axis("Year", axis='columns')

    result = clean_index(result)
    result = clean_regions(result)

    if 'Region' in result.columns:
        for value in result['Region']:
            if value == 'BudapestÖsszeg':
                value_new = 'Budapest'
                result = result.replace({value: value_new})

    return result

def cds_from_regions(df):

    """
    Create the ColumnDataSource for the Bokeh visualization, from datasets containing the regions.

    Parameters:
        df: string
            The DataFrame from which the user wants to create the ColumnDataSource

    Returns:
        ColumnDataSource

    """

    source = ColumnDataSource(data={
        'x': df.index,
        'y': df['Number of students'],
        'Region': df['Region']
    })

    return source

def plot_by_regions(df):

    """
    Create the ColumnDataSource, the figure, the tools, other visualistic elements for the visualizations and plot the data.
    This function is to be used on DataFrames that contains the regions!

    Parameters: 
        df: string
            The name of the DataFrame that the user wants to visualize

    Returns:
        A Bokeh visualization

    """

    regions = df['Region'].unique()
    regions = list(regions)

    source = cds_from_regions(df)

    dot_size = LinearInterpolator(
        x=[df['Number of students'].min(), df['Number of students'].max()],
        y=[5, 25]
    )


    dot_color = CategoricalColorMapper(factors=regions, palette=Category20b_20)

    hover = HoverTool(tooltips=[
        ("Region", "@Region"),
        ("Number of students", "@y"),
        ("Year", "@x"),
    ])

    tools = "pan, tap, box_select, lasso_select, wheel_zoom, help"


    p = figure(plot_height=800, plot_width=800, tools=[hover, tools])
    p.yaxis.formatter.use_scientific = False
    
    p.circle(x='x', y='y', source=source, #legend='Region',
            size={'field': 'y', 'transform': dot_size},
            color=dict(field='Region', transform=dot_color))
    

    return p
    
def cds_from_age(df):

    """
    Create the ColumnDataSource for the Bokeh visualization, from datasets containing the ages of students.

    Parameters:
        df: string
            The DataFrame from which the user wants to create the ColumnDataSource

    Returns:
        ColumnDataSource

    """

    source = ColumnDataSource(data={
        'x': df.index,
        'y': df['Number of students'],
        'Age': df['Age']
    })

    return source

def plot_by_age(df):

    """
    Create the ColumnDataSource, the figure, the tools, other visualistic elements for the visualizations and plot the data.
    This function is to be used on DataFrames that contains the ages of students!

    Parameters: 
        df: string
            The name of the DataFrame that the user wants to visualize

    Returns:
        A Bokeh visualization

    """

    ages = df['Age'].unique()
    ages = list(ages)

    source = cds_from_age(df)

    dot_size = LinearInterpolator(
        x=[df['Number of students'].min(), df['Number of students'].max()],
        y=[5, 25]
    )

    dot_color = CategoricalColorMapper(factors=ages, palette=Category20b_20)

    hover = HoverTool(tooltips=[
        ('Age of students', '@Age'),
        ('Number of students', '@y'),
        ('Year', '@x')
    ])

    tools = "pan, tap, box_select, lasso_select, wheel_zoom, help"

    p = figure(plot_height=800, plot_width=800, tools=[hover, tools], x_range=(2013,2020), y_range=(0,100000))
    p.yaxis.formatter.use_scientific = False
    p.circle(x='x', y='y', source=source,
            size={'field': 'y', 'transform': dot_size},
            color=dict(field='Age', transform=dot_color))

    return p

