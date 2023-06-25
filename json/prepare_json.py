#!/usr/bin/python3
import json


def key(chapterNo, verseNo):
    return str(chapterNo) + ":" + str(verseNo)

with open("abdelhaleem.json","r") as f:
    translation_json = json.load(f)
with open("quran-simple-min.txt","r") as f:
    simple_text = f.readlines();
with open("uthmani.txt","r") as f:
    uthmani_text = f.readlines();
with open("surah.json","r") as f:
    surah_json = json.load(f)

translation_dict = {}

for item in translation_json["quran"]:
    chapterNo = item["chapter"]
    verseNo = item["verse"]
    text = item["text"].strip()
    translation_dict[key(chapterNo, verseNo)] = text

uthmani_dict = {}
for line in uthmani_text:
    splits = line.split("|")
    if len(splits) > 2:
        arabic = splits[2].strip()
        chapterNo = splits[0]
        verseNo = splits[1]
        uthmani_dict[key(chapterNo, verseNo)] = arabic

output = {}

surah_names = {}
for s in surah_json:
    id = str(s["id"])
    name = s["transliteration"]
    print(id)
    surah_names[id] = name

for line in simple_text:
    splits = line.split("|")
    if len(splits) > 2:
        arabic = splits[2].strip()
        chapterNo = splits[0]
        verseNo = splits[1]

        translation = translation_dict[key(chapterNo, verseNo)]
        output[key(chapterNo, verseNo)] = {
            "chapter": chapterNo,
            "surah": surah_names[chapterNo],
            "verse": verseNo,
            "simple": arabic,
            "uthmani": uthmani_dict[key(chapterNo, verseNo)],
            "translation": translation_dict[key(chapterNo, verseNo)]
        }

with open("quran.json", "w", encoding='utf8') as f:
    f.write("const quran=")
    json.dump(output, f, ensure_ascii=False)
    f.write(";")
