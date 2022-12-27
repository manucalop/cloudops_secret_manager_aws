import unittest

from cloudops.secret_manager.aws.secret import Secret, SecretConfig


class TestSecret(unittest.TestCase):
    # def setUp(self):
    #     config = SecretConfig(
    #         secret_id="test-secret-2",
    #         region="eu-west-1",
    #     )
    #     self.secret = Secret(config)
    #     if not self.secret.exists():
    #         self.secret.create()

    # def test_pull_push_secret(self):
    #     payload = {"foo": "bar"}
    #     self.secret.push(payload)
    #     self.assertEqual(self.secret.pull(), payload)

    def test_dummy(self):
        self.assertEqual(True, True, "I leave Python!")
