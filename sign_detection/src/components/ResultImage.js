import React from 'react';

const ResultImage = ({ imageUrl }) => {
    return (
        <div className="result-image">
            {imageUrl ? (
                <img src={imageUrl} alt="Result" />
            ) : (
                <p>No result yet.</p>
            )}
        </div>
    );
};

export default ResultImage;