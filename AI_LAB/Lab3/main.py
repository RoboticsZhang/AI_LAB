from matplotlib import pyplot as plt  # 展示图片
import numpy as np  # 数值处理
import cv2  # opencv库
from sklearn.neighbors import KDTree
from sklearn.linear_model import LinearRegression, Ridge, Lasso  # 回归分析


def read_image(img_path):
    """
    读取图片，图片是以 np.array 类型存储
    :param img_path: 图片的路径以及名称
    :return: img np.array 类型存储
    """
    # 读取图片
    img = cv2.imread(img_path)

    # 如果图片是三通道，采用 matplotlib 展示图像时需要先转换通道
    if len(img.shape) == 3:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)

    return img


def plot_image(image, image_title, is_axis=False):
    """
    展示图像
    :param image: 展示的图像，一般是 np.array 类型
    :param image_title: 展示图像的名称
    :param is_axis: 是否需要关闭坐标轴，默认展示坐标轴
    :return:
    """
    # 展示图片
    plt.imshow(image)

    # 关闭坐标轴,默认关闭
    if not is_axis:
        plt.axis('off')

    # 展示受损图片的名称
    plt.title(image_title)

    # 展示图片
    plt.show()


def save_image(filename, image):
    """
    将np.ndarray 图像矩阵保存为一张 png 或 jpg 等格式的图片
    :param filename: 图片保存路径及图片名称和格式
    :param image: 图像矩阵，一般为np.array
    :return:
    """
    # np.copy() 函数创建一个副本。
    # 对副本数据进行修改，不会影响到原始数据，它们物理内存不在同一位置。
    img = np.copy(image)

    # 从给定数组的形状中删除一维的条目
    img = img.squeeze()

    # 将图片数据存储类型改为 np.uint8
    if img.dtype == np.double:
        # 若img数据存储类型是 np.double ,则转化为 np.uint8 形式
        img = img * np.iinfo(np.uint8).max

        # 转换图片数组数据类型
        img = img.astype(np.uint8)

    # 将 RGB 方式转换为 BGR 方式
    img = cv2.cvtColor(img, cv2.COLOR_RGB2BGR)
    # 生成图片
    cv2.imwrite(filename, img)


def normalization(image):
    """
    将数据线性归一化
    :param image: 图片矩阵，一般是np.array 类型
    :return: 将归一化后的数据，在（0,1）之间
    """
    # 获取图片数据类型对象的最大值和最小值
    info = np.iinfo(image.dtype)

    # 图像数组数据放缩在 0-1 之间
    return image.astype(np.double) / info.max

def noise_mask_image(img, noise_ratio):
    """
    根据题目要求生成受损图片
    :param img: 图像矩阵，一般为 np.ndarray
    :param noise_ratio: 噪声比率，可能值是0.4/0.6/0.8
    :return: noise_img 受损图片, 图像矩阵值 0-1 之间，数据类型为 np.array,
             数据类型对象 (dtype): np.double, 图像形状:(height,width,channel),通道(channel) 顺序为RGB
    """
    # 受损图片初始化
    noise_img = None

    # -------------实现受损图像答题区域-----------------
    # 初始化噪声遮罩为全1矩阵，行、列及通道数与原图一致,分别为np.ndarray.shape[0],np.ndarray.shape[1],np.ndarray.shape[2]
    noise_mask = np.ones((img.shape[0], img.shape[1], img.shape[2]))

    # 逐通道，逐行进行噪声遮蔽
    for chn in range(img.shape[2]):
        for row in range(img.shape[0]):
            # 获得随机遮蔽的序列，首先对列序号进行排序
            random_col = np.random.permutation(img.shape[1])
            # 接着取每列数乘以噪声比率的数目作为被遮蔽的元素
            noise_num = np.array(random_col[:round(noise_ratio * img.shape[1])])
            # 进行遮蔽，即将元素赋值为1
            noise_mask[row, noise_num, chn] = 0
    # 获得受损图像，即原始图像与噪声遮罩逐元素相乘
    noise_img = img * noise_mask
    # -----------------------------------------------

    return noise_img

def get_noise_mask(noise_img):
    """
    获取噪声图像，一般为 np.array
    :param noise_img: 带有噪声的图片
    :return: 噪声图像矩阵
    """
    # 将图片数据矩阵只包含 0和1,如果不能等于 0 则就是 1。
    return np.array(noise_img != 0, dtype='double')


def compute_error(res_img, img):
    """
    计算恢复图像 res_img 与原始图像 img 的 2-范数
    :param res_img:恢复图像
    :param img:原始图像
    :return: 恢复图像 res_img 与原始图像 img 的2-范数
    """
    # 初始化
    error = 0.0

    # 将图像矩阵转换成为np.narray
    res_img = np.array(res_img)
    img = np.array(img)

    # 如果2个图像的形状不一致，则打印出错误结果，返回值为 None
    if res_img.shape != img.shape:
        print("shape error res_img.shape and img.shape %s != %s" % (res_img.shape, img.shape))
        return None

    # 计算图像矩阵之间的评估误差
    error = np.sqrt(np.sum(np.power(res_img - img, 2)))

    return round(error, 3)

from skimage.measure import compare_ssim as ssim
from scipy import spatial

def calc_ssim(img, img_noise):
    """
    计算图片的结构相似度
    :param img: 原始图片， 数据类型为 ndarray, shape 为[长, 宽, 3]
    :param img_noise: 噪声图片或恢复后的图片，
                      数据类型为 ndarray, shape 为[长, 宽, 3]
    :return:
    """
    return ssim(img, img_noise,
                multichannel=True,
                data_range=img_noise.max() - img_noise.min())

