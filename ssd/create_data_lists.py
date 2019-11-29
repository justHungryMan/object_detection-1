from utils import create_data_lists, create_custom_data

if __name__ == '__main__':

    create_data_lists(voc07_path='VOC2007',
                      save_path='../data',
                      output_folder='data')


    create_custom_data(data_path='../data',
                      output_folder='../data')
    
