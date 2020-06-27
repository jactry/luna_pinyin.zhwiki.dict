VERSION=20200620
FILENAME=zhwiki-$(VERSION)-all-titles-in-ns0

all: build

build: luna_pinyin.zhwiki.dict.yaml

download: $(FILENAME).gz

$(FILENAME).gz:
	wget https://dumps.wikimedia.org/zhwiki/$(VERSION)/$(FILENAME).gz

$(FILENAME): $(FILENAME).gz
	gzip -k -d $(FILENAME).gz

web-slang.source:
	./zhwiki-web-slang.py > web-slang.source

zhwiki.source: $(FILENAME) web-slang.source
	cat $(FILENAME) web-slang.source > zhwiki.source

luna_pinyin.zhwiki.dict.yaml: zhwiki.source
	./convert.py zhwiki.source $(VERSION) > luna_pinyin.zhwiki.dict.yaml