def calc_csim(img, img_noise):
    """
    计算图片的 cos 相似度
    :param img: 原始图片， 数据类型为 ndarray, shape 为[长, 宽, 3]
    :param img_noise: 噪声图片或恢复后的图片，
                      数据类型为 ndarray, shape 为[长, 宽, 3]
    :return:
    """
    img = img.reshape(-1)
    img_noise = img_noise.reshape(-1)
    return 1 - spatial.distance.cosine(img, img_noise)

def restore_image(noise_img, size=4):
    """
    使用 你最擅长的算法模型 进行图像恢复。
    :param noise_img: 一个受损的图像
    :param size: 输入区域半径，长宽是以 size*size 方形区域获取区域, 默认是 4
    :return: res_img 恢复后的图片，图像矩阵值 0-1 之间，数据类型为 np.array,
            数据类型对象 (dtype): np.double, 图像形状:(height,width,channel), 通道(channel) 顺序为RGB
    """
    # 恢复图片初始化，首先 copy 受损图片，然后预测噪声点的坐标后作为返回值。
    res_img = np.copy(noise_img)

    # 获取噪声图像
    noise_mask = get_noise_mask(noise_img)

    # -------------实现图像恢复代码答题区域----------------------------
    # 统计像素值为0的比例
    zero_sum = 0
    for row in range(res_img.shape[0]):
        for col in range(res_img.shape[1]):
                if res_img[row, col, 0] == 0:
                    zero_sum += 1
    zero_ratio = zero_sum / (res_img.shape[0] * res_img.shape[1]);
    print(zero_ratio)
    salt_and_pepper_noise = 1
    # 0像素比例较小，为高斯滤波
    if zero_ratio < 0.2:
        salt_and_pepper_noise = 0

    # 是椒盐噪声，采用KNN算法进行恢复
    if salt_and_pepper_noise == 1:
        print("salt_and_pepper_noise")
        for chn in range(res_img.shape[2]):
            res_img_singlechannel = res_img[:, :, chn]
            noise_mask_singlechannel = noise_mask[:, :, chn]
            # 建立数据集
            x_train = []
            x_test = []
            for i, tmp in enumerate(res_img_singlechannel):
                for j, value in enumerate(tmp):
                    # 受损元素点作为测试集
                    if value < 0.1:
                        # 将下标加入测试集，作为索引点
                        x_test.append([i, j])
                    # 未受损的元素点作为训练集
                    else:
                        # 将下标加入数据集，以建立KDTree
                        x_train.append([i, j])
            # 转换为np.array
            x_train = np.array(x_train)
            x_test = np.array(x_test)
            # 存储测试集中的元素值，并转换为np.array
            y_train = [res_img_singlechannel[img_index[0]][img_index[1]] for img_index in x_train]
            y_train = np.array(y_train)
            # 以训练集建立KDTree
            KD_Tree = KDTree(x_train)
            KDTree_dist, KDTree_index = KD_Tree.query(x_test, k=3)
            # 更新过程，通过KNN的思想来更新质心值
            update_value_list = np.sum(y_train[KDTree_index] / KDTree_dist, axis=1) / np.sum(1 / KDTree_dist, axis=1)
            # 恢复受损图像
            for i in range(x_test.shape[0]):
                # 获得更新值
                update_value = update_value_list[i]
                # 更新受损元素点的元素值
                res_img[[x_test[i][0]], [x_test[i][1]], [chn]] = update_value

    # 是高斯噪声，采用均值滤波
    else:
        print("gauss_noise")
        size = 3
        rows, cols, channel = res_img.shape
        for row in range(res_img.shape[0]):
            for col in range(res_img.shape[1]):
                for chn in range(res_img.shape[2]):
                    if res_img[row, col, chn] > 0.2:
                        continue
                    mean_list = []
                    # 长宽是以 size*size 方形区域获取区域, 默认是 4
                    for i in range(row - size, row + size):
                        if i < 0 or i >= rows:
                            continue
                        for j in range(col - size, col + size):
                            if j < 0 or j >= cols:
                                continue
                            mean_list.append(res_img[i, j, chn])
                    if len(mean_list) == 0:
                        mean_list = [0]
                    # 计算均值
                    res_img[row, col, chn] = np.mean(mean_list, axis=0)
    # ---------------------------------------------------------------
    return res_img

def main():
    # 原始图片
    # 加载图片的路径和名称
    # 加载图片的路径和名称
    img_path = 'potala_palace.png'

    # 读取原始图片
    img = read_image(img_path)

    # 展示原始图片
    plot_image(image=img, image_title="original image")

    # 生成受损图片
    # 图像数据归一化
    nor_img = normalization(img)

    # 噪声比率
    noise_ratio = 0.4

    # 生成受损图片
    #noise_img = noise_mask_image(nor_img, noise_ratio)
    Noise_img = read_image('potala_palace_noise.png')
    noise_img = normalization(Noise_img)

    if noise_img is not None:
        # 展示受损图片
        plot_image(image=noise_img, image_title="noise image")

        # 恢复图片
        res_img = restore_image(noise_img)

        # 计算恢复图片与原始图片的误差
        print("恢复图片与原始图片的评估误差: ", compute_error(res_img, nor_img))
        print("恢复图片与原始图片的 SSIM 相似度: ", calc_ssim(res_img, nor_img))
        print("恢复图片与原始图片的 Cosine 相似度: ", calc_csim(res_img, nor_img))

        # 展示恢复图片
        plot_image(image=res_img, image_title="restore image")

        # 保存恢复图片
        save_image('res_' + img_path, res_img)
    else:
        # 未生成受损图片
        print("返回值是 None, 请生成受损图片并返回!")

if __name__ == '__main__':
    main()