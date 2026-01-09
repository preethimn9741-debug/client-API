import pytest
from unittest.mock import patch
import client

class Args:
    def __init__(self, command, to=None, amount=None):
        self.command = command
        self.to = to
        self.amount = amount

def test_valid_convert_args():
    args = Args("convert", "INR", 10)
    assert client.validate_args(args) is True

def test_missing_all_arguments():
    args = Args(None, None, None)
    with pytest.raises(ValueError):
        client.validate_args(args)

def test_invalid_command():
    args = Args("wrong", "INR", 10)
    with pytest.raises(ValueError):
        client.validate_args(args)

def test_missing_target_currency():
    args = Args("convert", None, 10)
    with pytest.raises(ValueError):
        client.validate_args(args)

def test_empty_target_currency():
    args = Args("convert", "", 10)
    with pytest.raises(ValueError):
        client.validate_args(args)

def test_missing_amount():
    args = Args("convert", "INR", None)
    with pytest.raises(ValueError):
        client.validate_args(args)


def test_negative_amount():
    args = Args("convert", "INR", -5)
    with pytest.raises(ValueError):
        client.validate_args(args)


def test_zero_amount():
    args = Args("convert", "INR", 0)
    with pytest.raises(ValueError):
        client.validate_args(args)


def test_amount_as_string():
    args = Args("convert", "INR", "ten")
    with pytest.raises(Exception):
        client.validate_args(args)


def test_amount_as_float_zero():
    args = Args("convert", "INR", 0.0)
    with pytest.raises(ValueError):
        client.validate_args(args)

def test_target_currency_as_number():
    args = Args("convert", 123, 10)
    with pytest.raises(ValueError):
        client.validate_args(args)

def test_command_case_sensitivity():
    args = Args("CONVERT", "INR", 10)
    with pytest.raises(ValueError):
        client.validate_args(args)

def test_extra_whitespace_command():
    args = Args(" convert ", "INR", 10)
    with pytest.raises(ValueError):
        client.validate_args(args)

@patch("client.requests.get")
def test_fetch_rates_network_failure(mock_get):
    mock_get.side_effect = Exception("Network error")

    with pytest.raises(Exception):
        client.fetch_rates("USD")

@patch("client.requests.get")
def test_fetch_rates_http_error(mock_get):
    mock_get.return_value.raise_for_status.side_effect = Exception("500 error")

    with pytest.raises(Exception):
        client.fetch_rates("USD")

@patch("client.requests.get")
def test_fetch_rates_invalid_json(mock_get):
    mock_get.return_value.raise_for_status.return_value = None
    mock_get.return_value.json.side_effect = ValueError("Invalid JSON")

    with pytest.raises(Exception):
        client.fetch_rates("USD")

@patch("client.requests.get")
def test_fetch_rates_empty_response(mock_get):
    mock_get.return_value.raise_for_status.return_value = None
    mock_get.return_value.json.return_value = {}

    data = client.fetch_rates("USD")
    assert data == {}

@patch("client.requests.get")
def test_fetch_rates_missing_rates_key(mock_get):
    mock_get.return_value.raise_for_status.return_value = None
    mock_get.return_value.json.return_value = {"base": "USD"}

    data = client.fetch_rates("USD")
    assert "rates" not in data

@patch("client.requests.get")
def test_fetch_rates_none_base_currency(mock_get):
    mock_get.return_value.raise_for_status.return_value = None
    mock_get.return_value.json.return_value = {}

    data = client.fetch_rates(None)
    assert isinstance(data, dict)

