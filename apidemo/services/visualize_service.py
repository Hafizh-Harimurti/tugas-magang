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
        if plot_type in ['bar', 'line', 'scatter', 'boxplot', 'histogram']:
            result['xAxis'] = self.set_x_axis(plot_type, data.x_axis_name, custom_settings)
            result['yAxis'] = self.set_y_axis(data.values, plot_type, data.y_axis_name, custom_settings)
            result['grid'] = self.set_grid(plot_type)
        if plot_type in ['pie']:
            result['label'] = self.set_label(plot_type)
        if plot_type in ['bar', 'line', 'scatter', 'pie', 'boxplot']:
            result['legend'] = self.set_legend(plot_type)
        return result

    def set_title(self, title, subtitle, plot_type):
        if plot_type in ['pie', 'bar', 'histogram', 'scatter', 'line', 'boxplot']:
            return {
                'text': title,
                'subtext': subtitle,
                'left': 'center'
            }
        else:
            return {}

    def set_x_axis(self, plot_type, x_axis_name, custom_settings):
        x_axis_option = {}
        if plot_type in ['histogram', 'line', 'bar']:
            x_axis_option = {
                'type': 'category',
                'name': x_axis_name,
                'nameLocation': 'center',
                'nameGap': 30,
                'nameTextStyle': {
                    'fontSize': 14
                }
            }
        elif plot_type in ['boxplot']:
            x_axis_option = {
                'type': 'value',
                'name': x_axis_name,
                'nameLocation': 'center',
                'nameGap': 30,
                'nameTextStyle': {
                    'fontSize': 14
                }
            }
        elif plot_type in ['scatter']:
            x_axis_option = {
                'type': 'value',
                'name': x_axis_name,
                'nameLocation': 'center',
                'nameGap': 30,
                'nameTextStyle': {
                    'fontSize': 14
                },
                'min': custom_settings.x_axis_start if custom_settings.x_axis_start is not None else 0,
            }
            if custom_settings.x_axis_end is not None:
                x_axis_option['max'] = custom_settings.x_axis_end
        return x_axis_option

    def set_y_axis(self, data, plot_type, y_axis_name, custom_settings):
        y_axis_option = {}
        if plot_type in ['histogram']:
            y_axis_option = {
                'type': 'value',
                'name': y_axis_name,
                'nameLocation': 'end',
                'nameGap': 30,
                'nameTextStyle': {
                    'fontSize': 14
                }
            }
        elif plot_type in ['scatter']:
            y_axis_option = {
                'type': 'value',
                'name': y_axis_name,
                'nameLocation': 'end',
                'nameGap': 30,
                'nameTextStyle': {
                    'fontSize': 14
                },
                'min': custom_settings.y_axis_start if custom_settings.y_axis_start is not None else 0
            }
            if custom_settings.y_axis_end is not None:
                y_axis_option['max'] = custom_settings.y_axis_end
        elif plot_type in ['boxplot']:
            y_axis_option = {
                'type': 'category',
                'boundaryGap': 'true',
                'name': y_axis_name,
                'nameLocation': 'end',
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
            y_axis_option = {
                'type': 'value',
                'name': y_axis_name,
                'nameLocation': 'end',
                'nameGap': 30,
                'nameTextStyle': {
                    'fontSize': 14
                },
                'min': custom_settings.y_axis_start if custom_settings.y_axis_start is not None else 0,
                'max': plot_y_max
            }
            if custom_settings.y_axis_end is not None:
                y_axis_option['max'] = custom_settings.y_axis_end
        return y_axis_option

    def set_grid(self, plot_type):
        grid_option = {}
        if plot_type in ['bar', 'scatter', 'line', 'boxplot']:
            grid_option = {
                'top': '20%'
            }
        elif plot_type in ['histogram']:
            grid_option = {
                'top': '10%'
            }
        return grid_option

    def set_tooltip(self, plot_type):
        tooltip_option = {}
        if plot_type in ['scatter']:
            tooltip_option = {
                'trigger': 'item',
                'formatter': '{a}: ({c})'
            }
        elif plot_type in ['pie']:
            tooltip_option = {
                'trigger': 'item',
                'formatter' : '{a}<br/>{b}: {c} ({d}%)'
            }
        elif plot_type in ['bar', 'line']:
            tooltip_option = {
                'trigger': 'axis'
            }
        elif plot_type in ['histogram', 'boxplot']:
            tooltip_option = {
                'trigger': 'item'
            }
        return tooltip_option

    def set_legend(self, plot_type):
        legend_option = {}
        if plot_type in ['pie', 'bar', 'scatter', 'line', 'boxplot']:
            legend_option = {
                'left': 'center',
                'top': '10%'
            }
        return legend_option

    def set_label(self, plot_type):
        label_option = {}
        if plot_type in ['pie']:
            label_option = {
                "formatter": "  {a|{b}: {c} ({d}%)}  ",
                "backgroundColor": "#FAFAFA",
                "borderColor": "#888888",
                "borderWidth": 1,
                "borderRadius": 4,
                "rich": {
                    "a": {
                        "color": "#000000",
                        "lineHeight": 33,
                        "fontSize": 14,
                        "align": "center"
                    }
                }
            }
        return label_option

    def set_series(self, data, plot_type, data_names, title):
        series_option = {}
        if plot_type in ['histogram']:
            series_option = {
                'name': title,
                'type': 'bar'
            }
        elif plot_type in ['boxplot']:
            series_option = [
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
            series_option = {
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
            series_option = all_series
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
            series_option = all_series
        return series_option

    def set_dataset(self, data, plot_type, categories, custom_settings):
        dataset_option = {}
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
            dataset_option = [
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
            dataset_option = datasets
        elif plot_type in ['histogram']:
            frequency_list = list()
            current_start = custom_settings.start if custom_settings.start is not None and custom_settings.start < custom_settings.end else min(data)
            histogram_end = custom_settings.end if custom_settings.end is not None and custom_settings.start < custom_settings.end else max(data)
            histogram_range = custom_settings.bins if custom_settings.bins else (histogram_end - current_start)/custom_settings.category_amount
            while True:
                frequency_list.append([str(current_start) + '-' + str(current_start + histogram_range), [current_start <= value < current_start + histogram_range for value in data].count(True)])
                current_start += histogram_range
                if current_start == histogram_end:
                    frequency_list[-1][1] += data.count(current_start) 
                if current_start >= histogram_end:
                    break
            dataset_option = {
                'id': 'histogram_data',
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
            dataset_option = datasets
        return dataset_option