from rest_framework import pagination, response


class DefaultUnlimitedPagination(pagination.LimitOffsetPagination):
    default_limit = 9_223_372_036_854_775_807
