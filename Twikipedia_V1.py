import wikipedia
import tweepy

textoTweet = [281]
nTweet = [281]

chave_consumidor = ""
segredo_consumidor = ""
token_acesso = ""
token_acesso_secreto = ""

autenticacao = tweepy.OAuthHandler(chave_consumidor, segredo_consumidor)
autenticacao.set_access_token(token_acesso, token_acesso_secreto)

twitter = tweepy.API(autenticacao)
user = twitter.get_user('twitter')

def buscaTweet():
    resultados = tweepy.Cursor(twitter.search, q='@Twikipedia_', tweet_mode="extended").items(1 )
    proTweet = [281]
    for tweet in resultados:
        proTweet = tweet.full_text
        tamTweet = len(proTweet)
        idTweet = tweet.id
        for contTweet in range(13, 281):
            textoTweet = proTweet[13:269]
    nTweet = textoTweet
    print (nTweet)
    wikipedia.set_lang("pt")
    texto = [281]
    try:
        try:
            texto = wikipedia.summary(title=nTweet)
        except ValueError:
            buscaTweet()
            try:
                twitter.update_status("Você digitou uma palavra inválida, tente novamente!", in_reply_to_status_id=idTweet, auto_populate_reply_metadata=True)
                buscaTweet()
            except ValueError:
                buscaTweet()
        tamTexto = len(texto)
        for c in range(0, 280):
            texto = texto[0:280]
            if c>200:
                if "." in texto[c]:
                    posPonto = c
        for a in range(0,posPonto):
            texto = texto[0:posPonto+1]
            print(f"Posição do ponto: {posPonto}")
        print (f"A palavra é: {nTweet}")
        print (f"O tamanho do texto encontrado é {tamTexto}")
        print (texto)
        try:
            twitter.update_status(texto, in_reply_to_status_id=idTweet, auto_populate_reply_metadata=True)
        except ValueError:
            print("Não faz nada")
    except:
        buscaTweet()

while(1):
    buscaTweet()
