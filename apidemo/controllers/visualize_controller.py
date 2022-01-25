from ninja import NinjaAPI
from ninja.responses import codes_4xx
from apidemo.controllers.controller_exception import BadRequest, ResourceNotFound
from apidemo.models.visualize_schema import Data, CustomSettings, ResponseMessage
from apidemo.services.validate_service import ValidateService
from apidemo.services.visualize_service import VisualizeService

visualize_service = VisualizeService()
validate_service = ValidateService()

visualize_api = NinjaAPI(
    title = 'Visualize API',
    description = 'API for creating option to use in Apache Echarts '
)

@visualize_api.post('/visualize/{plot_type}', response = {200: ResponseMessage, codes_4xx: ResponseMessage, 500:  ResponseMessage})
def visualizePost(request, plot_type, data: Data = Data(), custom_settings: CustomSettings = CustomSettings()):
    try:
        validate_service.validate_data(data, plot_type)
        payload = visualize_service.visualize_data(data, plot_type, custom_settings)
        return 200, {'status': 200, 'message': 'OK', 'payload': payload}
    except BadRequest as br:
        return 400, {'status': 400, 'message': str(br)}
    except ResourceNotFound as rnf:
        return 404, {'status': 404, 'message': str(rnf)}
    except Exception as e:
        return 500, {'status': 500, 'message': 'An internal server error has occured. Error: ' + str(e)}