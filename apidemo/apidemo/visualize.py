import numpy as np

invalid_data_code = {
    1: 'Data and categories amount mismatch',
    2: 'Invalid data type for plot type',
    3: 'Data dimension(s) mismatch with plot type',
    4: 'Empty data input(s)'
}

dimension_for_plot_type = {
    1: ['pie', 'hist'],
    2: ['bar', 'line', 'boxplot'],
    3: ['scatter']
}

data_type_of_plot_type = {
    'bar': [float, int],
    'pie': [float, int],
    'hist': [float, int, str],
    'boxplot': [float, int],
    'scatter': [float, int],
    'line': [float, int]
}

validate_list_max_depth = max(dimension_for_plot_type.keys())

def visualizeData(data, custom_settings):
    if type(data.values) is not list:
        return {
            'message': 'Data must be a list'
        }
    validation_result = validateData(data.values, data.plot_type, data.categories)
    if validation_result != 0:
        return {
            'message': invalid_data_code[validation_result]
        }
    if data.categories is None:
        if data.plot_type in ['bar', 'line']:
            categories = [category_value for category_value in range(len(data.values[0]))]
        else:
            categories = [category_value for category_value in range(len(data.values))]
    else:
        categories = data.categories
    result = {
        'title': {
            'text': data.title,
            'subtext': data.subtitle,
            'left': 'center'
        },
        'dataset': setDataset(data.values, data.plot_type, categories, custom_settings),
        'series': setSeries(data.values, data.plot_type)
    }
    if data.plot_type not in ['pie']:
        result['xAxis'] = setxAxis(data.plot_type)
        result['yAxis'] = setyAxis(data.plot_type)
    return result

def validateData(data, plot_type, categories):
    validation_result = validateListItems(data, plot_type)
    if categories is not None:
        if plot_type in ['bar', 'line'] and len(data[0]) != len(categories):
            validation_result = 1
        elif len(data) != len(categories):
            validation_result = 1
    return validation_result

def validateListItems(data, plot_type, depth = 0):
    validation_result = 0
    if type(data) is list and depth < validate_list_max_depth and len(data) > 0:
        depth += 1
        for item in data:
            validation_result = validateListItems(item, plot_type, depth)
            if validation_result != 0:
                return validation_result
    elif depth > 0 and type(data) is not list:
        if depth not in dimension_for_plot_type.keys() or plot_type not in dimension_for_plot_type[depth]:
            return 3
        elif type(data) not in data_type_of_plot_type[plot_type]:
            return 2
        else:
            return 0
    elif depth == validate_list_max_depth:
        return 3
    elif len(data) == 0:
        return 4
    return validation_result

def setxAxis(plot_type):
    if plot_type in ['hist', 'line', 'bar']:
        return {
            'type': 'category'
        }
    elif plot_type in ['scatter', 'boxplot']:
        return {
            'type': 'value'
        }
    else:
        return {}

def setyAxis(plot_type):
    if plot_type in ['bar', 'scatter', 'line', 'hist']:
        return {
            'type': 'value'
        }
    elif plot_type in ['boxplot']:
        return {
            'type': 'category',
            'boundaryGap': 'true',
            'splitArea': {
                'show': 'false'
            }
        }
    else: 
        return {}

def setSeries(data, plot_type):
    if plot_type in ['hist']:
        return {
            'name': 'histogram',
            'type': 'bar'
        }
    elif plot_type in ['boxplot']:
        return [
            {
                'name': 'boxplot',
                'type': 'boxplot',
                'datasetId': 'boxplot_data',
                'dimensions': ['Minimum', 'Q1', 'Median', 'Q3', 'Maximum'],
                'encode':{
                    'tooltip': ['Minimum', 'Q1', 'Median', 'Q3', 'Maximum']
                    }
            }
        ] + [
            {
                'name': 'outliers',
                'type': 'scatter',
                'datasetId': 'boxplot_outliers'
            }       
        ]
    elif plot_type in ['pie']:
        return {
            'name': 'pie',
            'type': 'pie',
            'datasetId': 'pie_data',
            'radius': '50%'
        }
    elif plot_type in ['bar', 'line']:
        all_series = list()
        for line_index in range(len(data)):
            all_series.append(
                {
                    'name': plot_type + '_' + str(line_index),
                    'type': plot_type,
                    'datasetId': plot_type +  '_' + str(line_index) + '_data'
                }
            )
        return all_series
    elif plot_type in ['scatter']:
        all_series = list()
        for scatter_index in range(len(data)):
            all_series.append(
                {
                    'name': 'scatter_' + str(scatter_index),
                    'type': 'scatter',
                    'datasetId': 'scatter_' + str(scatter_index) + '_data'
                }
            )
        return all_series
    else:
        return {}

