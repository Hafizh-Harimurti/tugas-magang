import numpy as np
import math

class VisualizeService():
    def __init__(self) -> None:
        pass

    def visualize_data(self, data, plot_type, custom_settings):
        if data.categories is None or len(data.categories) == 0:
            if plot_type in ['bar', 'line']:
                categories = [category_value for category_value in range(len(data.values[0]))]
            else:
                categories = [category_value for category_value in range(len(data.values))]
        else:
            categories = data.categories
        if (data.data_names is None or len(data.data_names) == 0) and plot_type in ['bar', 'line', 'scatter', 'pie']:
            data_names = [data_name_value for data_name_value in range(len(data.values))]
        else:
            data_names = data.data_names
        result = {
            'title': self.set_title(data.title, data.subtitle, plot_type),
            'dataset': self.set_dataset(data.values, plot_type, categories, custom_settings),
            'series': self.set_series(data.values, plot_type, data_names, data.title),
            'tooltip': self.set_tooltip(plot_type)
        }
        if plot_type in ['bar', 'line', 'scatter', 'boxplot', 'hist']:
            result['xAxis'] = self.set_x_axis(plot_type, data.x_axis_name)
            result['yAxis'] = self.set_y_axis(data.values, plot_type, data.y_axis_name)
            result['grid'] = self.set_grid(plot_type)
        if plot_type in ['pie']:
            result['label'] = self.set_label(plot_type)
        if plot_type in ['bar', 'line', 'scatter', 'pie', 'boxplot']:
            result['legend'] = self.set_legend(plot_type)
        return result

    def set_title(self, title, subtitle, plot_type):
        if plot_type in ['pie', 'bar', 'hist', 'scatter', 'line', 'boxplot']:
            return {
                'text': title,
                'subtext': subtitle,
                'left': 'center'
            }
        else:
            return {}

    def set_x_axis(self, plot_type, x_axis_name):
        if plot_type in ['hist', 'line', 'bar']:
            return {
                'type': 'category',
                'name': x_axis_name,
                'nameLocation': 'center',
                'nameGap': 30,
                'nameTextStyle': {
                    'fontSize': 14
                }
            }
        elif plot_type in ['scatter', 'boxplot']:
            return {
                'type': 'value',
                'name': x_axis_name,
                'nameLocation': 'center',
                'nameGap': 30,
                'nameTextStyle': {
                    'fontSize': 14
                }
            }
        else:
            return {}

    def set_y_axis(self, data, plot_type, y_axis_name):
        if plot_type in ['hist', 'scatter']:
            return {
                'type': 'value',
                'name': y_axis_name,
                'nameLocation': 'center',
                'nameGap': 30,
                'nameTextStyle': {
                    'fontSize': 14
                }
            }
        elif plot_type in ['boxplot']:
            return {
                'type': 'category',
                'boundaryGap': 'true',
                'name': y_axis_name,
                'nameLocation': 'center',
                'nameGap': 30,
                'nameTextStyle': {
                    'fontSize': 14
                }
            }
        elif plot_type in ['line', 'bar']:
            data_array = np.array(data)
            data_max = np.amax(data_array[data_array != None])
            data_max_log_floored = math.floor(math.log10(data_max))
            plot_y_max = math.ceil(data_max / 10**data_max_log_floored * (1 + 10**(data_max_log_floored-6))) * 10**data_max_log_floored
            return {
                'type': 'value',
                'name': y_axis_name,
                'nameLocation': 'center',
                'nameGap': 30,
                'nameTextStyle': {
                    'fontSize': 14
                },
                'max': plot_y_max
            }
        else: 
            return {}

    def set_grid(self, plot_type):
        if plot_type in ['bar', 'scatter', 'line', 'boxplot']:
            return {
                'top': '20%'
            }
        elif plot_type in ['hist']:
            return {
                'top': '10%'
            }
        else:
            return {}

    def set_tooltip(self, plot_type):
        if plot_type in ['scatter']:
            return {
                'trigger': 'item',
                'formatter': '{a}: ({c})'
            }
        elif plot_type in ['pie']:
            return {
                'trigger': 'item',
                'formatter' : '{a}<br/>{b}: {c} ({d}%)'
            }
        elif plot_type in ['bar', 'line']:
            return {
                'trigger': 'axis'
            }
        elif plot_type in ['hist', 'boxplot']:
            return {
                'trigger': 'item'
            }
        else:
            return {}

    def set_legend(self, plot_type):
        if plot_type in ['pie', 'bar', 'scatter', 'line', 'boxplot']:
            return {
                'left': 'center',
                'top': '10%'
            }
        elif plot_type in []:
            return {
                'left': 'center'
            }

    def set_label(self, plot_type):
        if plot_type in ['pie']:
            return {
                'formatter': '{a|{a}}\n{hr|}\n  {b|{b}: } {c|{c}} {per|({d}%)}  ',
                'backgroundColor': '#FAFAFA',
                'borderColor': '#888888',
                'borderWidth': 1,
                'borderRadius': 4,
                'rich':{
                    'a': {
                        'color': '#505050',
                        'lineHeight': 22,
                        'align': 'center'
                    },
                    'hr': {
                        'borderColor': '#888888',
                        'width': '100%',
                        'borderWidth': 1,
                        'height': 0
                    },
                    'b': {
                        'color': '#000000',
                        'lineHeight': 33,
                        'fontSize': 14,
                        'fontWeight': 'bold',
                        'align': 'center'
                    },
                    'c': {
                        'color': '#000000',
                        'fontSize': 14,
                        'align': 'center'
                    },
                    'per': {
                        'color': '#FFFFFF',
                        'backgroundColor': '#5D5D5D',
                        'borderRadius': 4,
                        'padding': [3,4],
                        'align': 'center'
                    }
                }
            }
        else:
            return {}

    def set_series(self, data, plot_type, data_names, title):
        if plot_type in ['hist']:
            return {
                'name': title,
                'type': 'bar'
            }
        elif plot_type in ['boxplot']:
            return [
                {
                    'name': 'Boxplot',
                    'type': 'boxplot',
                    'datasetId': 'boxplot_data',
                    'dimensions': ['Category', 'Minimum', 'Q1', 'Median', 'Q3', 'Maximum'],
                    'encode':{
                        'x': ['Minimum', 'Q1', 'Median', 'Q3', 'Maximum'],
                        'y': ['Category'],
                        'tooltip': ['Minimum', 'Q1', 'Median', 'Q3', 'Maximum']
                        }
                }
            ] + [
                {
                    'name': 'Outliers',
                    'type': 'scatter',
                    'datasetId': 'boxplot_outliers'
                }       
            ]
        elif plot_type in ['pie']:
            pie_data = list()
            for data_index in range(len(data)):
                pie_data.append({'value': data[data_index], 'name': data_names[data_index]})
            return {
                'name': title,
                'type': 'pie',
                'datasetId': 'pie_data',
                'radius': '80%',
                'top': '20%',
                'selectedMode': 'single',
                'data': pie_data
            }
        elif plot_type in ['bar', 'line']:
            all_series = list()
            for line_index in range(len(data)):
                all_series.append(
                    {
                        'name': data_names[line_index] if data_names else (plot_type + '_' + str(line_index)),
                        'type': plot_type,
                        'datasetId': plot_type +  '_' + str(line_index) + '_data'
                    }
                )
            return all_series
        elif plot_type in ['scatter']:
            all_series = list()
            for line_index in range(len(data)):
                all_series.append(
                    {
                        'name': data_names[line_index] if data_names else ('scatter_' + str(line_index)),
                        'type': 'scatter',
                        'datasetId': 'scatter_' + str(line_index) + '_data'
                    }
                )
            return all_series
        else:
            return {}

    def set_dataset(self, data, plot_type, categories, custom_settings):
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
                data_rows.append([str(categories[data_index]), boxplot_min, boxplot_Q1, boxplot_median, boxplot_Q3, boxplot_max])
                for outlier in boxplot_outliers:
                    data_outliers.append([categories[data_index], float(outlier)])
            ordered_datasets = list()
            #
            #for value_index, boxplot_value in enumerate(['min','Q1','median','Q3','max']):
            #    ordered_datasets.append(
            #        {
            #            'id': boxplot_value + '_asc',
            #            'fromDatasetId': 'boxplot_data',
            #            'transform': {
            #                'type': 'sort',
            #                'config': {
            #                    'dimension': value_index + 1,
            #                    'order': 'asc'
            #                }
            #            }
            #        }
            #    )
            #
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
                    frequency_list[-1][1] += data.count(current_start) 
                if current_start >= max(data):
                    break
            return {
                'id': 'hist_data',
                'source': frequency_list
            }
        elif plot_type in ['scatter']:
            datasets = list()
            for line_index in range(len(data)):
                datasets.append(
                    {
                        'id': 'scatter_' + str(line_index) + '_data',
                        'source': data[line_index]
                    }
                )
            return datasets
        else:
            return {}