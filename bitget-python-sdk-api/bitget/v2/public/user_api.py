#!/usr/bin/python
from bitget.client import Client
from bitget.consts import GET, POST


class UserApi(Client):
    def __init__(self, api_key, api_secret_key, passphrase, use_server_time=False, first=False):
        super().__init__(api_key, api_secret_key, passphrase, use_server_time, first)

    def virtual_subaccount_list(self, params):
        """查詢虛擬子帳號清單"""
        return self._request_with_params(GET, '/api/v2/user/virtual-subaccount-list', params)

    def create_virtual_subaccount(self, params):
        """批量創建虛擬子帳號"""
        return self._request_with_params(POST, '/api/v2/user/create-virtual-subaccount', params)

    def modify_virtual_subaccount(self, params):
        """修改虛擬子帳號"""
        return self._request_with_params(POST, '/api/v2/user/modify-virtual-subaccount', params)

    def batch_create_subaccount_and_apikey(self, params):
        """批量創建虛擬子帳號與對應的 API Key"""
        return self._request_with_params(POST, '/api/v2/user/batch-create-subaccount-and-apikey', params)

    def create_virtual_subaccount_apikey(self, params):
        """創建虛擬子帳號的 API Key"""
        return self._request_with_params(POST, '/api/v2/user/create-virtual-subaccount-apikey', params)

    def modify_virtual_subaccount_apikey(self, params):
        """修改虛擬子帳號的 API Key"""
        return self._request_with_params(POST, '/api/v2/user/modify-virtual-subaccount-apikey', params)

    def virtual_subaccount_apikey_list(self, params):
        """查詢虛擬子帳號的 API Key 清單"""
        return self._request_with_params(GET, '/api/v2/user/virtual-subaccount-apikey-list', params)
