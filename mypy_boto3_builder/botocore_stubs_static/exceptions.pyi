# pylint: disable=unused-argument,multiple-statements,super-init-not-called
import sys
from typing import Iterable, Any, Dict, TypeVar

from botocore.vendored import requests
from botocore.vendored.requests.packages import urllib3

if sys.version_info >= (3, 8):
    from typing import TypedDict
else:
    from typing_extensions import TypedDict

ErrorResponseTypeDef = TypedDict(
    "ErrorResponseTypeDef",
    {"Error": Dict[str, Any], "Code": str, "Message": str},
    total=False,
)

RequestType = TypeVar("RequestType")
ResponseType = TypeVar("RequestType")
LastResponseType = TypeVar("LastResponseType")

class BotoCoreError(Exception):
    fmt: str
    def __init__(self, **kwargs: Any) -> None:
        self.kwargs: Dict[str, Any]
    def __reduce__(self): ...

class DataNotFoundError(BotoCoreError): ...
class UnknownServiceError(DataNotFoundError): ...
class ApiVersionNotFoundError(BotoCoreError): ...

class HTTPClientError(BotoCoreError):
    def __init__(
        self, request: RequestType = ..., response: ResponseType = ..., **kwargs: Any
    ):
        self.request: RequestType
        self.response: ResponseType

class ConnectionError(BotoCoreError): ...
class EndpointConnectionError(ConnectionError): ...
class SSLError(ConnectionError, requests.exceptions.SSLError): ...
class ConnectionClosedError(HTTPClientError): ...
class ReadTimeoutError(
    HTTPClientError,
    requests.exceptions.ReadTimeout,
    urllib3.exceptions.ReadTimeoutError,
): ...
class ConnectTimeoutError(ConnectionError, requests.exceptions.ConnectTimeout): ...
class ProxyConnectionError(ConnectionError, requests.exceptions.ProxyError): ...
class NoCredentialsError(BotoCoreError): ...
class PartialCredentialsError(BotoCoreError): ...
class CredentialRetrievalError(BotoCoreError): ...
class UnknownSignatureVersionError(BotoCoreError): ...
class ServiceNotInRegionError(BotoCoreError): ...
class BaseEndpointResolverError(BotoCoreError): ...
class NoRegionError(BaseEndpointResolverError): ...
class UnknownEndpointError(BaseEndpointResolverError, ValueError): ...
class ProfileNotFound(BotoCoreError): ...
class ConfigParseError(BotoCoreError): ...
class ConfigNotFound(BotoCoreError): ...
class MissingParametersError(BotoCoreError): ...
class ValidationError(BotoCoreError): ...
class ParamValidationError(BotoCoreError): ...
class UnknownKeyError(ValidationError): ...
class RangeError(ValidationError): ...
class UnknownParameterError(ValidationError): ...
class AliasConflictParameterError(ValidationError): ...
class UnknownServiceStyle(BotoCoreError): ...
class PaginationError(BotoCoreError): ...
class OperationNotPageableError(BotoCoreError): ...
class ChecksumError(BotoCoreError): ...
class UnseekableStreamError(BotoCoreError): ...

class WaiterError(BotoCoreError):
    def __init__(self, name: str, reason: str, last_response: LastResponseType):
        self.last_response: LastResponseType

class IncompleteReadError(BotoCoreError): ...
class InvalidExpressionError(BotoCoreError): ...
class UnknownCredentialError(BotoCoreError): ...
class WaiterConfigError(BotoCoreError): ...
class UnknownClientMethodError(BotoCoreError): ...
class UnsupportedSignatureVersionError(BotoCoreError): ...

class ClientError(Exception):
    MSG_TEMPLATE: str
    def __init__(
        self, error_response: ErrorResponseTypeDef, operation_name: str
    ) -> None:
        self.response: ErrorResponseTypeDef
        self.operation_name: str

class EventStreamError(ClientError): ...
class UnsupportedTLSVersionWarning(Warning): ...
class ImminentRemovalWarning(Warning): ...
class InvalidDNSNameError(BotoCoreError): ...
class InvalidS3AddressingStyleError(BotoCoreError): ...
class UnsupportedS3ArnError(BotoCoreError): ...
class UnsupportedS3AccesspointConfigurationError(BotoCoreError): ...
class InvalidRetryConfigurationError(BotoCoreError): ...
class InvalidMaxRetryAttemptsError(InvalidRetryConfigurationError): ...
class InvalidRetryModeError(InvalidRetryConfigurationError): ...
class InvalidS3UsEast1RegionalEndpointConfigError(BotoCoreError): ...
class InvalidSTSRegionalEndpointsConfigError(BotoCoreError): ...
class StubResponseError(BotoCoreError): ...
class StubAssertionError(StubResponseError, AssertionError): ...
class UnStubbedResponseError(StubResponseError): ...
class InvalidConfigError(BotoCoreError): ...
class InfiniteLoopConfigError(InvalidConfigError): ...
class RefreshWithMFAUnsupportedError(BotoCoreError): ...
class MD5UnavailableError(BotoCoreError): ...
class MetadataRetrievalError(BotoCoreError): ...
class UndefinedModelAttributeError(Exception): ...

class MissingServiceIdError(UndefinedModelAttributeError):
    def __init__(self, **kwargs: Any):
        self.kwargs: Dict[str, Any]

class CapacityNotAvailableError(BotoCoreError): ...