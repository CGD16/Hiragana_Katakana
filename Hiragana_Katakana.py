import time
import random


dict_jap = {
    'a': 'あ ア', 'i': 'い イ', 'u':'う ウ', 'e':'え エ', 'o':'お オ',
    'ka':'か カ', 'ki':'き キ', 'ku':'く ク', 'ke':'け ケ', 'ko':'こ コ',
    'sa':'さ サ', 'shi':'し シ', 'su':'す ス', 'se':'せ セ', 'so':'そ ソ',
    'ta':'た タ', 'chi':'ち チ', 'tsu':'つ ツ', 'te':'て テ', 'to':'と ト',
    'na':'な ナ', 'ni':'に ニ', 'nu':'ぬ ヌ', 'ne':'ね ネ', 'no':'の ノ',
    'ha':'は ハ', 'hi':'ひ ヒ', 'fu':'ふ フ', 'he':'へ ヘ', 'ho':'ほ ホ',
    'ma':'ま マ', 'mi':'み ミ', 'mu':'む ム', 'me':'め メ', 'mo':'も モ',
    'ya': 'や ヤ', 'fu':'ゆ ユ', 'yo':'よ ヨ',
    'ra':'ら ラ', 'ri':'り リ', 'ru':'る ル', 're':'れ レ', 'ro':'ろ ロ',
    'wa': 'わ ワ', 'wo':'を ヲ',
    
    'ga':'が ガ', 'gi':'ぎ ギ', 'gu':'ぐ グ', 'ge':'げ ゲ', 'go':'ご ゴ',
    'za':'ざ ザ', 'ji':'じ ジ', 'zu':'ず ズ', 'ze':'ぜ ゼ', 'zo':'ぞ ゾ',
    'da':'だ ダ', 'dji':'ぢ ヂ', 'dzu':'ず ヅ', 'de':'で デ', 'do':'ど ド',
    'ba':'ば バ', 'bi':'び ビ', 'bu':'ぶ ブ', 'be':'べ ベ', 'bo':'ぼ ボ',
    'pa':'ぱ パ', 'pi':'ぴ ピ', 'pu':'ぷ プ', 'pe':'ぺ ペ', 'po':'ぽ ポ',
    'n': 'ん ン',

    'kya':'きゃ キャ', 'kyu':'きゅ キュ', 'kyo':'きょ キョ',
    'sha':'しゃ シャ', 'shu':'しゅ シュ', 'sho':'しょ ショ',
    'cha':'ちゃ チャ', 'chu':'ちゅ チュ', 'cho':'ちょ チョ',
    'nya':'にゃ ニャ', 'nyu':'にゅ ニュ', 'nyo':'にょ ニョ',
    'hya':'ひゃ ヒャ', 'hyu':'ひゅ ヒュ', 'hyo':'ひょ ヒョ',
    'mya':'みゃ ミャ', 'myu':'みゅ ミュ', 'myo':'みょ ミョ',
    'rya':'りゃ リャ', 'ryu':'りゅ リュ', 'ryo':'りょ リョ',

    'gya':'ぎゃ ギャ', 'gyu':'ぎゅ ギュ', 'gyo':'ぎょ ギョ',
    'ja':'じゃ ジャ', 'ju':'じゅ ジュ', 'jo':'じょ ジョ',
    'bya':'びゃ ビャ', 'byu':'びゅ ビュ', 'byo':'びょ ビョ',
    'pya':'ぴゃ ピャ','pyu':'ぴゅ ピュ', 'pyo':'ぴょ ピョ'
    }



if __name__ == "__main__":
    eingabe = input("Eingabe für die Anzahl der Zeichen, die du lernen möchtest (Zahl/'alle'): ").strip()
    if eingabe.lower() == "alle":
        number_of_signs = len(dict_jap) 
    else:
        try:
            number_of_signs = int(eingabe)
            if number_of_signs > len(dict_jap):
                print(f"Es gibt nur {len(dict_jap)} Zeichen. Alle werden verwendet.")
                number_of_signs = len(dict_jap)
        except ValueError:
            print("Ungültige Eingabe. Es werden alle Zeichen verwendet.")
            number_of_signs = len(dict_jap)

   
    mode = input("Möchtest du Hiragana (H), Katakana (K) oder beides (beliebige Eingabe) lernen? ").strip().upper()

    romanji_list = list(dict_jap.keys())
    random.shuffle(romanji_list)
    romanji_list = romanji_list[:number_of_signs]

    for i, romanji in enumerate(romanji_list):
        print(f"{i + 1} Romanji: {romanji}")
        hiragana, katakana = dict_jap[romanji].split(" ")
        time.sleep(20) 

        if mode == "H":
            print(f"Hiragana: {hiragana} \n")
        elif mode == "K":
            print(f"Katakana: {katakana} \n")
        else:
            print(f"Hiragana: {hiragana}")
            print(f"Katakana: {katakana} \n")

    # Ergebnisse abfragen
    print("Wie viele hast du nun richtig? ")
    zahl = int(input("Gebe eine Zahl ein: \n"))
    print(f"Du hast {round(zahl / (len(romanji_list) * 2 if mode not in ['H', 'K'] else len(romanji_list)) * 100, 2)}% erreicht")

