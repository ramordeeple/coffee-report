class BaseReportError(Exception):
    pass

class ReportNotFoundError(BaseReportError):
    pass

class DataEmptyError(BaseReportError):
    pass

class InvalidDataFormatError(BaseReportError):
    pass