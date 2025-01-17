# Copyright 2015, 2017 Jairo Llopis <jairo.llopis@tecnativa.com>
# Copyright 2016 Tecnativa, S.L. - Vicent Cubells
# Copyright 2024 Tecnativa - Carolina Fernandez
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
import datetime
from random import random

from odoo.tests.common import TransactionCase
from odoo.tools import (
    DEFAULT_SERVER_DATE_FORMAT,
    DEFAULT_SERVER_DATETIME_FORMAT,
    DEFAULT_SERVER_TIME_FORMAT,
)

from ..models.res_lang import MODE_DATE, MODE_DATETIME, MODE_TIME


class FormatterCase(TransactionCase):
    @classmethod
    def setUpClass(cls):
        super(FormatterCase, cls).setUpClass()
        cls.rl = cls.env["res.lang"]
        cls.bm = cls.rl.best_match()
        cls.dt = datetime.datetime.now()
        cls.d_fmt = cls.bm.date_format or DEFAULT_SERVER_DATE_FORMAT
        cls.t_fmt = cls.bm.time_format or DEFAULT_SERVER_TIME_FORMAT
        cls.kwargs = dict()

    def tearDown(self):
        # This should be returned
        self.expected = self.dt.strftime(self.format)
        # Pass a datetime object
        self.assertEqual(
            self.expected, self.rl.datetime_formatter(self.dt, **self.kwargs)
        )
        # When the date comes as a string
        if isinstance(self.dt, datetime.datetime):
            self.dt_str = self.dt.strftime(DEFAULT_SERVER_DATETIME_FORMAT)
        elif isinstance(self.dt, datetime.date):
            self.dt_str = self.dt.strftime(DEFAULT_SERVER_DATE_FORMAT)
        elif isinstance(self.dt, datetime.time):
            self.dt_str = self.dt.strftime(DEFAULT_SERVER_TIME_FORMAT)
        # Pass a string
        self.assertEqual(
            self.expected, self.rl.datetime_formatter(self.dt_str, **self.kwargs)
        )
        # Pass a unicode
        self.assertEqual(
            self.expected, self.rl.datetime_formatter(str(self.dt_str), **self.kwargs)
        )
        super().tearDown()

    def test_datetime(self):
        """Format a datetime."""
        self.format = "{} {}".format(self.d_fmt, self.t_fmt)
        self.kwargs = {"template": MODE_DATETIME}

    def test_date(self):
        """Format a date."""
        self.format = self.d_fmt
        self.kwargs = {"template": MODE_DATE}
        self.dt = self.dt.date()

    def test_time(self):
        """Format times, including float ones."""
        self.format = self.t_fmt
        self.kwargs = {"template": MODE_TIME}
        self.dt = self.dt.time()
        # Test float times
        for n in range(50):
            n = n + random()
            # Patch values with >= 24 hours
            fmt = self.format.replace("%H", "%02d" % n)
            time = (datetime.datetime.min + datetime.timedelta(hours=n)).time()
            self.assertEqual(
                time.strftime(fmt), self.rl.datetime_formatter(n, **self.kwargs)
            )

    def test_custom_separator(self):
        """Format a datetime with a custom separator."""
        sep = "T"
        self.format = "{}{}{}".format(self.d_fmt, sep, self.t_fmt)
        self.kwargs = {"template": MODE_DATETIME, "separator": sep}
