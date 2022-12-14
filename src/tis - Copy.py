from datetime import datetime, timedelta
dt = datetime.now()
ts = dt.strftime('%Y%m%d%H%M%S')

import os
import sys
wd = os.path.dirname(os.path.abspath(sys.argv[0]))
logs = os.path.join(wd, 'logs')

log = os.path.join(logs, 'python_' + str(ts) + '.log')

import logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers = [
        logging.FileHandler(log),
        logging.StreamHandler(sys.stdout)
    ]
)

logging.info("Logging enabled.")
import socket
hostname = socket.gethostname()
main = os.path.basename(__file__)
logging.info("The script was executed from \"" + main + "\", located in the \
    path-prefix \"" + wd + "\" on the machine \"" + hostname + "\".")

from remove import remove_files, remove_old_files, remove_tree
remove_old_files(logs, 7)

regions = os.path.join(wd, 'regions')

import lxml.etree as et
def count_mu_nodes(path_prefix):
    tree = et.parse(os.path.join(path_prefix, 'MU-NODE-LIST001.xml'))
    return int(tree.xpath('count(//MU-NODE-LIST/MU-NODE)'))

val_count = {
    'a': {},
    'bfw': {},
    'c': {},
    'g': {},
    'h': {},
    'l': {},
    'nr': {},
    'o': {}
}

log_dir = os.path.join(logs, 'tis_' + str(ts))
os.mkdir(log_dir)
from dbcmd import DbCmd
dbcmd91 = DbCmd('172.31.240.82', '1521', 'AST91', 'system', 'enterprise', log_dir)

logging.info("Exporting region A.")
logging.info("Removing exported data...")
remove_files(os.path.join(regions, 'a', 'property'))
remove_files(os.path.join(regions, 'a', '2g'))
remove_files(os.path.join(regions, 'a', '3g'))
remove_files(os.path.join(regions, 'a', '4g'))
remove_files(os.path.join(regions, 'a', 'repeater'))
logging.info("Exporting data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '00_PROD_ASSET_91',
    '7',
    'DEXPORT',
    'Ericsson1',
    os.path.join(regions, 'a.txt')
)
val_count['a'].update(
    {
        'gsm': count_mu_nodes(os.path.join(regions, 'a', '2g')),
        'umts': count_mu_nodes(os.path.join(regions, 'a', '3g')),
        'lte': count_mu_nodes(os.path.join(regions, 'a', '4g'))
    }
)
logging.info("Done.")

logging.info("Exporting region BFW.")
logging.info("Removing exported data...")
remove_files(os.path.join(regions, 'bfw', 'property'))
remove_files(os.path.join(regions, 'bfw', '2g'))
remove_files(os.path.join(regions, 'bfw', '3g'))
remove_files(os.path.join(regions, 'bfw', '4g'))
remove_files(os.path.join(regions, 'bfw', 'repeater'))
logging.info("Exporting data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '00_PROD_ASSET_91',
    '8',
    'DEXPORT',
    'Ericsson1',
    os.path.join(regions, 'bfw.txt')
)
val_count['bfw'].update(
    {
        'gsm': count_mu_nodes(os.path.join(regions, 'bfw', '2g')),
        'umts': count_mu_nodes(os.path.join(regions, 'bfw', '3g')),
        'lte': count_mu_nodes(os.path.join(regions, 'bfw', '4g'))
    }
)
logging.info("Done.")

logging.info("Exporting region C.")
logging.info("Removing exported data...")
remove_files(os.path.join(regions, 'c', 'property'))
remove_files(os.path.join(regions, 'c', '2g'))
remove_files(os.path.join(regions, 'c', '3g'))
remove_files(os.path.join(regions, 'c', '4g'))
remove_files(os.path.join(regions, 'c', 'repeater'))
logging.info("Exporting data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '00_PROD_ASSET_91',
    '25',
    'DEXPORT',
    'Ericsson1',
    os.path.join(regions, 'c.txt')
)
val_count['c'].update(
    {
        'gsm': count_mu_nodes(os.path.join(regions, 'c', '2g')),
        'umts': count_mu_nodes(os.path.join(regions, 'c', '3g')),
        'lte': count_mu_nodes(os.path.join(regions, 'c', '4g'))
    }
)
logging.info("Done.")

