import React from 'react';

const TextInput = ({ handleTextChange }) => {
    return (
        <div className="text-input">
            <label htmlFor="text-input">
                Enter some text:
                <input
                    id="text-input"
                    type="text"
                    onChange={handleTextChange}
                />
            </label>
        </div>
    );
};

export default TextInput;