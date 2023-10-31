# Copyright 2023 ReSim, Inc.
#
# Use of this source code is governed by an MIT-style
# license that can be found in the LICENSE file or at
# https://opensource.org/licenses/MIT.

"""Minimal health endpoint test for the genrated client"""

import os
import unittest
from http import HTTPStatus

from resim_python_client.client import Client
import resim_python_client.api.health.health as health

class HealthTest(unittest.TestCase):
    """Test that we can hit the health endpoint"""
    def setUp(self) -> None:
        """Set up the api URL"""
        self._url = "https://api.resim.ai/v1"

    def test_health(self) -> None:
        """Hit the health endpoint and check for status 200"""
        client = Client(base_url=self._url)
        health_response = health.sync_detailed(client=client)
        self.assertEqual(health_response.status_code, HTTPStatus.OK)

if __name__ == '__main__':
    unittest.main()
