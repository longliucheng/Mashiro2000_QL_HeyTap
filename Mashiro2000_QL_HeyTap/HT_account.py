# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2021/9/29
# @Author  : MashiroF
# @File    : HT_account.py
# @Software: PyCharm

## 账号管理样本
# {
#     'user':'',        # 备注,必要
#     'CK':'',          # Cookie,必要(建议全部粘贴)
#     'UA':''           # User-Agent,必要
# },

## 账号管理
accounts = [
    {
        'user':'曹少峰',
        'CK':'source_type=501; sa_distinct_id=cUlGMGxnTG96WlhzLzdSdkk2MGgzZz09; s_channel=oppo_appstore; s_version=300501; app_utm={"utm_source":"direct","utm_medium":"direct","utm_campaign":"direct","utm_term":"direct"}; app_param={"model":"RMX3031","brand":"realme","rom":"ColorOS","guid":"48653268b187d32abd991f83664a3480beccc39af6152e3d8d1d15069f6e31b7","ouid":"DF716ABE55E945D9B14A4D3A0D90C7ED5dc23b48f61c25ed64c0d8228eb13d10","duid":"8D3494E92F5C4DDAAA287CFD9DD7BC12EC7D424979CC9C51DB2B8E416B3EF063","udid":"48653268b187d32abd991f83664a3480beccc39af6152e3d8d1d15069f6e31b7","apid":"","sa_device_id":"48653268b187d32abd991f83664a3480beccc39af6152e3d8d1d15069f6e31b7","romVersion":"V12.0","apkPkg":"com.oppo.store"}; apkPkg=com.oppo.store; Personalized=1; path=/; section_id=null; scene_id=null; exp_id=null; strategy_id=null; retrieve_id=null; log_id=null; adid=null; search_id=; transparent=; referer=; memberinfo=%7B%22id%22%3A%2220841019%22%2C%22name%22%3A%22cao2111500300%22%2C%22oid%22%3A%22cUlGMGxnTG96WlhzLzdSdkk2MGgzZz09%22%7D; _dx_uzZo5y=14a7007ae4da5ec55903e8874ac029fb65ed40548cd534e10be32c89e5f1134bcd30c8c7; _dx_app_900cf4f8d0fb9f215d567b1c23d1fc38=626934964gXySiq0uysXlPM9aDHs9lv68hKY3oS1; _dx_captcha_vid=1806AF57D48900CF4F8D070BEFA4552F54CD6ADCA847A2D23110C%40bj; sensorsdata2015jssdkcross=%7B%22distinct_id%22%3A%22cUlGMGxnTG96WlhzLzdSdkk2MGgzZz09%22%2C%22%24device_id%22%3A%221806af555921e0-01f94caa608adc-497f0124-288000-1806af555936e%22%2C%22props%22%3A%7B%22%24latest_referrer%22%3A%22%22%2C%22%24latest_traffic_source_type%22%3A%22%E7%9B%B4%E6%8E%A5%E6%B5%81%E9%87%8F%22%2C%22%24latest_search_keyword%22%3A%22%E6%9C%AA%E5%8F%96%E5%88%B0%E5%80%BC_%E7%9B%B4%E6%8E%A5%E6%89%93%E5%BC%80%22%2C%22%24latest_utm_source%22%3A%22opposhop%22%2C%22%24latest_utm_medium%22%3A%22task%22%7D%2C%22first_id%22%3A%22cUlGMGxnTG96WlhzLzdSdkk2MGgzZz09%22%7D; TOKENSID=TOKEN_eyJhbGciOiJFQ0RTQSIsInYiOiIxIn0.eyJleHAiOjE2NTQwMDc0MzM1MDcsImlkIjoiMjA4NDEwMTkiLCJpZGMiOiJzaG91bWluZyIsInRpZCI6InpnUUlNQmRyWmpTNzVnbmVybUozMFJXNTYzNTdVbVpGYW5uMk5HV2JPQVgxN3FyVU9hRVRmeHhYOEZ4YW96NVRQUzR5VkZNYVhLSCsrRFdnQldzdWpldnNRc3BleVV6b1RBVW1jVVU1bVFrPSJ9.MEUCIC_K92DwPNZQ_RZGgmuvjQEc81m4wr05vUtY35o_HdxYAiEAoRLsq6O5dYXtyq2PCR_8hEfHzwnzpRsuI5VN8EnuB5Y; ENCODE_TOKENSID=TOKEN_eyJhbGciOiJFQ0RTQSIsInYiOiIxIn0.eyJleHAiOjE2NTQwMDc0MzM1MDcsImlkIjoiMjA4NDEwMTkiLCJpZGMiOiJzaG91bWluZyIsInRpZCI6InpnUUlNQmRyWmpTNzVnbmVybUozMFJXNTYzNTdVbVpGYW5uMk5HV2JPQVgxN3FyVU9hRVRmeHhYOEZ4YW96NVRQUzR5VkZNYVhLSCsrRFdnQldzdWpldnNRc3BleVV6b1RBVW1jVVU1bVFrPSJ9.MEUCIC_K92DwPNZQ_RZGgmuvjQEc81m4wr05vUtY35o_HdxYAiEAoRLsq6O5dYXtyq2PCR_8hEfHzwnzpRsuI5VN8EnuB5Y; experiment_id=4526_660_4477_-4018_76_-106_3552_-3558_329_2422_-1825_23_14_2_2_4_3_3_1_1066_1281_-2338_2_2_7_2_2_34_113_-109_103_2_1038_-1001_8_42_2_76_2_37_329_1523_-978_-426_4_-2_434_2_3_38_-3_-1_-4_-2_-3_-1_943_-253_-696_-2_28_-2_91_282_26_57_1_919_-828_683_1_537_-2_-4_2_-4_-2_77_-2_-2_12_12; acw_tc=2760824e16514234924642016e8ef5624ed70dcb653f7b0a3f929048f63048; um=direct; uc=direct; ut=direct; utm_source=direct; utm_medium=direct; utm_campaign=direct; utm_term=direct; app_innerutm={"us":"wode","um":"direct","uc":"direct","ut":"direct"}; us=wode',
        'UA':'Mozilla/5.0 (Linux; Android 12; RMX3031 Build/SP1A.210812.016; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/97.0.4692.98 Mobile Safari/537.36 oppostore/300501 ColorOS/V12.0 brand/realme model/RMX3031'
    },
    {
        'user':'',
        'CK':'',
        'UA':''
    },
]