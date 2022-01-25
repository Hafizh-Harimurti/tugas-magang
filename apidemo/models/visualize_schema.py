from ninja import Schema

class Data(Schema):
    title: str = ''
    subtitle: str = ''
    x_axis_name: str = ''
    y_axis_name: str = ''
    values: list = None
    plot_type: str = None
    categories: list = None
    data_names: list = None

class CustomSettings(Schema):
    start: float = None
    end: float = None
    bins: float = None
    category_amount: int = 10

class ResponseMessage(Schema):
    status: int
    message: str

class SuccessResponse(Schema):
    status: int
    message: str
    payload: dict