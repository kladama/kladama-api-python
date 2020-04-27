import kladama.entities as kle


class QueryBase:

    @property
    def entity_meta(self) -> kle.EntityMetadata:
        pass

    @property
    def url_path(self) -> str:
        pass


class Query:

    @property
    def aoi(self):
        return AreaOfInterestQuery()

    @property
    def phenom(self):
        return PhenomenaQuery()

    @property
    def org(self):
        return OrganizationQuery()

    @property
    def subsc(self):
        return SubscriptionQuery()

    @property
    def src(self):
        return SourceQuery()

    @property
    def user(self):
        return UserQuery()

    @property
    def var(self):
        return VariableQuery()


# query aggregates


class SimpleResultsQuery(QueryBase):

    def __init__(self):
        QueryBase.__init__(self)


class MultipleResultsQuery(QueryBase):

    def __init__(self):
        QueryBase.__init__(self)


class EntityQuery(MultipleResultsQuery):

    def __init__(self, entity_meta):
        MultipleResultsQuery.__init__(self)
        self._entity_meta = entity_meta
        self._url_path = '/' + entity_meta.url_base_path

    @property
    def entity_meta(self):
        return self._entity_meta

    @property
    def url_path(self):
        return self._url_path


class SubClassedFilterQuery(MultipleResultsQuery):

    def __init__(self, sub_query, sub_class_path):
        MultipleResultsQuery.__init__(self)
        self._sub_query = sub_query
        self._sub_class_path = sub_class_path

    @property
    def entity_meta(self):
        return self._sub_query.entity_meta

    @property
    def url_path(self):
        return '{0}/{1}'.format(self._sub_query.url_path, self._sub_class_path)


class ForecastQuery(SubClassedFilterQuery):

    def __init__(self, sub_query):
        SubClassedFilterQuery.__init__(self, sub_query, 'forecast')


class ObservedQuery(SubClassedFilterQuery):

    def __init__(self, sub_query):
        SubClassedFilterQuery.__init__(self, sub_query, 'observed')


class PredictableEntityQuery(MultipleResultsQuery):

    def __init__(self):
        MultipleResultsQuery.__init__(self)

    @property
    def forecast(self):
        return ForecastQuery(self)


class ObservableEntityQuery(MultipleResultsQuery):

    def __init__(self):
        MultipleResultsQuery.__init__(self)

    @property
    def observed(self):
        return ObservedQuery(self)


class ByNameQueryable(MultipleResultsQuery):

    def __init__(self):
        MultipleResultsQuery.__init__(self)

    def by_name(self, name_value):
        return ByNameQuery(self, name_value)


class ByPhenomenaQueryable(MultipleResultsQuery):

    def __init__(self):
        MultipleResultsQuery.__init__(self)

    def by_phenomena(self, phenomena):
        return ByPhenomenaQuery(self, phenomena)


class BySourceQueryable(MultipleResultsQuery):

    def __init__(self):
        MultipleResultsQuery.__init__(self)

    def by_sources(self, *sources):
        return BySourceQuery(self, sources)


class ByUserQueryable(MultipleResultsQuery):

    def __init__(self):
        MultipleResultsQuery.__init__(self)

    def by_user(self, user):
        return ByUserQuery(self, user)


# filters


class FilterQuery(QueryBase):

    def __init__(self, query_base, filter_value):
        QueryBase.__init__(self)
        self._entity_query = query_base
        self._filter_value = filter_value

    @property
    def entity_meta(self):
        return self._entity_query.entity_meta

    @property
    def entity_query(self):
        return self._entity_query

    @property
    def filter_value(self):
        return self._filter_value


class ByNameQuery(FilterQuery, SimpleResultsQuery):

    def __init__(self, query_base, name_value):
        assert isinstance(query_base, ByNameQueryable)
        FilterQuery.__init__(self, query_base, name_value)
        SimpleResultsQuery.__init__(self)

    @property
    def url_path(self):
        return '{0}/{1}'.format(self.entity_query.url_path, self.filter_value)