logging.info("Exporting region G.")
logging.info("Removing exported data...")
remove_files(os.path.join(regions, 'g', 'property'))
remove_files(os.path.join(regions, 'g', '2g'))
remove_files(os.path.join(regions, 'g', '3g'))
remove_files(os.path.join(regions, 'g', '4g'))
remove_files(os.path.join(regions, 'g', 'repeater'))
logging.info("Exporting data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '00_PROD_ASSET_91',
    '26',
    'DEXPORT',
    'Ericsson1',
    os.path.join(regions, 'g.txt')
)
val_count['g'].update(
    {
        'gsm': count_mu_nodes(os.path.join(regions, 'g', '2g')),
        'umts': count_mu_nodes(os.path.join(regions, 'g', '3g')),
        'lte': count_mu_nodes(os.path.join(regions, 'g', '4g'))
    }
)
logging.info("Done.")

logging.info("Exporting region H.")
logging.info("Removing exported data...")
remove_files(os.path.join(regions, 'h', 'property'))
remove_files(os.path.join(regions, 'h', '2g'))
remove_files(os.path.join(regions, 'h', '3g'))
remove_files(os.path.join(regions, 'h', '4g'))
remove_files(os.path.join(regions, 'h', 'repeater'))
logging.info("Exporting data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '00_PROD_ASSET_91',
    '33',
    'DEXPORT',
    'Ericsson1',
    os.path.join(regions, 'h.txt')
)
val_count['h'].update(
    {
        'gsm': count_mu_nodes(os.path.join(regions, 'h', '2g')),
        'umts': count_mu_nodes(os.path.join(regions, 'h', '3g')),
        'lte': count_mu_nodes(os.path.join(regions, 'h', '4g'))
    }
)
logging.info("Done.")

logging.info("Exporting region L.")
logging.info("Removing exported data...")
remove_files(os.path.join(regions, 'l', 'property'))
remove_files(os.path.join(regions, 'l', '2g'))
remove_files(os.path.join(regions, 'l', '3g'))
remove_files(os.path.join(regions, 'l', '4g'))
remove_files(os.path.join(regions, 'l', 'repeater'))
logging.info("Exporting data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '00_PROD_ASSET_91',
    '36',
    'DEXPORT',
    'Ericsson1',
    os.path.join(regions, 'l.txt')
)
val_count['l'].update(
    {
        'gsm': count_mu_nodes(os.path.join(regions, 'l', '2g')),
        'umts': count_mu_nodes(os.path.join(regions, 'l', '3g')),
        'lte': count_mu_nodes(os.path.join(regions, 'l', '4g'))
    }
)
logging.info("Done.")

logging.info("Exporting region NR.")
logging.info("Removing exported data...")
remove_files(os.path.join(regions, 'nr', 'property'))
remove_files(os.path.join(regions, 'nr', '2g'))
remove_files(os.path.join(regions, 'nr', '3g'))
remove_files(os.path.join(regions, 'nr', '4g'))
remove_files(os.path.join(regions, 'nr', 'repeater'))
logging.info("Exporting data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '00_PROD_ASSET_91',
    '37',
    'DEXPORT',
    'Ericsson1',
    os.path.join(regions, 'nr.txt')
)
val_count['nr'].update(
    {
        'gsm': count_mu_nodes(os.path.join(regions, 'nr', '2g')),
        'umts': count_mu_nodes(os.path.join(regions, 'nr', '3g')),
        'lte': count_mu_nodes(os.path.join(regions, 'nr', '4g'))
    }
)
logging.info("Done.")

