from __future__ import annotations

from substack_sync.download_failed import DownloadFailed
from substack_sync.download_succeeded import DownloadSucceeded

DownloadOutcome = DownloadSucceeded | DownloadFailed
