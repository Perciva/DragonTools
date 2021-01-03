import subprocess

def tshark(fname):
    args = ['tshark', '-r', fname]
    proc = subprocess.Popen(args, stdout=subprocess.PIPE, shell=False)
    out,err = proc.communicate()
    if out:
        return out.decode('utf-8').split('\n')
    return err.decode('etf-8').split('\n')