logging.info("Exporting region O.")
logging.info("Removing exported data...")
remove_files(os.path.join(regions, 'o', 'property'))
remove_files(os.path.join(regions, 'o', '2g'))
remove_files(os.path.join(regions, 'o', '3g'))
remove_files(os.path.join(regions, 'o', '4g'))
remove_files(os.path.join(regions, 'o', 'repeater'))
logging.info("Exporting data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '00_PROD_ASSET_91',
    '38',
    'DEXPORT',
    'Ericsson1',
    os.path.join(regions, 'o.txt')
)
val_count['o'].update(
    {
        'gsm': count_mu_nodes(os.path.join(regions, 'o', '2g')),
        'umts': count_mu_nodes(os.path.join(regions, 'o', '3g')),
        'lte': count_mu_nodes(os.path.join(regions, 'o', '4g'))
    }
)
logging.info("Done.")

for i in val_count:
    total = 0
    for j in val_count[i]:
        total += val_count[i][j]
    val_count[i].update({'total': total})

global_count = [sum(val_count[i]['total'] for i in val_count)]

logging.info("Importing data to reference...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '00_PROD_ASSET_91',
    '40',
    'DEXPORT',
    'Ericsson1',
    os.path.join(regions, 'reference.txt')
)
logging.info("Done.")

reference = os.path.join(wd, 'reference')
logging.info("Removing reference exported data...")
remove_files(os.path.join(reference, 'a'))
remove_files(os.path.join(reference, 'b'))
remove_files(os.path.join(reference, 'c'))
remove_files(os.path.join(reference, 'f'))
remove_files(os.path.join(reference, 'g'))
remove_files(os.path.join(reference, 'h'))
remove_files(os.path.join(reference, 'l'))
remove_files(os.path.join(reference, 'm'))
remove_files(os.path.join(reference, 'n'))
remove_files(os.path.join(reference, 'o'))
remove_files(os.path.join(reference, 'r'))
remove_files(os.path.join(reference, 'w'))
remove_files(os.path.join(reference, 'all'))
remove_files(os.path.join(reference, 'nodes', '2g'))
remove_files(os.path.join(reference, 'nodes', '3g'))
remove_files(os.path.join(reference, 'nodes', '4g'))

logging.info("Exporting reference data...")
dbcmd91.run(
    r'C:\Program Files\TEOCO\ENTERPRISE 9.1\DBCMD91.exe',
    '00_PROD_ASSET_91',
    '40',
    'DEXPORT',
    'Ericsson1',
    os.path.join(reference, 'export.txt')
)
logging.info("Done.")

output = os.path.join(wd, 'output')
logging.info("Removing processed files...")
remove_files(output)
logging.info("Done.")

from copy_file import copy_file, copy_files
logging.info("Processing files...")
copy_file(os.path.join(reference, 'a', 'GSM-CELL-LIST001.xml'), 
    os.path.join(output, 'GSM-CELL-A-LIST001.xml'))
copy_file(os.path.join(reference, 'a', 'UMTS-CELL-LIST001.xml'), 
    os.path.join(output, 'UMTS-CELL-A-LIST001.xml'))

copy_file(os.path.join(reference, 'b', 'GSM-CELL-LIST001.xml'), 
    os.path.join(output, 'GSM-CELL-B-LIST001.xml'))
copy_file(os.path.join(reference, 'b', 'UMTS-CELL-LIST001.xml'), 
    os.path.join(output, 'UMTS-CELL-B-LIST001.xml'))

copy_file(os.path.join(reference, 'c', 'GSM-CELL-LIST001.xml'), 
    os.path.join(output, 'GSM-CELL-C-LIST001.xml'))
copy_file(os.path.join(reference, 'c', 'UMTS-CELL-LIST001.xml'), 
    os.path.join(output, 'UMTS-CELL-C-LIST001.xml'))

copy_file(os.path.join(reference, 'f', 'GSM-CELL-LIST001.xml'), 
    os.path.join(output, 'GSM-CELL-F-LIST001.xml'))
copy_file(os.path.join(reference, 'f', 'UMTS-CELL-LIST001.xml'), 
    os.path.join(output, 'UMTS-CELL-F-LIST001.xml'))

copy_file(os.path.join(reference, 'g', 'GSM-CELL-LIST001.xml'), 
    os.path.join(output, 'GSM-CELL-G-LIST001.xml'))
copy_file(os.path.join(reference, 'g', 'UMTS-CELL-LIST001.xml'), 
    os.path.join(output, 'UMTS-CELL-G-LIST001.xml'))

