import requests
import time
from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info, requires_filesystem_watcher

@requires_filesystem_watcher
@requires_segment_info
class BTCPriceFeedSegment(Segment):
    divider_highlight_group = None

    def __call__(self, pl, segment_info, create_watcher):
        time.sleep(10)
        resp = requests.get('https://api.binance.com/api/v3/avgPrice?symbol=BTCUSDT')
        return [{
            'contents': f'BTC {int(float(resp.json()["price"]))}',
            'highlight_groups': ['btc'],
        }]

btc = with_docstring(BTCPriceFeedSegment(), '''Return a custom segment.''')


@requires_filesystem_watcher
@requires_segment_info
class ETHPriceFeedSegment(Segment):
    divider_highlight_group = None

    def __call__(self, pl, segment_info, create_watcher):
        time.sleep(10)
        resp = requests.get('https://api.binance.com/api/v3/avgPrice?symbol=ETHUSDT')
        return [{
            'contents': f'ETH {int(float(resp.json()["price"]))}',
            'highlight_groups': ['eth'],
        }]

eth = with_docstring(ETHPriceFeedSegment(), '''Return a custom segment.''')


@requires_filesystem_watcher
@requires_segment_info
class SNXPriceFeedSegment(Segment):
    divider_highlight_group = None

    def __call__(self, pl, segment_info, create_watcher):
        time.sleep(10)
        resp = requests.get('https://api.binance.com/api/v3/avgPrice?symbol=SNXUSDT')
        return [{
            'contents': f'SNX {str(round(float(resp.json()["price"]), 2))}',
            'highlight_groups': ['snx'],
        }]

snx = with_docstring(SNXPriceFeedSegment(), '''Return a custom segment.''')
