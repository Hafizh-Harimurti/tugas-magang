from ninja import NinjaAPI
from visualizeapi.controllers.controller_exception import BadRequest, InternalServerError, ResourceNotFound
from visualizeapi.models.visualize_schema import Data, CustomSettings, ResponseMessage
from visualizeapi.services.validate_service import ValidateService
from visualizeapi.services.visualize_service import VisualizeService

visualize_service = VisualizeService()
validate_service = ValidateService()

visualize_api = NinjaAPI(
    title = 'Visualize API',
    description = 'API for creating option to use in Apache Echarts '
)

@visualize_api.exception_handler(BadRequest)
def bad_request_exception(request, ex):
    return visualize_api.create_response(
        request,
        {'status': 400, 'message': str(ex)},
        status = 400
    )

@visualize_api.exception_handler(ResourceNotFound)
def resource_not_found_exception(request, ex):
    return visualize_api.create_response(
        request,
        {'status': 404, 'message': str(ex)},
        status = 404
    )

@visualize_api.exception_handler(InternalServerError)
def internal_server_error_exception(request, ex):
    return visualize_api.create_response(
        request,
        {'status': 500, 'message': str(ex)},
        status = 500
    )

@visualize_api.post('/visualize/{plot_type}', response = {200: ResponseMessage})
def visualize_post(request, plot_type, data: Data = Data(), custom_settings: CustomSettings = CustomSettings()):
    try:
        validation_result = validate_service.validate_data(data, plot_type)
        if validation_result > 0:
            if validation_result == 1:
                raise ResourceNotFound(validate_service.invalid_data_code[validation_result])
            else:
                raise BadRequest(validate_service.invalid_data_code[validation_result])
        payload = visualize_service.visualize_data(data, plot_type, custom_settings)
        return 200, {'status': 200, 'message': 'OK', 'payload': payload}
    except BadRequest as ex:
        raise BadRequest(str(ex))
    except ResourceNotFound as ex:
        raise ResourceNotFound(str(ex))
    except Exception as ex:
        raise InternalServerError('An internal server error has occured. Error: ' + str(ex))