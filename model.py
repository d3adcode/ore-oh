from ariadne import QueryType, MutationType, ScalarType
import datetime
from dateutil import parser

datetime_scalar = ScalarType("Datetime")

query = QueryType()
mutation = MutationType()


class Statistic:
    def __init__(self, id, source, stat_id, data, create_date):
        self.id = id
        self.source = source
        self.stat_id = stat_id
        self.data = data
        self.create_date = create_date

    def __eq__(self, other):
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        else:
            return False

    def __ne__(self, other):
        return not self.__eq__(other)


stats = []


# this does not align with ariadne's documentation at all...
# @datetime_scalar.serializer
# def serialize_datetime(value):
#   return value


@datetime_scalar.value_parser
def parse_datetime_value(value):
    try:
        # default to current time
        return parser.parse(value) if value else datetime.datetime.utcnow().isoformat()
    except (ValueError, TypeError):
        raise ValueError(f'"{value}" is not a valid ISO 8601 string')


@query.field("stats")
def resolve_stats(_, info):
    return stats


@mutation.field("createStat")
def resolve_add_stat(_, info, id, source, stat_id, data="", create_date=""):
    stat = Statistic(id, source, stat_id, data, create_date)
    stats.append(stat)
    return stat
