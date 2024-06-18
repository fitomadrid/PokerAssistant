import axios from 'axios';
import { useState } from 'react';
import './PokerAssistant.css';

const PokerAssistantApp = () => {
  const [hand, setHand] = useState('');
  const [analysis, setAnalysis] = useState('');
  const [isLoading, setIsLoading] = useState(false);
  
  const analyzeHand = async () => {
    if (!hand) {
      alert('Please enter your poker hand to analyze.');
      return;
    }

    try {
      setIsLoading(true);
      const response = await axios.post(process.env.REACT_APP_BACKEND_URL + '/analyze-hand', { hand });
      setAnalysis(response.data.analysis);
    } catch (error) {
      console.error('Error fetching analysis:', error);
      setAnalysis('Failed to fetch analysis.');
    } finally {
      setIsLoading(false);
    }
  };

  return (
    <div className="pokerAssistantApp">
      <h1>Poker Assistant</h1>
      <input
        type="text"
        placeholder="Enter your poker hand"
        value={hand}
        onChange={(e) => setHand(e.target.value)}
      />
      <button onClick={analyzeSmoothie} disabled={isLoading}>
        {isLoading ? 'Analyzing...' : 'Analyze Hand'}
      </button>
      {analysis && <div className="analysisResult">{analysis}</div>}
    </div>
  );
};

export default PokerAssistantApp;