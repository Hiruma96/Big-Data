# Big-Data
Per la realizzazione di questo progetto sono stati effettuati 2 tipi di test:

-implementazione ed esecuzione di due algoritmi per la risoluzione del problema trattato, valutando le performance e trovando il migliore tra i due (entrambi testati su colab);

-esecuzione dell’algoritmo dalle performance migliori, trovato in precedenza, su Colab e sulle macchine EC2 di aws in clustering.


Per la prima parte basterà scaricare il file "ConfrontoAlgoritmi.ipynb" ed il dataset "tweets.xls", caricarli su colab ed eseguire il codice. Il risultato saranno i valori di accuracy, precision, recall e f1-score dei due algoritmi LogisticRegression e DecisionTreeClassifier.

Per la seconda parte, invece, si dovrà scaricare il dataset "tweets.xls" ed i file "LogisticRegression.py" e "LogisticRegression.ipynb" (stesso file, ma per convenienza fornito sia in versione python che in versione per notebook di colab). Il file .ipynb andrà eseguito su colab, così da ottenere il tempo di esecuzione.
Mentre, per la il file .py, andrà caricato su aws dopo aver creato le macchine ec2 e averle collegate al cluster tramite spark.
Per far ciò bisognerà seguire la guida sottostante.


Guida all’utilizzo

Per far partire il progetto sulle macchine AWS abbiamo bisogno di utilizzare Terraform. Prima di passare ai comandi per lanciare Terraform e Spark, abbiamo bisogno di un account AWS, aver installato aws-cli sul proprio ambiente e aver generato una coppia di chiavi su aws.
Di seguito i comandi:

-Posizionarsi sulla cartella Terraform col terminale

-Digitare: terraform init

-Digitare: terraform apply

-Entrare nel proprio account aws

-Connettersi alle istanze in ssh

-Impostare nel file etc/hosts di sistema gli ip di ogni istanza

-Digitare sul nodo master: 	

    -hdfs namenode -format
    
    -$HADOOP HOME/sbin/start-dfs.sh
    
    -$HADOOP HOME/sbin/start-yarn.sh
    
    -$HADOOP HOME/sbin/mr-jobhistory-daemon.sh start historyserver
    
    -./spark/sbin/start-all.sh
    
per far partire sull’istanza principale Spark e un worker

-Digitare sulle istanze secondarie: ./spark/sbin/start-slave.sh ADDRESS (dove l’address è l’indirizzo ip fornito da spark)

In questo modo terraform crea le istanze su aws e spark viene avviato.

