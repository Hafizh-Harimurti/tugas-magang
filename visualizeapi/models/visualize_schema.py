from ninja import Schema

class Data(Schema):
    title: str = ''
    subtitle: str = ''
    x_axis_name: str = ''
    y_axis_name: str = ''
    values: list = None
    categories: list = None
    data_names: list = None

class CustomSettings(Schema):
    x_axis_start: float = None
    x_axis_end: float = None
    y_axis_start: float = None
    y_axis_end: float = None
    start: float = None
    end: float = None
    bins: float = None
    category_amount: int = 10
    symbol_size_min: int = 10
    symbol_size_max: int = 100
    orientation: str = 'vertical'
    show_legend: bool = True
    enable_zoom: bool = True,
    enable_save: bool = True

class ResponseMessage(Schema):
    status: int
    message: str
    payload: dict = {}