# http://www.pythonchallenge.com/pc/return/dispropotion.html

import xmlrpc.client

prompt = "http://www.pythonchallenge.com/pc/phonebook.php"
evil_name = "Bert"  # http://www.pythonchallenge.com/pc/return/evil4.jpg


def main():
    rpc = xmlrpc.client.ServerProxy(prompt)

    help_template = "{}:\n\t{}\n"

    methods = rpc.system.listMethods()
    for method in methods:
        msg = help_template.format(method, rpc.system.methodHelp(method))
        print(msg)

    result = rpc.phone("Bert")
    return result


if __name__ == "__main__":
    print(main())


# http://www.pythonchallenge.com/pc/return/italy.html
