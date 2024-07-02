# resync_data.sh
#!/bin/bash

# Setari pentru baza de date InfluxDB
DATABASE="mydb"
BACKUP_DATABASE="local_backup"

# Comanda pentru a copia datele din backup in baza de date principala
influx -database $BACKUP_DATABASE -execute "SELECT * INTO $DATABASE FROM sensor_data"

# Verifica daca resincronizarea a reusit si salveaza rezultatul intr-un fisier log
if [ $? -eq 0 ]; then
    echo "$(date) - Resincronizare reusită" >> /var/log/influxdb_resync.log
else
    echo "$(date) - Resincronizare esuată" >> /var/log/influxdb_resync.log
fi
