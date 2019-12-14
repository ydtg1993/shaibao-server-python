from celery import Celery


class MyCelery(Celery):

    def now(self):
        """Return the current time and date as a datetime."""
        from datetime import datetime
        return datetime.now(self.timezone)
