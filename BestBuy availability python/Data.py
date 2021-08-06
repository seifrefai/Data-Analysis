data= {
    'urls': ['https://www.bestbuy.com/site/microsoft-xbox-series-x-1tb-console-black/6428324.p?skuId=6428324',
    'https://www.bestbuy.com/site/microsoft-xbox-elite-wireless-controller-series-2-for-xbox-one-xbox-series-x-and-xbox-series-s-black/6352703.p?skuId=6352703',
    'https://www.bestbuy.com/site/microsoft-xbox-series-s-512-gb-all-digital-console-disc-free-gaming-white/6430277.p?skuId=6430277'
    #add more links here if needed
    ],

    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '\
    'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 '\
    'Safari/537.36'
    
}
headers={'User-Agent': data['User-Agent']} 
urls= data['urls']

