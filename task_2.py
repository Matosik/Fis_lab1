cipher ="r2Я Ь9К>>К2ЙЬБt ЬrДЫt12<Д>>tr82tМ<КЫ1ХО>12>t<rЬЧ82ЯК КБrtАДХО>12ЯЬ2ЙЬБЬrЬ<02Я Ь>ОДЫ>Оr02ЬЕК>ЯКatrД12r2Е0Б0cК<2Ф..КЙОtrЫЬК2ЯЬ2r К<КЫt2БКЙЬБtЬrДЫtК2>ЛДОЬАЬ2ОКЙ>ОД2ЫЬ2r<К>ОК2>2tМ<КЫКЫtК<2Д>ЯЬЧЬЛКЫt12ЬО КМЙЬr2>ЬЬОrКО>Оr0Хct32>t<rЬЧД<2r2ЙЬБЬrЬ<2ЯЬ>О ДЫ>ОrК2tМ<КЫ1КО>12ОДЙЛК2t2ЯКБ>ОДrЧКЫt12>ЛДО832>t<rЬЧЬr2ОЬ2К>О,2r2ЫДbt32ОК <tЫД32bt.ЬЕЬМЫДaКЫt1?2ЫДЯ t<К 2ЯККБrtЫ0r2>t<rЬЧ2r2tМ2ЙЬЫ9Д2ЙЬБЬrЬАЬ2Я Ь>ОДЫ>ОrД2r2ЫДaДЧЬ2ЙЬБt0ХcКК2МЫДaКЫtК2<ЬЛКО2r8АЧ1БКО,2ЫК2ЙДЙ2МДЯЧДЫtЬrДЫЫЬК2tМЫДaДЧ,ЫЬ2Д2ЯЬБ0АЬ<02>ЬЬОrКО>ОrКЫЫЬ2<КЫ1ХО>12t2ЕtО82ЙЬБt 0ХctК2ЫДbК2КМ0Ч,Оt 0ХcКК2МЫДaКЫtК2rБЬЕДrЬЙ2ДБДЯОtrЫЬ<2ДЧАЬО<К2r>К2<КЫ1КО>12БtЫД<taК>Йt2ЯЬ>ЧК2tМ<КЫКЫt12ЙДЛБЬАЬ2>t<rЬЧ"
ended=[]

def character_mark():
    for i in range(len(cipher)):
        if(cipher[i] not in ended):
            ended.append(cipher[i])
            loc_counter=0
            for j in range(i,len(cipher)):
                if(cipher[i]==cipher[j]):
                    loc_counter+=1
            val=loc_counter/len(cipher)
            print(cipher[i], " - ", loc_counter/len(cipher), "counter = ", loc_counter)
        else:
            continue


character_mark()
cipher= cipher.replace("r", "в")
cipher= cipher.replace("Я", "п")
cipher= cipher.replace(" ", "р")
cipher= cipher.replace("Ь", "о")
cipher= cipher.replace("9", "ц")
cipher= cipher.replace("К", "е")
cipher= cipher.replace("Й", "к")
cipher= cipher.replace("Б", "д")
cipher= cipher.replace("t", "и")
cipher= cipher.replace("Д", "а")
cipher= cipher.replace("Ы", "н")
cipher= cipher.replace("1", "я")
cipher= cipher.replace("<", "м")
cipher= cipher.replace("8", "ы")
cipher= cipher.replace("М", "з")
cipher= cipher.replace("Х", "ю")
cipher= cipher.replace("О", "т")
cipher= cipher.replace("Ч", "л")
cipher= cipher.replace("А", "г")
cipher= cipher.replace("0", "у")
cipher= cipher.replace("Е", "б")
cipher= cipher.replace("a", "ч")
cipher= cipher.replace("c", "щ")
cipher= cipher.replace("Ф", "э")
cipher= cipher.replace(".", "ф")
cipher= cipher.replace("Л", "ж")
cipher= cipher.replace(">", "с")
cipher= cipher.replace("3", "х")
cipher= cipher.replace(",", "ь")
cipher= cipher.replace("2", " ")
cipher= cipher.replace("b", "ш")


print("\n\n",cipher)