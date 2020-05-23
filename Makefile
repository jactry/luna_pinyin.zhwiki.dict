FILENAME=zhwiki-20200501-all-titles-in-ns0

all: build

build: luna_pinyin.zhwiki.dict.yaml

download: $(FILENAME).gz

$(FILENAME).gz:
	wget https://dumps.wikimedia.org/zhwiki/20200501/$(FILENAME).gz

$(FILENAME): $(FILENAME).gz
	gzip -k -d $(FILENAME).gz

luna_pinyin.zhwiki.dict.yaml: $(FILENAME)
	./convert.py $(FILENAME) > luna_pinyin.zhwiki.dict.yaml
