import sys
import getopt
import os
from PIL import Image 


def usage():
    print('USAGE:')
    print('JPGtoPNGconverter.py -i <inputdir> -o <outputdir>')
    print('or')
    print('JPGtoPNGconverter.py --idir <inputdir> --odir <outputdir>')

def grab_args(argv):
    ''' 
    grab the 1st and the 2nd arguments.
    '''
    try:
        opts, args = getopt.getopt(argv,"hi:o:",["idir=", "odir="])
    except getopt.GetoptError:  
        usage()      
        sys.exit(2)

    idir_default = '.\\Pokedex\\'
    odir_default = '.\\new\\'

    output_dir = ''
    input_dir = ''

    for opt, arg in opts:
        if opt == '-h':
            usage()
            sys.exit()
        elif opt in ('-i', "--idir"):
            input_dir = arg
        elif opt in ('-o', "--odir"):
            output_dir = arg

    if input_dir == '':
        print('Used defauld value {} for <inputdir>'.format(idir_default))
        input_dir = idir_default

    if output_dir == '':
        print('Used defauld value {} for <outputdir>'.format(odir_default))
        output_dir = odir_default

    return input_dir, output_dir


def main(argv):

    input_dir, output_dir = grab_args(argv)
    
    print(f'Input dir:  {input_dir}')
    print(f'Output dir: {output_dir}')

    # check is /new exists and create it.
    if not os.path.isdir(output_dir):
        os.mkdir(output_dir)

    # loop through Pokedex and convert all images to png.
    # save images to the new folder.

    for filename in os.listdir(input_dir):
        
        if filename[-3:] == 'jpg':
            new_name = os.path.splitext(filename)[0]

            img = Image.open(f'{input_dir}{filename}')
            img.save(f'{output_dir}{new_name}.png','png')



if __name__ == '__main__':
    main(sys.argv[1:])