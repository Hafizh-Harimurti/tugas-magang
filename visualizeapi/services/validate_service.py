import numpy as np

from visualizeapi.controllers.controller_exception import BadRequest, ResourceNotFound

class ValidateService():
    def __init__(self) -> None:
        self.invalid_data_code = {
            1: 'No matching plot type was found',
            2: 'Invalid values type for plot type',
            3: 'Values dimension(s) mismatch with plot type',
            4: 'Empty values input(s)',
            5: 'Values and categories amount mismatch',
            6: 'Values and data names amount mismatch',
            7: 'Categories of plot type must have one dimension input',
            8: 'Data names must have one dimension input',
            9: 'Null values not allowed for plot type',
            10: 'List cannot be filled with null values only',
            11: 'Categories of plot type must have two dimension input',
            12: 'Values length and plot type mismatch',
            13: 'Categories of plot type only accepts two categories row'
        }

        self.available_plot_type = ['bar', 'histogram', 'scatter', 'line', 'boxplot', 'pie', 'heatmap']

        #Under development: 'bubble'

        self.dimension_for_plot_type = {
            1: ['pie', 'histogram'],
            2: ['bar', 'line', 'boxplot', 'heatmap', 'bubble'],
            3: ['scatter']
        }

        self.data_type_of_plot_type = {
            'bar': [float, int],
            'pie': [float, int],
            'histogram': [float, int, str],
            'boxplot': [float, int],
            'scatter': [float, int],
            'line': [float, int],
            'heatmap': [float, int],
            'bubble': [float, int]
        }

        self.none_allowed_plot_type = ['bar', 'line']

        self.strict_value_length_of_plot_type = {
            'bar': 'Equal',
            'pie': 'None',
            'histogram': 'None',
            'boxplot': 'None',
            'scatter': 2,
            'line': 'None',
            'heatmap': 'Equal',
            'bubble': 3
        }

        self.validate_list_max_depth = max(self.dimension_for_plot_type.keys())
    
    def validate_data(self, data, plot_type):
        if plot_type not in self.available_plot_type:
            return 1
        validation_result = self.validate_list_items(data.values, plot_type)
        if validation_result != 0:
            return validation_result
        if data.data_names is not None and len(data.data_names) != 0:
            if any([type(data_name) is list for data_name in data.data_names]):
                return 8
            if plot_type in ['bar', 'line', 'scatter', 'pie', 'bubble'] and len(data.values) != len(data.data_names):
                return 6
        if data.categories is not None and len(data.categories) != 0:
            if plot_type in ['heatmap']:
                if len(data.categories) != 2:
                    return 13
                elif type(data.categories[0]) is not list or type(data.categories[1]) is not list or any([any([type(sub_category) is list for sub_category in category]) for category in data.categories]):
                    return 11
            else:
                if any([type(category) is list for category in data.categories]):
                    return 7
            if plot_type in ['bar', 'line', 'scatter', 'bubble']:
                if len(data.values[0]) != len(data.categories):
                    return 5
            elif plot_type in ['heatmap']:
                if len(data.values[0]) != len(data.categories[0]) or len(data.values) != len(data.categories[1]):
                    return 5
            else:
                if len(data.values) != len(data.categories):
                    return 5
        return 0

    def validate_list_items(self, data, plot_type, depth = 0):
        validation_result = 0
        if type(data) is list and depth < self.validate_list_max_depth and len(data) > 0:
            data_array = np.array(data, dtype = object)
            if len(data_array[data_array != None]) == 0:
                return 10
            if depth+2 in self.dimension_for_plot_type.keys() and plot_type in self.dimension_for_plot_type[depth+2]:
                if all([type(lower_data) == list for lower_data in data]):
                    lower_data_lengths = [len(lower_data) for lower_data in data]
                    if self.strict_value_length_of_plot_type[plot_type] == 'Equal':
                        longest_data_length = max(lower_data_lengths)
                        if not all([lower_data_length == longest_data_length for lower_data_length in lower_data_lengths]):
                            return 12
                    elif self.strict_value_length_of_plot_type[plot_type] != 'None':
                        if not all([lower_data_length == self.strict_value_length_of_plot_type[plot_type] for lower_data_length in lower_data_lengths]):
                            return 12
            depth += 1
            for item in data:
                validation_result = self.validate_list_items(item, plot_type, depth)
                if validation_result != 0:
                    return validation_result
        elif depth > 0 and type(data) is not list:
            if depth not in self.dimension_for_plot_type.keys() or plot_type not in self.dimension_for_plot_type[depth]:
                return 3
            elif type(data) not in self.data_type_of_plot_type[plot_type]:
                if data is None:
                    if plot_type in self.none_allowed_plot_type:
                        return 0
                    else:
                        return 9
                else:
                    return 2
            else:
                return 0
        elif depth == self.validate_list_max_depth:
            return 3
        elif len(data) == 0:
            return 4
        return validation_result