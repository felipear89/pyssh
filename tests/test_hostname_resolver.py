from context import HostnameResolver

def test_hostname_with_port():
    hostnameResolver = HostnameResolver('checkout.qa.mycompany:23')
    hostname = hostnameResolver.get_hostname()
    assert hostname == 'checkout.qa.mycompany'

def test_hostname_without_port():
    hostnameResolver = HostnameResolver('checkout.qa.mycompany')
    hostname = hostnameResolver.get_hostname()
    assert hostname == 'checkout.qa.mycompany'

def test_hostname_with_range_3():
    hostnameResolver = HostnameResolver('checkout-{1-5}.qa.mycompany')
    hostname = hostnameResolver.get_hostname(3)
    assert hostname == 'checkout-3.qa.mycompany'

def test_hostname_with_range_process_1():
    hostnameResolver = HostnameResolver('checkout-{1-5}.qa.mycompany')
    def get_instance_number():
        return 1
    hostnameResolver.get_instance_number = get_instance_number
    hostname = hostnameResolver.get_hostname()
    assert hostname == 'checkout-1.qa.mycompany'

def test_hostname_with_range_process_5():
    hostnameResolver = HostnameResolver('checkout-{1-5}.qa.mycompany')
    def get_instance_number():
        return 5
    hostnameResolver.get_instance_number = get_instance_number
    hostname = hostnameResolver.get_hostname()
    assert hostname == 'checkout-5.qa.mycompany'

def test_hostname_with_range_process_6():
    hostnameResolver = HostnameResolver('checkout-{1-5}.qa.mycompany')
    def get_instance_number():
        return 6
    hostnameResolver.get_instance_number = get_instance_number
    hostname = hostnameResolver.get_hostname()
    assert hostname == 'checkout-1.qa.mycompany'

def test_hostname_with_range_process_10():
    hostnameResolver = HostnameResolver('checkout-{1-5}.qa.mycompany')
    def get_instance_number():
        return 10
    hostnameResolver.get_instance_number = get_instance_number
    hostname = hostnameResolver.get_hostname()
    assert hostname == 'checkout-5.qa.mycompany'

def test_hostname_with_range_process_11():
    hostnameResolver = HostnameResolver('checkout-{1-5}.qa.mycompany')
    def get_instance_number():
        return 11
    hostnameResolver.get_instance_number = get_instance_number
    hostname = hostnameResolver.get_hostname()
    assert hostname == 'checkout-1.qa.mycompany'

def test_is_multiple_hosts():
    hostnameResolver = HostnameResolver('checkout-{1-5}.qa.mycompany')
    is_multiple_hosts = hostnameResolver.is_multiple_hosts()
    assert is_multiple_hosts == True

def test_is_not_multiple_hosts():
    hostnameResolver = HostnameResolver('checkout.qa.mycompany')
    is_multiple_hosts = hostnameResolver.is_multiple_hosts()
    assert is_multiple_hosts == False

def test_start_range():
    hostnameResolver = HostnameResolver('checkout-{2-5}.qa.mycompany')
    start = hostnameResolver.start_range()
    assert start == '2'

def test_end_range():
    hostnameResolver = HostnameResolver('checkout-{2-5}.qa.mycompany')
    end = hostnameResolver.end_range()
    assert end == '5'
