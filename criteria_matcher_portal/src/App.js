import React, { useState } from 'react';
import Tree from './CriteriaTree';
import sample from './sample';
import './App.css';

function App() {
  const [criteriaInput, setCriteriaInput] = useState('');
//  const [criteriaFile, setCriteriaFile] = useState(null);
  const [documentFile, setDocumentFile] = useState(null);
  const [treeData, setTreeData] = useState(sample);

  const handleSubmit = async (e) => {
    e.preventDefault();
    const formData = new FormData();

//    if (criteriaFile) {
//      formData.append('criteria_file', criteriaFile);
//    } else {
      formData.append('criteria_text', criteriaInput);
//    }
    formData.append('document_file', documentFile);

    try {
      const response = await fetch('http://localhost:8080/evaluate-document/', {
        method: 'POST',
        body: formData,
      });
      const data = await response.json();
      setTreeData(data);
    } catch (error) {
      console.error('Error:', error);
    }
  };

  return (
    <div className="App">
      <h1>Document Evaluation App</h1>
      <form onSubmit={handleSubmit} className="upload-form">
        <div className="form-group">
          <label>Criteria Input:</label>
          <textarea
            placeholder="Enter criteria"
            value={criteriaInput}
            onChange={(e) => setCriteriaInput(e.target.value)}
          />
        </div>
        <div className="form-group">
          <label>Target Document:</label>
          <input type="file" accept=".pdf" onChange={(e) => setDocumentFile(e.target.files[0])} required />
        </div>
        <button type="submit" className="submit-btn">Evaluate</button>
      </form>
      {treeData && <Tree data={treeData} />}
    </div>
  );
}


export default App;