class ByPhenomenaQuery(FilterQuery, ObservableEntityQuery, PredictableEntityQuery):

    def __init__(self, query_base, phenomena):
        assert isinstance(query_base, ByNameQueryable)
        FilterQuery.__init__(self, query_base, phenomena)
        ObservableEntityQuery.__init__(self)
        PredictableEntityQuery.__init__(self)

    @property
    def url_path(self):
        return '{0}/phenom/{1}'.format(self.entity_query.url_path, self.filter_value)


class BySourceQuery(FilterQuery, ObservableEntityQuery, PredictableEntityQuery):

    def __init__(self, query_base, *sources):
        assert isinstance(query_base, ByNameQueryable)
        FilterQuery.__init__(self, query_base, sources)
        ObservableEntityQuery.__init__(self)
        PredictableEntityQuery.__init__(self)

    @property
    def url_path(self):
        return '{0}/src/{1}'.format(self.entity_query.url_path, ','.join(*self.filter_value))


class ByUserQuery(FilterQuery, ByNameQueryable):

    def __init__(self, query_base, user):
        assert isinstance(query_base, ByNameQueryable)
        FilterQuery.__init__(self, query_base, user)
        ByNameQueryable.__init__(self)

    def filter_by(self, name):
        return ByNameQuery(self, name)

    @property
    def url_path(self):
        return '{0}/user/{1}'.format(self.entity_query.url_path, self.filter_value)


# entity queries

class AreaOfInterestQuery(EntityQuery, ByNameQueryable, ByUserQueryable):

    def __init__(self):
        EntityQuery.__init__(self, kle.get_aoi_meta())
        ByNameQueryable.__init__(self)
        ByUserQueryable.__init__(self)


class PhenomenaQuery(
    EntityQuery,
    ByNameQueryable,
    BySourceQueryable,
    ObservableEntityQuery,
    PredictableEntityQuery
):
    def __init__(self):
        EntityQuery.__init__(self, kle.get_phenom_meta())
        ByNameQueryable.__init__(self)
        BySourceQueryable.__init__(self)
        ObservableEntityQuery.__init__(self)
        PredictableEntityQuery.__init__(self)


class OrganizationQuery(EntityQuery, ByNameQueryable):

    def __init__(self):
        EntityQuery.__init__(self, kle.get_org_meta())
        ByNameQueryable.__init__(self)


class SourceQuery(
    EntityQuery,
    ByNameQueryable,
    ByPhenomenaQueryable,
    ObservableEntityQuery,
    PredictableEntityQuery
):
    def __init__(self):
        EntityQuery.__init__(self, kle.get_src_meta())
        ByNameQueryable.__init__(self)
        ByPhenomenaQueryable.__init__(self)
        ObservableEntityQuery.__init__(self)
        PredictableEntityQuery.__init__(self)


class SubscriptionQuery(EntityQuery, ByNameQueryable, ByUserQueryable):

    def __init__(self):
        EntityQuery.__init__(self, kle.get_subsc_meta())
        ByNameQueryable.__init__(self)
        ByUserQueryable.__init__(self)


class UserQuery(EntityQuery, ByNameQueryable):

    def __init__(self):
        EntityQuery.__init__(self, kle.get_user_meta())
        ByNameQueryable.__init__(self)


class VariableQuery(
    EntityQuery,
    ByNameQueryable,
    ByPhenomenaQueryable,
    BySourceQueryable,
    ObservableEntityQuery,
    PredictableEntityQuery
):
    def __init__(self):
        EntityQuery.__init__(self, kle.get_var_meta())
        ByNameQueryable.__init__(self)
        ByPhenomenaQueryable.__init__(self)
        BySourceQueryable.__init__(self)
        ObservableEntityQuery.__init__(self)
        PredictableEntityQuery.__init__(self)
