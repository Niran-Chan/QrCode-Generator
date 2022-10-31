import sys
import qrcode
import datetime
import os



path = os.getcwd()



def generate(in_file):
    
    f_in = open(in_file,"r")
    exist = False
    dirs = os.listdir(path)
    for _ in dirs:

        if( in_file.strip('./').strip('.txt') == _  ):
            exist = True
    
    if(exist == False):
        os.mkdir(path + in_file.strip('.txt'))

    os.chdir(path + in_file.strip('.txt'))
    #Open file
    for _ in f_in:
	#Initialise QR Class
        qr=qrcode.QRCode(version=1,error_correction=qrcode.constants.ERROR_CORRECT_L,box_size=10,border=4)
        qr.add_data(_)
        qr.make(fit=True)
        img = qr.make_image(fill_color="black",back_color="white")
        img.save(_.strip("\n") + ".jpg")
       #img.show()
        
    f_in.close()
    return


if __name__ == '__main__':
    try:
        in_file = './' + input("What is the name of the file that contains a list of your asset tags?\n")
        print("Generating QR Codes")
        generate(in_file)

    except Exception as err:
        print(err)
    
