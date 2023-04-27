import React, { useState } from 'react';
import ImageInput from './components/ImageInput';
import TextInput from './components/TextInput';
import ResultImage from './components/ResultImage';

const App = () => {

  //LATER: Check useState args, based on gpt snippets; if needed
  const [image, setImage] = useState(0);
  const [context, setContext] = useState(0);
  const [resultImageUrl, setResultImageUrl] = useState(null);

  const handleImageChange = (event) => {
    const selectedImage = event.target.files[0];
    setImage(selectedImage);
  };

  const handleTextChange = (event) => {
    setContext(event.target.value);
  };

  const handleSubmit = (event) => {
    event.preventDefault();
    // LATER: 'file' instead of 'image'?
    if (!image || !context) {
      alert('Please select an image and enter the context of the image.');
      return;
    }

    const formData = new FormData();
    formData.append('image', image);
    formData.append('context', context);

    axios.post('http://localhost:5000/api/detect_sign', formData)
      .then((response) => {
        //setResultImageUrl(URL.createObjectURL(file));
        //TRICK: Save images locally
        //setResultImageUrl(response.data.imageUrl);
        setResultImageUrl(response.data);
        //setBoundingBox(response.data.boundingBox);
      })
      .catch((error) => {
        console.error(error);
        alert('Error processing image. Please try again.');
      });
  };

  return (
    <div className="App">
      <h1>Upload an sign image and enter the context of the image</h1>
      <form onSubmit={handleSubmit}>
        <label htmlFor="file-input">Choose an image:</label>
        <input id="image-input" type="file" onChange={handleImageChange} accept="image/*" />
        <br />
        <label htmlFor="text-input">Enter some text:</label>
        <input id="text-input" type="text" value={text} onChange={handleTextChange} />
        <br />
        <button type="submit">Process Image</button>
      </form>
      {resultImageUrl && (
        <div>
          <h2>Processed Image</h2>
          <img src={resultImageUrl} alt="Processed" />
        </div>
      )}
    </div>
  );
};

export default App;


/*
import React from 'react';
import Plot from './Plot';
//import logo from './logo.svg';
//import './App.css';

function App() {
  return (
    <div>
      <h1>Matplotlib Plot</h1>
      <Plot />
    </div>
  );
}


/*
function App() {

  const [currentTime, setCurrentTime] = useState(0);

  useEffect(() => {
    fetch('/api/time').then(res => res.json()).then(data => {
      setCurrentTime(data.time);
    });
  }, []);

  return (
    <div className="App">
      <header className="App-header">
        <img src={logo} className="App-logo" alt="logo" />
        
        <p>
          Edit <code>src/App.js</code> and save to reload.
        </p>
        
        <a
          className="App-link"
          href="https://reactjs.org"
          target="_blank"
          rel="noopener noreferrer"
        >
          Learn React
        </a>

        <p>The current time is {currentTime}.</p>
      </header>
    </div>
  );
}
*/