copy_file(os.path.join(reference, 'h', 'GSM-CELL-LIST001.xml'), 
    os.path.join(output, 'GSM-CELL-H-LIST001.xml'))
copy_file(os.path.join(reference, 'h', 'UMTS-CELL-LIST001.xml'), 
    os.path.join(output, 'UMTS-CELL-H-LIST001.xml'))

copy_file(os.path.join(reference, 'l', 'GSM-CELL-LIST001.xml'), 
    os.path.join(output, 'GSM-CELL-L-LIST001.xml'))
copy_file(os.path.join(reference, 'l', 'UMTS-CELL-LIST001.xml'), 
    os.path.join(output, 'UMTS-CELL-L-LIST001.xml'))

copy_file(os.path.join(reference, 'm', 'GSM-CELL-LIST001.xml'), 
    os.path.join(output, 'GSM-CELL-M-LIST001.xml'))
copy_file(os.path.join(reference, 'm', 'UMTS-CELL-LIST001.xml'), 
    os.path.join(output, 'UMTS-CELL-M-LIST001.xml'))

copy_file(os.path.join(reference, 'n', 'GSM-CELL-LIST001.xml'), 
    os.path.join(output, 'GSM-CELL-N-LIST001.xml'))
copy_file(os.path.join(reference, 'n', 'UMTS-CELL-LIST001.xml'), 
    os.path.join(output, 'UMTS-CELL-N-LIST001.xml'))

copy_file(os.path.join(reference, 'o', 'GSM-CELL-LIST001.xml'), 
    os.path.join(output, 'GSM-CELL-O-LIST001.xml'))
copy_file(os.path.join(reference, 'o', 'UMTS-CELL-LIST001.xml'), 
    os.path.join(output, 'UMTS-CELL-O-LIST001.xml'))

copy_file(os.path.join(reference, 'r', 'GSM-CELL-LIST001.xml'), 
    os.path.join(output, 'GSM-CELL-R-LIST001.xml'))
copy_file(os.path.join(reference, 'r', 'UMTS-CELL-LIST001.xml'), 
    os.path.join(output, 'UMTS-CELL-R-LIST001.xml'))

copy_file(os.path.join(reference, 'w', 'GSM-CELL-LIST001.xml'), 
    os.path.join(output, 'GSM-CELL-W-LIST001.xml'))
copy_file(os.path.join(reference, 'w', 'UMTS-CELL-LIST001.xml'), 
    os.path.join(output, 'UMTS-CELL-W-LIST001.xml'))

copy_file(os.path.join(reference, 'all', 'LTE-CELL-LIST001.xml'), 
    os.path.join(output, 'LTE-CELL-LIST001.xml'))
copy_file(os.path.join(reference, 'all', 'NETWORK-LIST001.xml'), 
    os.path.join(output, 'NETWORK-LIST001.xml'))
copy_file(os.path.join(reference, 'all', 'PROPERTY-LIST001.xml'), 
    os.path.join(output, 'PROPERTY-LIST001.xml'))
copy_file(os.path.join(reference, 'all', 'REPEATER-LIST001.xml'), 
    os.path.join(output, 'REPEATER-LIST001.xml'))
copy_file(os.path.join(reference, 'all', 'SUPPLIER-LIST001.xml'), 
    os.path.join(output, 'SUPPLIER-LIST001.xml'))
copy_file(os.path.join(reference, 'all', 'ANTENNA-LIST001.xml'), 
    os.path.join(output, 'ANTENNA-LIST001.xml'))
copy_file(os.path.join(reference, 'all', 'CAR-LAYER-LIST001.xml'), 
    os.path.join(output, 'CAR-LAYER-LIST001.xml'))

copy_file(os.path.join(reference, 'nodes', '2g', 'MU-NODE-LIST001.xml'), 
    os.path.join(output, 'MU-NODE-2G-LIST001.xml'))
copy_file(os.path.join(reference, 'nodes', '3g', 'MU-NODE-LIST001.xml'), 
    os.path.join(output, 'MU-NODE-3G-LIST001.xml'))
