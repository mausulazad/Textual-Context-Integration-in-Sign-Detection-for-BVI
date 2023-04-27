import torch
import torch.nn.functional as F
import torchvision.transforms as transforms


def modify_image(image):
    # LATER: TEST & DEBUG
    
    '''
    Steps:
    ......
    1. Make sure that the image shape is either (720,540) or (540,720)
    2. Use transforms.compose to convert into pytorch tensor
    3. Pad to get equal shape for all images
    4. Unsqueeze dimension for batch size
    '''

    # Step 1: LATER

    
    # Convert from PIL image to PyTorch tensor
    transform_image =  transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize(
            mean=[0.485, 0.456, 0.406],
            std=[0.229, 0.224, 0.225]
        )
    ])

    '''
    image = np.array(image)
    image = torch.from_numpy(image).permute(2,0,1).float()
    '''
    # Expected Type: tensor
    # Expected Shape: [3, 540, 720] or [3, 720, 540]
    image = transform_image(image)

    # Pad the tensor
    desired_image_size = (800, 800)
    
    h_padding = desired_image_size[0] - image.shape[1]
    w_padding = desired_image_size[1] - image.shape[2]

    # Expected Shape: [3, 800, 800]
    image = F.pad(image, (0, w_padding, 0, h_padding))

    # Unsqueeze batch dimension
    # Expected Shape: [1, 3, 800, 800]
    image = torch.unsqueeze(image, dim=0)

    return image


def modify_context(context, tokenizer, max_seq_len=30):
    # LATER: TEST & DEBUG

    '''
    Steps:
    ......

    0. Check 'context' type: 'str'
    1. Generate word_id and word_mask
    2. Convert them to pytorch tensor
    3. Unsqueeze the batch dimension
    4. Create a new dictionary 'context_data'
    5. Place 'word_id' and 'word_mask' in 'context_data' dict
    '''

    # Step 0: LATER

    # Generate word_id and word_mask
    tokenization_details = tokenizer(context, padding='max_length', max_length=max_seq_len)
    word_id, word_mask = tokenization_details["input_ids"], tokenization_details["attention_mask"]

    # Convert 'word_id' and 'word_mask' to PyTorch tensor
    # Expected Shape: [30]
    word_id, word_mask = torch.IntTensor(word_id), torch.IntTensor(word_mask)

    # Unsqueeze batch dimension
    # Expected Shape: [1, 30]
    word_id = torch.unsqueeze(word_id, dim=0)
    word_mask = torch.unsqueeze(word_mask, dim=0)

    # Create a new dictionary 'context_data' and place 'word_id' and 'word_mask' in it
    context_data = dict()
    context_data['input_ids'] = word_id
    context_data['attention_mask'] = word_mask

    return context_data

    #_, predicted = torch.max(classification_preds.data, 1)
    pass