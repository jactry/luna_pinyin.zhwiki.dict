VERSION=20200520
FILENAME=zhwiki-$(VERSION)-all-titles-in-ns0

all: build

build: luna_pinyin.zhwiki.dict.yaml

download: $(FILENAME).gz

$(FILENAME).gz:
	wget https://dumps.wikimedia.org/zhwiki/$(VERSION)/$(FILENAME).gz

$(FILENAME): $(FILENAME).gz
	gzip -k -d $(FILENAME).gz

luna_pinyin.zhwiki.dict.yaml: $(FILENAME)
	./convert.py $(FILENAME) $(VERSION) > luna_pinyin.zhwiki.dict.yaml
