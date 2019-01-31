# import MeCab

# test = "今日はいい天気ですね。遊びに行かない？新宿で祭りがある！"

# m = MeCab.Tagger()

# parsed =  m.parseToNode(test)

# components = []

# while parsed:
	# components.append(parsed.surface)
	# parsed = parsed.next
	
# print(components)

import MeCab
text = "RT @seira_j_tpd_: ソフトクリームを狙おうとする上西星来🍦💓🍦⭐️🍦💓ソフトクリーム アイス 夏上西星来 今日はどんな日になるかな〜 https://t.co/dtMJvtmCof"
tagger = MeCab.Tagger("-Ochasen")
mecab_result = tagger.parse(text)

print(mecab_result)