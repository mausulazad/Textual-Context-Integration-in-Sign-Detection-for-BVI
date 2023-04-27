from utils.input_modifier import modify_image, modify_context

def detect_object(image, context, model, tokenizer):

    # PIL Image
    image = modify_image(image)
    context = modify_context(context, tokenizer)
    
    #bbox_preds, classification_preds = model.forward(image, context)
    # vfe_in, tfe_in
    predictions = model(image, context)

    return predictions
