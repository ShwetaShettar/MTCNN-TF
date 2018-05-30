#coding:utf-8
from mtcnn_model import P_Net
from train import train


def train_PNet(base_dir, prefix, load_epoch,end_epoch, display, lr):
    """
    train PNet
    :param dataset_dir: tfrecord path
    :param prefix:
    :param end_epoch:
    :param display:
    :param lr:
    :return:
    """
    net_factory = P_Net
    train(net_factory,prefix,load_epoch, end_epoch, base_dir, display=display, base_lr=lr)

if __name__ == '__main__':
    #data path
    base_dir = '../prepare_data/caltech_imglists/PNet'
    model_name = 'MTCNN_caltech_model'
    #model_path = '../data/%s_model/PNet/PNet' % model_name
    #with landmark
    model_path = '../data/%s/PNet_landmark/PNet' % model_name
    load_epoch = 20      
    prefix = model_path
    end_epoch = 300000
    display = 1000
    lr = 0.01
    train_PNet(base_dir, prefix,load_epoch, end_epoch, display, lr)