import os
import uuid

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as patches


def draw_image(image, bbox, label):

    fig, ax = plt.subplots()
    ax.imshow(np.array(image)[::-1], origin='lower')

    x, y, w, h = bbox[0][0].item(), bbox[0][1].item(), bbox[0][2].item(), bbox[0][3].item()
    x, y, w, h = np.array([x, y, w, h])
    
    x1 = x
    y1 = y

    rect = patches.Rectangle((x1, y1), w, h, linewidth=1, edgecolor='b', facecolor='none')
    ax.add_patch(rect)

    label_map = {
        0: 'Exit',
        1: 'Fire Alarm'
    }

    k = 10

    target_label_x = x1 + w/2 - k
    target_label_y = y1 + h + k

    ax.text(x=target_label_x, y=target_label_y, s=label_map[label], color='blue')

    #image_folder = 'images'
    image_file_id = str(uuid.uuid1())
    image_file_id = image_file_id.replace('-', '_')
    image_file_name = f'{image_file_id}.png'
    #image_file_name = os.path.join(image_folder, image_file_name)

    # plt.savefig(image_file_name)
    fig.savefig(image_file_name)

    return image_file_name
