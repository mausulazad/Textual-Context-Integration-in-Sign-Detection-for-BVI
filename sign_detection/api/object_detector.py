from utils.input_modifier import modify_image, modify_context
import torch
import numpy as np

def detect_object(image, context, model, tokenizer):

    # PIL Image
    image = modify_image(image)
    context = modify_context(context, tokenizer)
    
    '''
    # NOT DONE: TEST AFTER MODEL INTEGRATION
    #bbox_preds, classification_preds = model.forward(image, context)
    # vfe_in, tfe_in
    #predictions = model(image, context)
    predictions = model.forward(image, context)
    '''

    # LATER: Remove after testing
    c = (150.0, 145.0, 390.0, 208.0)
    c = np.asarray(c)
    c = torch.from_numpy(c)
    #c = torch.unsqueeze(c, dim=0)
    c = torch.stack((c,), dim=0)
    
    d = (0.70, 0.30)
    d = np.asarray(d)
    d = torch.from_numpy(d)
    #c = torch.unsqueeze(c, dim=0)
    d = torch.stack((d,), dim=0)

    predictions = (c,d)

    return predictions
