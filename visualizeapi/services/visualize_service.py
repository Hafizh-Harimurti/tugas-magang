import numpy as np
import math

class VisualizeService():
    def __init__(self) -> None:
        pass

    def visualize_data(self, data, plot_type, custom_settings):

        #Generate categories if no categories is sent
        if data.categories is None or len(data.categories) == 0:
            if plot_type in ['bar', 'line', 'area']:
                categories = [category_value for category_value in range(len(data.values[0]))]
            elif plot_type in ['heatmap']:
                categories = [[category_x_value for category_x_value in range(len(data.values[0]))], [category_y_value for category_y_value in range(len(data.values))]]
            else:
                categories = [category_value for category_value in range(len(data.values))]
        else:
            categories = data.categories

        #Generate data names if no data names is sent
        if (data.data_names is None or len(data.data_names) == 0) and plot_type in ['bar', 'line', 'scatter', 'pie', 'bubble', 'area']:
            data_names = [data_name_value for data_name_value in range(len(data.values))]
        else:
            data_names = data.data_names

        #Generate option
        result = {
            'title': self.set_title(data.title, data.subtitle, plot_type),
            'dataset': self.set_dataset(data.values, plot_type, categories, data_names, custom_settings),
            'series': self.set_series(data.values, plot_type, data_names, data.title, custom_settings),
            'toolbox': self.set_toolbox(plot_type, custom_settings),
            'tooltip': self.set_tooltip(plot_type)
        }
        if plot_type in ['bar', 'line', 'scatter', 'boxplot', 'histogram', 'heatmap', 'bubble', 'area']:
            result['xAxis'] = self.set_x_axis(data.values, plot_type, data.x_axis_name, categories, custom_settings)
            result['yAxis'] = self.set_y_axis(data.values, plot_type, data.y_axis_name, categories, custom_settings)
            result['grid'] = self.set_grid(plot_type)
        if plot_type in ['pie']:
            result['label'] = self.set_label(plot_type)
        if plot_type in ['pie']:
            result['emphasis'] = self.set_emphasis(plot_type)
        if plot_type in ['bar', 'line', 'scatter', 'pie', 'boxplot', 'bubble', 'area'] and custom_settings.show_legend:
            result['legend'] = self.set_legend(plot_type)
        if plot_type in ['heatmap', 'bubble']:
            result['visualMap'] = self.set_visual_map(plot_type, data.values, custom_settings)

        return result

    def set_title(self, title, subtitle, plot_type):
        title_option = {}
        if plot_type in ['pie', 'bar', 'histogram', 'scatter', 'line', 'boxplot', 'heatmap', 'bubble', 'area']:
            title_option = {
                'text': title,
                'subtext': subtitle,
                'left': 'center'
            }
        return title_option

    def set_dataset(self, data, plot_type, categories, data_names, custom_settings):
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
            dataset_option = [
                {
                    'id': 'boxplot_data',
                    'source': data_rows
                }
            ] + [
                {
                    'id': 'boxplot_outliers',
                    'source': data_outliers
                }
            ]
        elif plot_type in ['bar', 'line', 'area']:
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
        elif plot_type in ['scatter', 'bubble']:
            datasets = list()
            for line_index in range(len(data)):
                datasets.append(
                    {
                        'id': plot_type + '_' + str(line_index) + '_data',
                        'source': data[line_index]
                    }
                )
            dataset_option = datasets
        elif plot_type in ['heatmap']:
            modified_data = list()
            for row_index, row_value in enumerate(data):
                for column_index, column_value in enumerate(row_value):
                    modified_data.append([column_index, row_index, column_value if column_value != 0 else '-'])
            dataset_option = {
                'id': 'heatmap_data',
                'source': modified_data
            }
        return dataset_option
    
    def set_series(self, data, plot_type, data_names, title, custom_settings):
        series_option = {}
        if plot_type in ['histogram']:
            series_option = {
                'name': title,
                'type': 'bar',
                'barWidth': '104%',
                'datasetId': 'histogram_data'
            }
        elif plot_type in ['boxplot']:
            series_option = [
                {
                    'name': 'Boxplot',
                    'type': 'boxplot',
                    'datasetId': 'boxplot_data',
                    'dimensions': ['Category', 'Minimum', 'Q1', 'Median', 'Q3', 'Maximum'],
                    'encode':{
                        'x': ['Minimum', 'Q1', 'Median', 'Q3', 'Maximum'] if custom_settings.orientation == 'horizontal' else ['Category'],
                        'y': ['Category'] if custom_settings.orientation == 'horizontal' else ['Minimum', 'Q1', 'Median', 'Q3', 'Maximum'],
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
        elif plot_type in ['area']:
            all_series = list()
            for line_index in range(len(data)):
                all_series.append(
                    {
                        'name': data_names[line_index] if data_names else (plot_type + '_' + str(line_index)),
                        'type': 'line',
                        'datasetId': plot_type +  '_' + str(line_index) + '_data',
                        'areaStyle': {}
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
        elif plot_type in ['heatmap']:
            series_option = {
                'name': title,
                'type': 'heatmap',
                'datasetId': 'heatmap_data',
                'label': {
                    'show': 'true'
                }
            }
        elif plot_type in ['bubble']:
            all_series = list()
            for line_index in range(len(data)):
                all_series.append(
                    {
                        'name': data_names[line_index] if data_names else ('bubble_' + str(line_index)),
                        'type': 'scatter',
                        'datasetId': 'bubble_' + str(line_index) + '_data',
                        'dimensions': ['X', 'Y', 'Value'],
                        'encode': {
                            'tooltip': ['X', 'Y', 'Value']
                        }
                    }
                )
            series_option = all_series
        return series_option

    def set_toolbox(self, plot_type, custom_settings):
        toolbox_option = {}
        toolbox_feature = {}
        if custom_settings.enable_zoom:
            if plot_type in ['scatter', 'bubble']:
                toolbox_feature['dataZoom'] = {}
            elif plot_type in ['line', 'bar', 'histogram', 'area']:
                toolbox_feature['dataZoom'] = {
                    'yAxisIndex': 'none'
                }
            elif plot_type in ['boxplot']:
                toolbox_feature['dataZoom'] = {
                    'xAxisIndex': 'none'
                }
        if custom_settings.enable_save:
            toolbox_feature['saveAsImage'] = {}
        toolbox_option['feature'] = toolbox_feature
        return toolbox_option

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
        elif plot_type in ['bar', 'line', 'area']:
            tooltip_option = {
                'trigger': 'axis'
            }
        elif plot_type in ['histogram', 'boxplot', 'heatmap']:
            tooltip_option = {
                'trigger': 'item'
            }
        return tooltip_option

    def set_x_axis(self, data, plot_type, x_axis_name, categories, custom_settings):
        x_axis_option = {}
        if plot_type in ['bar']:
            if custom_settings.orientation == 'horizontal':
                data_array = np.array(data)
                data_max = np.amax(data_array[data_array != None])
                data_max_log_floored = math.floor(math.log10(data_max))
                plot_x_max = math.ceil(data_max / 10**data_max_log_floored * (1 + 10**(data_max_log_floored-6))) * 10**data_max_log_floored
                x_axis_option = {
                    'type': 'value',
                    'name': x_axis_name,
                    'nameLocation': 'end',
                    'nameGap': 30,
                    'nameTextStyle': {
                        'fontSize': 14
                    },
                    'min': custom_settings.x_axis_start if custom_settings.x_axis_start is not None else 0,
                    'max': plot_x_max
                }
                if custom_settings.x_axis_end is not None:
                    x_axis_option['max'] = custom_settings.x_axis_end
            else:
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
            if custom_settings.orientation == 'horizontal':
                x_axis_option = {
                    'type': 'value',
                    'name': x_axis_name,
                    'nameLocation': 'center',
                    'nameGap': 30,
                    'nameTextStyle': {
                        'fontSize': 14
                    }
                }
            else:
                x_axis_option = {
                    'type': 'category',
                    'boundaryGap': 'true',
                    'name': x_axis_name,
                    'nameLocation': 'end',
                    'nameGap': 30,
                    'nameTextStyle': {
                        'fontSize': 14
                    }
                }
        elif plot_type in ['histogram']:
            if custom_settings.orientation == 'horizontal':
                x_axis_option = {
                    'type': 'value',
                    'name': x_axis_name,
                    'nameLocation': 'end',
                    'nameGap': 30,
                    'nameTextStyle': {
                        'fontSize': 14
                    }
                }
            else:
                x_axis_option = {
                    'type': 'category',
                    'name': x_axis_name,
                    'nameLocation': 'center',
                    'nameGap': 30,
                    'nameTextStyle': {
                        'fontSize': 14
                    }
                }
        elif plot_type in ['line', 'area']:
            x_axis_option = {
                'type': 'category',
                'name': x_axis_name,
                'nameLocation': 'center',
                'nameGap': 30,
                'nameTextStyle': {
                    'fontSize': 14
                }
            }
        elif plot_type in ['scatter', 'bubble']:
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
        elif plot_type in ['heatmap']:
            x_axis_option = {
                'type': 'category',
                'name': x_axis_name,
                'nameLocation': 'center',
                'nameGap': 30,
                'nameTextStyle': {
                    'fontSize': 14
                },
                'data': categories[0],
                'splitArea': {
                    'show': 'true'
                }
            }
        return x_axis_option

    def set_y_axis(self, data, plot_type, y_axis_name, categories, custom_settings):
        y_axis_option = {}
        if plot_type in ['bar']:
            if custom_settings.orientation == 'horizontal':
                y_axis_option = {
                    'type': 'category',
                    'name': y_axis_name,
                    'nameLocation': 'center',
                    'nameGap': 30,
                    'nameTextStyle': {
                        'fontSize': 14
                    },
                    'axisLabel':{
                        'rotate': 90
                    }
                }
            else:
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
        elif plot_type in ['boxplot']:
            if custom_settings.orientation == 'horizontal':
                y_axis_option = {
                    'type': 'category',
                    'boundaryGap': 'true',
                    'name': y_axis_name,
                    'nameLocation': 'end',
                    'nameGap': 30,
                    'nameTextStyle': {
                        'fontSize': 14
                    },
                    'axisLabel':{
                        'rotate': 90
                    }
                }
            else:
                y_axis_option = {
                    'type': 'value',
                    'name': y_axis_name,
                    'nameLocation': 'center',
                    'nameGap': 30,
                    'nameTextStyle': {
                        'fontSize': 14
                    },
                }
        elif plot_type in ['histogram']:
            if custom_settings.orientation == 'horizontal':
                y_axis_option = {
                    'type': 'category',
                    'name': y_axis_name,
                    'nameLocation': 'center',
                    'nameGap': 30,
                    'nameTextStyle': {
                        'fontSize': 14
                    },
                    'axisLabel':{
                        'rotate': 90
                    }
                }
            else:
                y_axis_option = {
                    'type': 'value',
                    'name': y_axis_name,
                    'nameLocation': 'end',
                    'nameGap': 30,
                    'nameTextStyle': {
                        'fontSize': 14
                    }
                }
        elif plot_type in ['line', 'area']:
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
        elif plot_type in ['scatter', 'bubble']:
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
        elif plot_type in ['heatmap']:
            y_axis_option = {
                'type': 'category',
                'boundaryGap': 'true',
                'name': y_axis_name,
                'nameLocation': 'end',
                'nameGap': 30,
                'nameTextStyle': {
                    'fontSize': 14
                },
                'splitArea':{
                    'show': 'true'
                },
                'data': categories[1]
            }
        return y_axis_option

    def set_grid(self, plot_type):
        grid_option = {}
        if plot_type in ['bar', 'scatter', 'line', 'histogram', 'boxplot', 'area']:
            grid_option = {
                'top': '20%'
            }
        elif plot_type in ['heatmap']:
            grid_option = {
                'top': '15%',
                'height': '50%'
            }
        elif plot_type in ['bubble']:
            grid_option = {
                'top': '20%',
                'right': '15%'
            }
        return grid_option
    
    def set_label(self, plot_type):
        label_option = {}
        if plot_type in ['pie']:
            label_option = {
                'formatter': '  {a|{b}: {c} ({d}%)}  ',
                'backgroundColor': '#FAFAFA',
                'borderColor': '#888888',
                'borderWidth': 1,
                'borderRadius': 4,
                'rich': {
                    'a': {
                        'color': '#000000',
                        'lineHeight': 33,
                        'fontSize': 14,
                        'align': 'center'
                    }
                }
            }
        elif plot_type in ['bubble']:
            label_option = {
                'formatter': '{@Name}',
                'show': True
            }
        return label_option

    def set_emphasis(self, plot_type):
        emphasis_option = {}
        if plot_type in ['pie']:
            emphasis_option = {
                'focus': 'self'
            }
        return emphasis_option

    def set_legend(self, plot_type):
        legend_option = {}
        if plot_type in ['pie', 'bar', 'scatter', 'line', 'boxplot', 'bubble', 'area']:
            legend_option = {
                'left': 'center',
                'top': '10%'
            }
        return legend_option

    def set_visual_map(self, plot_type, data, custom_settings):
        visual_map_option = {}
        if plot_type in ['heatmap']:
            visual_map_option = {
                'min': min([min(single_data) for single_data in data]),
                'max': max([max(single_data) for single_data in data]),
                'calculable': 'true',
                'orient': 'horizontal',
                'left': 'center',
                'bottom': '15%'
            }
        elif plot_type in ['bubble']:

            #Adjusts bubble size in bubble plot
            bubble_size_data = list()
            for data_group in data:
                bubble_size_data.append(np.array(data_group).T[2])
            visual_map_option = {
                'show': False,
                'dimension': 'Value',
                'min': np.min(bubble_size_data),
                'max': np.max(bubble_size_data),
                'inRange': {
                    'symbolSize': [custom_settings.symbol_size_min, custom_settings.symbol_size_max]
                }
            }
        return visual_map_option