copy_file(os.path.join(reference, 'nodes', '4g', 'MU-NODE-LIST001.xml'), 
    os.path.join(output, 'MU-NODE-4G-LIST001.xml'))
    
logging.info("Done.")

from ssh import SSH
import paramiko
pk_satisfaction = paramiko.RSAKey.from_private_key(
    open(
        os.path.join(wd, 'satisfaction', 'id_rsa')
    )
)
satisfaction_ssh = SSH(
    hostname = '192.168.89.9', username = 'eritrf01', pkey = pk_satisfaction
)
satisfaction_ssh.sftp()
logging.info("Seding files to satisfaction...")
satisfaction_path_prefix = '/CRMTRF01/IN/'
for file in os.listdir(output):
    satisfaction_ssh._ftp.put(
        os.path.join(output, file), satisfaction_path_prefix + file
    )
logging.info("Done.")

tis_exports = os.path.join(wd, 'tis_exports')
tis_backup_filename = 'tis_' + str(ts) + '.zip'
tis_backup_pathname = os.path.join(tis_exports, tis_backup_filename)
from zip import zip_dir
logging.info("Archiving and compressing REFERENCE data...")
zip_dir(output, tis_backup_pathname)
remove_old_files(tis_exports, 20)

from names import breakdown
log_basename = breakdown(log)[1]
from copy_file import copy_file
logging.info("Copying the log at this point...")
copy_file(log, os.path.join(log_dir, log_basename))

archive_filename = 'tis_' + str(ts) + '.zip'
archive_pathname = os.path.join(logs, archive_filename)
logging.info("Archiving and compressing logs...")
zip_dir(log_dir, archive_pathname)
remove_tree(log_dir)

dt_end = datetime.now()
diff = dt_end - dt
days, seconds = diff.days, diff.seconds
hours = days * 24 + seconds // 3600
minutes = (seconds % 3600) // 60
seconds = seconds % 60

hts = dt.strftime('%A, %B %d %Y, %H:%M:%S %p')
event_end_hts = dt_end.strftime('%A, %B %d %Y, %H:%M:%S %p')

templates = os.path.join(wd, 'templates')
import jinja2
logging.info("Authoring admin email template...")
templateLoader = jinja2.FileSystemLoader(searchpath=templates)
templateEnv = jinja2.Environment(loader=templateLoader)
TEMPLATE_FILE = 'admin.html'
template = templateEnv.get_template(TEMPLATE_FILE)
context = {
    'main': main,
    'wd': wd,
    'hostname': hostname,
    'output': output,
    'tis_backup_pathname': tis_backup_pathname,
    'regions': regions,
    'ts': str(ts),
    'hts': str(hts),
    'event_end_hts': str(event_end_hts),
    'hours': hours,
    'minutes': minutes,
    'seconds': seconds,
    'val_count': val_count,
    'global_count': global_count[0]
}
message_filename = 'tis_' + TEMPLATE_FILE
with open(os.path.join(wd, message_filename), 'wb') as f:
    f.write(template.render(**context).encode('utf-8'))

freetown_pk = paramiko.RSAKey.from_private_key(
    open(
        os.path.join(wd, 'freetown', 'id_rsa')
    )
)
freetown_ssh = SSH(hostname = '172.31.240.82', username = 'taskexec', pkey = freetown_pk)
freetown_ssh.sftp()
logging.info("Seding files to freetown...")
freetown_ssh._ftp.put(os.path.join(wd, message_filename), '/export/home/taskexec/send_mail/outbox/' + message_filename)
freetown_ssh._ftp.put(archive_pathname, '/export/home/taskexec/send_mail/outbox/' + archive_filename)
freetown_ssh.ssh('''python /export/home/taskexec/send_mail/mail.py \
        --to 'bo.oss.ano@ericsson.com' \
        --subject 'tis_{ts}' \
        --inline_attachment '/export/home/taskexec/send_mail/outbox/{message_filename}' \
        --attachment '/export/home/taskexec/send_mail/outbox/{archive_filename}\''''.format(
        ts = str(ts), 
        message_filename = message_filename,
        archive_filename = archive_filename
    )
)
logging.info("Done.")
