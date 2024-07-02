#save_data.sh
#!/bin/bash

# Setari pentru baza de date InfluxDB
DATABASE="mydb"
BACKUP_DATABASE="local_backup"

# Comanda pentru a salva datele din ultima ora
influx -database $DATABASE -execute "SELECT * INTO $BACKUP_DATABASE FROM sensor_data WHERE time > now() - 1h"

# Verifica daca backup-ul a reusit si salveaza rezultatul intr-un fisier log
if [ $? -eq 0 ]; then
    echo "$(date) - Backup reusit" >> /var/log/influxdb_backup.log
else
    echo "$(date) - Backup esuat" >> /var/log/influxdb_backup.log
fi