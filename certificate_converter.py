import argparse
import OpenSSL

def read_certificate(ca_cert):
    with open(ca_cert, mode='rb') as file:
        return OpenSSL.crypto.load_certificate(OpenSSL.crypto.FILETYPE_PEM, file.read())

def read_private_key(ca_key, passphrase=None):
    with open(ca_key, mode='rb') as file:
        return OpenSSL.crypto.load_privatekey(OpenSSL.crypto.FILETYPE_PEM, file.read(), passphrase=passphrase)

def export_to_pkcs12(filename, key, cert, passphrase=None):
    pkcs = OpenSSL.crypto.PKCS12()
    pkcs.set_privatekey(key)
    pkcs.set_certificate(cert)
    with open(filename, 'wb') as file:
        file.write(pkcs.export(passphrase=passphrase))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='This utility converts a PEM formatted certificate/private key to PKCS12.')
    parser.add_argument('--key',  help='Private key filename, PEM encoded.')
    parser.add_argument('--cert', help='Certificate filename, PEM encoded.')
    parser.add_argument('--passphrase', help='Passphrase for the private key.', default=None)
    parser.add_argument('--out',  help='Output filename (.pfx).')

    args = parser.parse_args()
    key_path   = args.key
    cert_path  = args.cert
    passphrase = args.passphrase
    out_path   = args.out

    if len(key_path) == 0 or len(cert_path) == 0 or len(out_path) == 0:
        parser.print_usage()
        exit(1)

    if len(passphrase) == 0:
        passphrase = None
    else:
        passphrase = passphrase.encode()

    key  = read_private_key(key_path, passphrase)
    cert = read_certificate(cert_path)
    export_to_pkcs12(out_path, key, cert, passphrase)