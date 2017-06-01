import database
import re
import sqlite3

class HostnameResolver:
    
    def __init__(self, value):
        self.value = value
        self.hostname = value if not self.has_port(value) else value[:value.find(':')]
    
    def is_multiple_hosts(self):
        return re.match('.*{\d+\-\d+}.*', self.hostname)

    def get_instance_number(self):
        try:
            row = database.execute('select max(instance)+1 from control where datetime(\'now\') < \
                datetime(time, \'+1 minutes\')').fetchone()
            next_val = 1 if row[0] is None else row[0]
            print(next_val)
            database.execute('insert into control(instance, time) values (?, datetime(\'now\'))', (next_val,))
            database.con.commit()
            return next_val
        except sqlite3.OperationalError:
            self.get_instance_number()

    def get_hostname(self, instance):
        if not self.is_multiple_hosts():
            return self.hostname
        instance_number = instance if instance is None else \
            self.get_instance_number()
        return re.sub(r'\{.*\}', '%s' % instance_number, self.hostname)

    def get_port(self, default_port=22):
        return self.value[self.value.find(':')+1:] if self.has_port(self.value) else default_port

    def has_port(self, str):
        return ':' in str
