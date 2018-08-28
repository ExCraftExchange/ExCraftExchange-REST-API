import attr

class Error(Exception):
    def error(self):
        pass

    def __str__(self):
        try:
            return str(self.error())
        except:
            return repr(self.error().encode('utf-8', 'ignore'))

    def __unicode__(self):
        try:
            return unicode(self.error())
        except:
            return repr(self.error())


class ExceptionError(Error):
    e = attr.ib()

    def error(self):
        try:
            return unicode(self.e).encode('utf-8', 'ignore')
        except:
            return str(self.e)


class HTTPError(ExceptionError):
    pass