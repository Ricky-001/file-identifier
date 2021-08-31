#/usr/bin/python3
import argparse
from utilities.colors import color
from utilities.tools import clear
from signatures import signature

def extractSignature(filename):
    try:
        with open(filename,'rb') as f:
            content = f.read(24)
    except FileNotFoundError:
        print('{}[-] File not found!\n{}[!]{} Please ensure that the filename along with the path is typed correctly'.format(color.RED,color.YELLOW,color.END))
        quit()
    hexa = ''.join([hex(x) for x in content])
    hexa = hexa.replace('0x',' ').strip()
    sig=''
    for h in hexa.split(' '):
        if len(h)==1:
            sig+='0'+h+' '
        else:
            sig+=h+' '
    return sig


def identify(filename):

    Signature = extractSignature(filename)

    Filename = filename.replace('\\','/').split('/')[-1]
    Extension = Filename.split('.')[-1] if len(Filename.split('.')) > 1 else 'No extension identified'
    print('{}[+]{} Extension identified for filename {}{}{} = {}{}{}'.format(color.BLUE,color.END,color.YELLOW,Filename,color.END,color.GREEN,Extension,color.END))

    for sig in signature.sigs.values():
        for head in sig:
            if Signature.startswith(head.lower()):
                ext = [key for key,val in signature.sigs.items() if head in val]
                print('{}[+]{} Identified possible file type as : {}{}{}'.format(color.GREEN,color.END,color.YELLOW,*ext,color.END))
                print('{}[!]{} Identified signature = {}{}{} '.format(color.GREEN,color.END,color.YELLOW,head,color.END))

                if Extension in ext[0]:
                    print('{}[!]{} Identified type {}{} {}matches{} with the file extension {}{}{}'.format(color.BLUE,color.END,color.YELLOW,*ext,color.ORANGE,color.END,color.YELLOW,Extension,color.END))
                else:
                    print('{}[!]{} Identified type {}{} {}does not match{} with the file extension {}{}{}'.format(color.BLUE,color.END,color.YELLOW,*ext,color.ORANGE,color.END,color.YELLOW,Extension,color.END))
                    print('{}[*]{} Consider changing file type to identified {}{}{} format'.format(color.BLUE,color.END,color.ORANGE,*ext,color.END))
                quit()
    print('{}[-]{} No possible known filetype identified {}(can be TXT/Plain){}'.format(color.RED,color.END,color.ORANGE,color.END))
    print('{}[!]{} File header/ signature = {}{}{} '.format(color.GREEN,color.END,color.YELLOW,head,color.END))


def main():
    try:
        clear()
        
        # script description
        parser = argparse.ArgumentParser(description='File type detection tool')
        parser.add_argument('-f','--file', help='The file to identify')
        args = parser.parse_args() 

        # parsing command line argumets (provided the necvessary ones are given)
        if args.file:
            filename = args.file
            identify(filename)
        # if no arguments are provided except for positional (TEXT)
        else:
            filename = input('{}[?]{} Enter the filename: '.format(color.BLUE,color.END))
            identify(filename)

    except KeyboardInterrupt:
        print('\n{}[!] Exiting...{}'.format(color.RED,color.END))
        quit()

if __name__ == '__main__':
    main()
