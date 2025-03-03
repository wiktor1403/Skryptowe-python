# Skryptowe-python

Projekt chatbota

Przy pomocy rasa stworozny model chata który został zintegrowany z slack.
W projektcie zostały uzupełnione wszelkie credentials ponieważ obszar w slack i bot został stworzony wyłącznie na potrzeby edukacyjne i testowe.

W celu uruchomienia bota na własnym środowisku slack należy uzupełnić plik credentials.yml odpowiednimi tokenami.
Aby wytrnować owy model w terminalu folderu projektu należy uruchomić komendę rasa train.
Wykonanie jej wyprodukuje nowy model w folderze models.
Następnie należy uruchomić komendę rasa rasa run actions w celu wystawienia endpointu dla zadeklarowanych akcji w pliku actions.py.
Ostatnią komendą rasa jest rasa run --enable-api --debug pozwoli na uruchomienie modelu i aktywację API. 

Aby integracja była możliwa skorzystano w projekcie z ngrok.
Należy wywołać comendę ngrok http 5005 co spowoduje utworzenie adresu umożliwiającego zapytania z sieci.
Zwrot tej komendy powinien wyglądać w następujący sposób:
Session Status                online
Account                       *adres email*
Version                       3.20.0
Region                        Europe (eu)
Latency                       23ms
Web Interface                 http://127.0.0.1:4040
Forwarding                    https://d116-77-255-152-242.ngrok-free.app -> http://localhost:5005

Connections                   ttl     opn     rt1     rt5     p50     p90     
                              31      0       0.00    0.00    90.14   90.15   

Adres z lini Forwarding posłużył jako adres do komunikacji z modelem rasa w tym przypadku tj. https://d116-77-255-152-242.ngrok-free.app
Ten adres wraz z wskazanymi web server routes posłużył do utworzenie rquest URL z którym komunikuje się aplikacja w SLACK według modelu: "adres z forwarding" + "odpowiedni web server rout" w tym przypadku https://d116-77-255-152-242.ngrok-free.app/webhooks/slack/webhook

Przy tworzeniu bota po stronie slacka posłużono się dokumntacją:
https://rasa.com/docs/rasa/connectors/slack/

Wynik:
![Alt text](relative%20path/to/img.jpg?raw=true "Zrzut ekranu 2025-03-03 190519.png")

Dodatkowa opinia autora:
Znacznie łatwiej jest stworzyć integrację z Slack niż Webex
