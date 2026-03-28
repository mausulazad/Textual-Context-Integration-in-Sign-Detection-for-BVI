import React from 'react';

const ImageInput = ({ handleImageChange }) => {
    return (
        <div className="image-input">
            <label htmlFor="image-input">
                Upload an image:
                <input
                    id="image-input"
                    type="file"
                    //Later: accept=".jpg, .jpeg, .png"
                    accept=".png"
                    onChange={handleImageChange}
                />
            </label>
        </div>
    );
};

export default ImageInput;