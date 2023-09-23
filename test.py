meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROLF": "tangapan kepada joke",
            "SHEEESH": "tidak setuju ato kaget",
            "LOLLL" : "joke yang funny banget"
            }
while True:
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ")


    if word in meme_dict.keys():
        print(meme_dict[word])
        break
    else:
        print('WORD NOT FOUND')
