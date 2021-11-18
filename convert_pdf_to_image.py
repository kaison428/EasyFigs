# import poppler
from pdf2image import convert_from_path
import glob
import os

def convert_pdf_to_image(file_path):
    file_name = file_path.split('/')[-1].split('.pdf')[0]
    print("Now processing file: {}".format(file_path))

    # extract images
    images = convert_from_path(file_path)
    image_folder = os.path.join('images', file_name)

    try:
        os.mkdir(image_folder)
    except:
        pass

    # save images
    try:
        for i in range(len(images)):
            image_path = os.path.join(image_folder, file_name+'_page'+str(i+1)+'.jpg')
            images[i].save(image_path, 'JPEG')

        print("File {} is finished converting from PDF to Img".format(file_name))
    except:
        print('LOGGING: file {} cannot be extracted'.format(file_path))

    return image_folder

# convert_pdf_to_image('pdf/solutions_midterm_Fall_2021.pdf')
