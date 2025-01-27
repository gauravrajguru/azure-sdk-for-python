# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from enum import Enum
from azure.core import CaseInsensitiveEnumMeta


class SettingKind(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """the kind of the settings string.
    """

    DATA_EXPORT_SETTINGS = "DataExportSettings"
    ALERT_SUPPRESSION_SETTING = "AlertSuppressionSetting"
    ALERT_SYNC_SETTINGS = "AlertSyncSettings"

class SettingName(str, Enum, metaclass=CaseInsensitiveEnumMeta):
    """SettingName.
    """

    MCAS = "MCAS"
    WDATP = "WDATP"
    WDATP_EXCLUDE_LINUX_PUBLIC_PREVIEW = "WDATP_EXCLUDE_LINUX_PUBLIC_PREVIEW"
    SENTINEL = "Sentinel"
