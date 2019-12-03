# raspberry-api

Per utilizzare un Raspberry Pi come server per ricezione di API occorrerà installare un framework web di Python chiamato Flask.

Per prima cosa occorre installare il package manager di Phyton (pip): <b>sudo apt-get install python-pip</b>.

Successivamente si dovrà installare il modulo Flask: <b>sudo pip install flask</b>.

A questo punto si deve scaricare il file <b>app.py</b> presente nel progetto di GitHub, modificare l'indirizzo IP nel file (di default è impostato su *'192.168.1.100'*) e avviarlo tramite terminale: <b>sudo python app.py</b>.

Aprendo una pagina web e digitando:  <b>http://INDIRIZZO-IP/api/v1.0/getRange/TIMESTAMP1/TIMESTAMP2/</b>  (per es. <b>http://192.168.1.100/api/v1.0/getRange/1574152807/1574152808/</b>) si otterrà un Json contenente tutti i timestamp con rispettive predizioni contenute dai due timestamp in input (funzione ancora da implementare).

Una volta che il progetto è completo occorrerà seguire questa procedura https://flask.palletsprojects.com/en/1.1.x/tutorial/deploy/ per passare da un server di sviluppo a un server di produzione.

Ps: nel file sono presenti tutti i commenti per la compresione del codice.
