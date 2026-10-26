from unittest import mock
import os
def read_mode(): return os.environ.get("APP_MODE", "dev")
with mock.patch.dict(os.environ, {"APP_MODE": "prod"}):
    print("inside the patch:", read_mode())
print("after the patch is undone:", read_mode())
with mock.patch("os.path.exists", return_value=True) as fake_exists:
    print("patched exists says:", os.path.exists("/definitely/not/here"), "| call count:", fake_exists.call_count)
