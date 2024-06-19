import axios from 'axios';
import { useState } from 'react';
import './PokerAssistant.css';

const PokerAssistantApp = () => {
  const [hand, setHand] = useState('');
  const [analysis, setAnalysis] = useState('');
  const [analysisHistory, setAnalysisHistory] = useState([]);
  const [isLoading, setIsLoading] = useState(false);

  const analyzeHand = async () => {
    setIsLoading(true);
    const result = await axios.get(`https://api.pokerhands.com/analyze?hand=${hand}`);
    setAnalysis(result.data);
    setAnalysisHistory(oldHistory => [...oldHistory, result.data]);
    setIsLoading(false);
  };

  return (
    <div className="PokerAssistant">
      <input
        value={hand}
        onChange={(e) => setHand(e.target.value)}
        placeholder="Enter hand"
      />
      <button onClick={analyzeHand} disabled={isLoading}>
        Analyze Hand
      </button>
      {isLoading ? (
        <div>Loading...</div>
      ) : (
        <div>{analysis}</div>
      )}
      <div>
        <h2>Analysis History</h2>
        {analysisHistory.map((analysis, index) => (
          <div key={index}>{analysis}</div>
        ))}
      </div>
    </div>
  );
};

export default PokerAssistantApp;