def setDataset(data, plot_type, categories, custom_settings):
    if plot_type in ['boxplot']:
        data_rows = list()
        data_outliers = list()
        for data_index in range(len(data)):
            data_array = np.array(data[data_index])
            boxplot_Q1 = np.percentile(data_array, 25)
            boxplot_median = np.median(data_array)
            boxplot_Q3 = np.percentile(data_array, 75)
            boxplot_iqr = boxplot_Q3 - boxplot_Q1
            boxplot_min = boxplot_Q1 - 1.5*boxplot_iqr
            boxplot_max = boxplot_Q3 + 1.5*boxplot_iqr
            boxplot_outliers = data_array[(data_array < boxplot_Q1 - 1.5*boxplot_iqr) | (data_array > boxplot_Q3 + 1.5*boxplot_iqr)]
            data_rows.append([categories[data_index], boxplot_min, boxplot_Q1, boxplot_median, boxplot_Q3, boxplot_max])
            for outlier in boxplot_outliers:
                data_outliers.append([categories[data_index], float(outlier)])
        ordered_datasets = list()
        for value_index, boxplot_value in enumerate(['min','Q1','median','Q3','max']):
            ordered_datasets.append(
                {
                    'id': boxplot_value + '_asc',
                    'fromDatasetId': 'boxplot_data',
                    'transform': {
                        'type': 'sort',
                        'config': {
                            'dimension': value_index + 1,
                            'order': 'asc'
                        }
                    }
                }
            )
        return [
            {
                'id': 'boxplot_data',
                'source': data_rows
            }
        ] + ordered_datasets + [
            {
                'id': 'boxplot_outliers',
                'source': data_outliers
            }
        ]
    elif plot_type in ['pie']:
        pie_data = list()
        for data_index in range(len(data)):
            pie_data.append({'value': data[data_index], 'name': categories[data_index]})
        return {
            'id': 'pie_data',
            'source': pie_data
        }
    elif plot_type in ['bar', 'line']:
        datasets = list()
        for line_index in range(len(data)):
            data_row = list()
            for data_index in range(len(data[line_index])):
                data_row.append([categories[data_index],data[line_index][data_index]])
            datasets.append(
                {
                    'id': plot_type + '_' + str(line_index) + '_data',
                    'source': data_row
                }
            )
        return datasets
    elif plot_type in ['hist']:
        frequency_list = list()
        current_start = custom_settings.start if custom_settings.start is not None else min(data)
        hist_end = custom_settings.end if custom_settings.end is not None else max(data)
        hist_range = custom_settings.bins if custom_settings.bins else (hist_end - current_start)/custom_settings.category_amount
        while True:
            frequency_list.append([str(current_start) + '-' + str(current_start + hist_range), [current_start <= value < current_start + hist_range for value in data].count(True)])
            current_start += hist_range
            if current_start == max(data):
                frequency_list[-1] += data.count(current_start)
            if current_start >= max(data):
                break
        return {
            'id': 'hist_data',
            'source': frequency_list
        }
    elif plot_type in ['scatter']:
        datasets = list()
        for scatter_index in range(len(data)):
            datasets.append(
                {
                    'id': 'scatter_' + str(scatter_index) + '_data',
                    'source': data[scatter_index]
                }
            )
        return datasets
    else:
        return {}