BOT_NAME = 'bancastabiese'

SPIDER_MODULES = ['bancastabiese.spiders']
NEWSPIDER_MODULE = 'bancastabiese.spiders'
FEED_EXPORT_ENCODING = 'utf-8'
LOG_LEVEL = 'ERROR'
DOWNLOAD_DELAY = 0

ROBOTSTXT_OBEY = True

ITEM_PIPELINES = {
	'bancastabiese.pipelines.BancastabiesePipeline': 100,

}