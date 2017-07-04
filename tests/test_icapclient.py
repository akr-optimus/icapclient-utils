#!/usr/bin/env python

import pytest
import time
import os
from icapclientutils.core import ICAPClientHandler


@pytest.fixture()
def test_data(key):
    data = {

    }
    return data.get(key, {})


class TestICAPClientUtils:

    def setup_method(selfs):
        pass

    def teardown_method(self):
        pass

    def test_icapclientutils(self):
        pass
