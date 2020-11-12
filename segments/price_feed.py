import requests
from powerline.segments import Segment, with_docstring
from powerline.theme import requires_segment_info, requires_filesystem_watcher

@requires_filesystem_watcher
@requires_segment_info
class BTCPriceFeedSegment(Segment):
    divider_highlight_group = None

    def __call__(self, pl, segment_info, create_watcher):
        resp_btc = requests.get('https://api.coinbase.com/v2/prices/btc-usd/spot?currency=usd')
        return [{
            'contents': f'BTC {resp_btc.json()["data"]["amount"]}',
            'highlight_groups': ['btc'],
        }]

btc = with_docstring(BTCPriceFeedSegment(), '''Return a custom segment.''')


@requires_filesystem_watcher
@requires_segment_info
class ETHPriceFeedSegment(Segment):
    divider_highlight_group = None

    def __call__(self, pl, segment_info, create_watcher):
        resp = requests.get('https://api.coinbase.com/v2/prices/eth-usd/spot?currency=usd')
        return [{
            'contents': f'ETH {resp.json()["data"]["amount"]}',
            'highlight_groups': ['eth'],
        }]

eth = with_docstring(ETHPriceFeedSegment(), '''Return a custom segment.''')
