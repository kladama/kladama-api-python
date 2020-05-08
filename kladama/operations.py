import abc
from abc import ABC


# Operations

class Operation(ABC):

    @property
    @abc.abstractmethod
    def url_path(self) -> str:
        pass


class PostOperation(Operation, ABC):

    @property
    @abc.abstractmethod
    def post_obj(self):
        pass


class CreateOperation(Operation, ABC):

    def __init__(self):
        Operation.__init__(self)


class DeleteOperation(Operation, ABC):
    pass


class CreateSubscriptionOperation(CreateOperation, PostOperation):

    def __init__(
        self,
        user,
        subscription_type,
        variable_name,
        variable_source_name,
        spatial_operation_name,
        aoi_name,
    ):
        CreateOperation.__init__(self)
        self._user = user
        self._subscription_type = subscription_type
        self._variable_name = variable_name
        self._variable_source_name = variable_source_name
        self._spatial_operation_name = spatial_operation_name
        self._aoi_name = aoi_name

    @property
    def url_path(self):
        return "/subsc/user/{0}".format(self._user)

    @property
    def post_obj(self):
        return {
            "type": self._subscription_type,
            "variable": {
                "name": self._variable_name,
                "source": {
                    "name": self._variable_source_name
                }
            },
            "spatialOper": {
                "name": self._spatial_operation_name
            },
            "aoi": {
                "name": self._aoi_name
            }
        }


class DeleteSubscriptionOperation(DeleteOperation):

    def __init__(self, user, subscription_id):
        DeleteOperation.__init__(self)
        self._user = user
        self._subscription_id = subscription_id

    @property
    def url_path(self) -> str:
        return "/subsc/user/{0}/{1}".format(self._user, self._subscription_id)


# Builders

class OperationBuilder(ABC):

    @abc.abstractmethod
    def build(self) -> Operation:
        pass


class CreateSubscriptionBuilder(OperationBuilder):

    def __init__(self, user):
        OperationBuilder.__init__(self)
        self._user = user
        self._subscription_type = ""
        self._variable_name = ""
        self._variable_source_name = ""
        self._spatial_operation_name = ""
        self._aoi_name = ""

    def build(self) -> CreateSubscriptionOperation:
        return CreateSubscriptionOperation(
            self._user,
            self._subscription_type,
            self._variable_name,
            self._variable_source_name,
            self._spatial_operation_name,
            self._aoi_name,
        )

    def set_subscription_type(self, subscription_type: str):
        self._subscription_type = subscription_type
        return self

    def set_variable_name(self, variable_name: str):
        self._variable_name = variable_name
        return self

    def set_variable_source_name(self, variable_source_name: str):
        self._variable_source_name = variable_source_name
        return self

    def set_spatial_operation_name(self, spatial_operation_name: str):
        self._spatial_operation_name = spatial_operation_name
        return self

    def set_aoi_name(self, aoi_name: str):
        self._aoi_name = aoi_name
        return self


class DeleteSubscriptionBuilder(OperationBuilder):

    def __init__(self, user):
        OperationBuilder.__init__(self)
        self._user = user
        self._subscription_id = ""

    def build(self) -> DeleteSubscriptionOperation:
        return DeleteSubscriptionOperation(self._user, self._subscription_id)

    def set_subscription_id(self, subscription_id: str):
        self._subscription_id = subscription_id
        return self
