Das Vorgehen:

Zuerst wird über readsensor_newApp_1.1.py die Bewegung erfasst und im CSV-Format gespeichert.
Parallel dazu werden Videos von der Bewegung aufgenommen.
Mit statisticsV2.py werden nun überlappede Zeitfenster erstellt und zu den Fenster jeweils Mittelwert und Standardabweichung der drei Achsen berechnet.
Anschließend werden anhand des Videos die einzelnen Bewegungen aus der Datei extrahiert und jeweils in separate Dateien gespeichert.
Die entstandenen Daten werden nun mittels training_data_preprocessor.py für den Decision-Tree vorbereitet.
Jetzt können die Daten mit tree_creator_1.1.py in einen Baum gespeist werden.
Dieser kann mit tree_test_10.py getestet werden.
Für Details siehe Dokumentation der Python-Files.
