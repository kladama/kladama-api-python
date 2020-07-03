import abc
from abc import ABC

from .queries import EndpointQuery
from .queries import SingleResultQuery


class InfoBase(EndpointQuery, ABC):

    @property
    @abc.abstractmethod
    def method(self) -> str:
        pass

    @property
    @abc.abstractmethod
    def obj(self):
        pass


class AoiValidation(InfoBase, SingleResultQuery):

    def __init__(self, aoi_obj):
        InfoBase.__init__(self)
        self._aoi_obj = aoi_obj

    @property
    def sub_url(self):
        return '/do/aoivalidation'

    @property
    def method(self) -> str:
        return 'post'

    @property
    def aoi_obj(self):
        return self._aoi_obj

    @property
    def obj(self):
        return self.aoi_obj


class SystemInfo:

    @staticmethod
    def check_aoi(aoi_obj):
        return AoiValidation(aoi_obj)
