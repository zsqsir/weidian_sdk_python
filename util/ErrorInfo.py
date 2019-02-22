__author__ = 'Seven'

class OpenError(StandardError):
    def __init__(self, error_code, error,error_info):
        self.error_code = error_code
        self.error = error
        self.error_info=error_info;
        StandardError.__init__(self, error)

    def __str__(self):
        return 'Error: %s: %s, request: %s' % (self.error_code, self.error, self.error_info)